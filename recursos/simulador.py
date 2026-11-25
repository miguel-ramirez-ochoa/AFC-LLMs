# Devuelve respuestas artificiales para ensayar sin Internet.
# cliente_ia.py usa este módulo cuando CHARLA_MODO=simulado.
# No es un LLM: solo verifica el flujo de mensajes y no consume créditos.


def responder_simulado(mensajes):
    """Muestra qué clases de mensajes ha recibido el cliente."""
    # Contamos mensajes para observar el contexto sin copiar datos privados.
    instrucciones = sum(m["role"] == "system" for m in mensajes)
    preguntas = sum(m["role"] == "user" for m in mensajes)
    respuestas = sum(m["role"] == "assistant" for m in mensajes)
    return (f"[SIMULACIÓN, no IA] Recibidos: {instrucciones} system, "
            f"{preguntas} user y {respuestas} assistant. "
            "La conexión de tu código funciona en modo local de prueba.")
