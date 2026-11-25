# Envía mensajes a un LLM y devuelve su respuesta como texto.
# Conecta con la API de OpenRouter usando config.py y requests.
# Los cinco retos llaman a preguntar_ia() sin gestionar credenciales.

import requests
import config


def preguntar_ia(mensajes):
    """Recibe una lista de mensajes con role y content; devuelve str."""
    # Detectamos estructuras incorrectas antes de gastar tokens.
    if not isinstance(mensajes, list) or not mensajes:
        raise ValueError("Se necesita una lista no vacía de mensajes.")
    for mensaje in mensajes:
        if (not isinstance(mensaje, dict)
                or mensaje.get("role") not in {"system", "user", "assistant"}
                or not isinstance(mensaje.get("content"), str)
                or not mensaje["content"].strip()):
            raise ValueError("Cada mensaje necesita role válido y content de texto no vacío.")
    if not any(m["role"] == "user" for m in mensajes):
        raise ValueError("Incluye al menos un mensaje del usuario.")

    # El simulador permite probar el flujo sin Internet ni credenciales.
    if config.MODO == "simulado":
        from recursos.simulador import responder_simulado
        return responder_simulado(mensajes)
    if config.MODO != "real":
        raise ValueError("CHARLA_MODO debe ser real o simulado.")
    if not config.MODELO:
        raise ValueError("OPENROUTER_MODEL no puede estar vacío.")

    # Autenticamos la petición y limitamos la longitud de la generación.
    cabeceras = {"Authorization": f"Bearer {config.obtener_api_key()}"}
    datos = {"model": config.MODELO, "messages": mensajes,
             "max_tokens": config.MAX_TOKENS, "stream": False}
    try:
        respuesta = requests.post(config.OPENROUTER_URL, headers=cabeceras,
                                 json=datos, timeout=(10, 75), allow_redirects=False)
    except requests.Timeout:
        raise RuntimeError("La API tardó demasiado. Prueba de nuevo manualmente.") from None
    except requests.RequestException:
        raise RuntimeError("No se pudo conectar con OpenRouter. Revisa Internet.") from None

    # No mostramos la respuesta de error sin filtrar: puede contener datos privados.
    errores = {400: "Petición inválida: revisa mensajes y modelo.",
               401: "API key inválida o revocada.",
               402: "Saldo o límite de gasto de la clave agotado.",
               403: "Acceso denegado al modelo.",
               404: "Modelo o ruta no disponible.",
               429: "Límite de peticiones alcanzado; consulta al ponente."}
    if respuesta.status_code != 200:
        detalle = errores.get(respuesta.status_code, "Servicio no disponible o error inesperado.")
        raise RuntimeError(f"HTTP {respuesta.status_code}: {detalle}")

    # Extraemos solo el texto generado del JSON devuelto por la API.
    try:
        cuerpo = respuesta.json()
        if cuerpo.get("error"):
            raise ValueError("La respuesta contiene un error.")
        texto = cuerpo["choices"][0]["message"]["content"]
        if not isinstance(texto, str) or not texto.strip():
            raise ValueError("Respuesta vacía.")
    except (ValueError, KeyError, IndexError, TypeError, AttributeError):
        raise RuntimeError("Respuesta sin texto válido. Revisa el modelo o el límite de salida.") from None
    return texto.strip()
