# Carga el modelo, la clave y el modo de funcionamiento del taller.
# Lee .env desde la raíz del repositorio mediante python-dotenv.
# cliente_ia.py utiliza esta configuración para elegir la conexión.

import os
from pathlib import Path
from dotenv import load_dotenv

# Buscamos .env sin depender de la carpeta actual de la terminal.
RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")

# La URL es fija para no enviar la clave a otro servidor por accidente.
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODELO = os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3.3-70b-instruct").strip()
MODO = os.getenv("CHARLA_MODO", "real").strip().lower()
MAX_TOKENS = 600


def obtener_api_key():
    """Devuelve la clave privada sin mostrarla."""
    clave = os.getenv("OPENROUTER_API_KEY", "").strip()
    if not clave or clave in {"TU_API_KEY", "PEGA_AQUI_TU_CLAVE"}:
        raise ValueError("Copia .env.example como .env e introduce OPENROUTER_API_KEY.")
    return clave
