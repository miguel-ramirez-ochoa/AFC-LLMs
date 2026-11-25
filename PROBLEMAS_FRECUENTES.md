# Problemas frecuentes

[← Volver al README](README.md) · [Guía de instalación](INSTALACION.md)

## Python, terminal y venv

| Mensaje o síntoma | Qué hacer |
|---|---|
| `command not found: python` en macOS | Activa `.venv` o usa el ejecutable `python3.12` para crearlo. `python` puede no existir fuera del entorno. |
| `Necesitas Python 3.10 o posterior` | Comprueba `python --version`. Si el venv se creó con Python 3.9, hay que recrearlo con una versión compatible. |
| `py` no reconocido en Windows | Comprueba `python --version`. Si tampoco funciona, instala Python con permiso y abre una terminal nueva. |
| PowerShell bloquea `Activate.ps1` | Usa `.\.venv\Scripts\python.exe` en lugar de `python` en todos los comandos, sin cambiar la política de seguridad. |
| `No module named venv` o `ensurepip is not available` | En Linux puede faltar el paquete de venv de tu versión de Python. Instálalo con permiso o solicita ayuda. |
| `ModuleNotFoundError: requests` o `dotenv` | Comprueba que usas el intérprete de `.venv` e instala `python -m pip install -r requirements.txt` ahí. |
| No encuentra `requirements.txt` o `verificar_instalacion.py` | Estás en otra carpeta. Entra en la raíz del repositorio y comprueba sus archivos con `ls` o `Get-ChildItem`. |
| No encuentra `01_hola_ia.py` | Los retos están organizados en carpetas. Usa `python -m retos.reto01.reto` desde la raíz. |
| `No module named retos` o `cliente_ia` | Ejecuta desde la raíz con `python -m retos.reto01.reto`, no haciendo doble clic en `reto.py`. |
| Aviso sobre pip desactualizado | Si la instalación termina correctamente, no hace falta actualizar pip durante el taller. |
| Error de permisos o conexión al instalar | No utilices `sudo pip` ni desactives verificaciones TLS. Consulta al ponente; puedes trabajar en pareja. |

### Recrear un venv que usa un Python antiguo

Hazlo únicamente en la raíz de tu proyecto. No elimines tu código ni `.env`. Si `.venv` está activo, desactívalo primero con `deactivate`. En lugar de borrarlo, podemos renombrarlo para conservarlo temporalmente. Si `.venv_antiguo` ya existe, elige otro nombre.

**macOS/Linux (ejemplo con Python 3.12):**

```bash
mv .venv .venv_antiguo
python3.12 -m venv .venv
source .venv/bin/activate
python --version
python -m pip install -r requirements.txt
```

**Windows (PowerShell, ejemplo con Python 3.12):**

```powershell
Rename-Item .venv .venv_antiguo
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
python -m pip install -r requirements.txt
```

Usa la versión compatible que realmente tengas instalada. Si PowerShell bloquea la activación, aplica la alternativa indicada arriba. No subas ningún entorno a GitHub.

## Configuración y OpenRouter

| Mensaje | Qué hacer |
|---|---|
| `Copia .env.example como .env e introduce OPENROUTER_API_KEY` | Comprueba que has creado `.env` en la raíz, que no acaba en `.txt` y que la clave está en la primera variable. No enseñes la clave. |
| Aparece otro modelo en el verificador | Comprueba `OPENROUTER_MODEL=meta-llama/llama-3.3-70b-instruct` en `.env`. Si sigue apareciendo otro, una variable de entorno externa podría tener prioridad: solicita ayuda. |
| `HTTP 400` | Revisa la estructura de mensajes y la configuración del modelo. |
| `HTTP 401` o `403` | Clave inválida, caducada, revocada o acceso denegado. Avisa al ponente sin mostrar la clave. |
| `HTTP 402` | Saldo o límite de gasto agotado. Avisa al ponente. No cargues dinero por tu cuenta. |
| `HTTP 404` | Modelo o ruta no disponible. No cambies de modelo sin consultar. |
| `HTTP 429` | Límite temporal de peticiones. Espera unos segundos, reintenta una sola vez si te lo indican o avisa al ponente. |
| Timeout, `HTTP 5xx` o problema de red | Consulta al ponente. No ejecutes reintentos automáticos ni bucles de peticiones. |
| `Respuesta sin texto válido` | El proveedor no devolvió texto utilizable. Avisa al ponente si se repite; no significa necesariamente que el ejercicio esté mal. |

## Retos y pruebas

- «Pendiente» o `NotImplementedError`: los TODO son intencionados. Lee el README del reto y completa el código.
- Las pruebas de infraestructura deben pasar desde el inicio: `python -m unittest discover -s tests -v`.
- Las comprobaciones de los retos 1–4 fallan inicialmente a propósito. Ejecuta las del reto correspondiente, por ejemplo `python -m unittest tests.comprobar_retos.Reto1 -v`.
- Las pruebas simuladas verifican la estructura del programa; no garantizan que una respuesta real sea correcta. Comprueba también los ejemplos del reto con el LLM.

## Si no funciona Internet

Con las dependencias ya instaladas, cambia `CHARLA_MODO=real` por `CHARLA_MODO=simulado` en `.env`. No necesita clave, no llama a OpenRouter ni consume saldo. Permite comprobar los mensajes y el historial; **no genera respuestas inteligentes**. Vuelve a `real` cuando el ponente lo indique.

## Cómo pedir ayuda

Muestra el mensaje de error, la versión de Python y qué comando ejecutaste. Nunca muestres el contenido de `.env`, ni lo compartas con ChatGPT, Claude u otras herramientas. Si el problema es de instalación, puedes avanzar con un compañero mientras lo resolvemos.
