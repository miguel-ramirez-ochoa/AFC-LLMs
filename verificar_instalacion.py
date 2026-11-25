# Comprueba Python, dependencias y configuración antes de los retos.
# Lee config.py y usa cliente_ia.py solo si se indica --api.
# Sin --api no hace peticiones ni consume tokens.

import argparse
import importlib.util
import sys


def main():
    # Permitimos comprobar la API real de forma explícita.
    parser = argparse.ArgumentParser(description="Verificador del taller")
    parser.add_argument("--api", action="store_true", help="Hace una consulta de prueba")
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        print("Necesitas Python 3.10 o posterior. Revisa INSTALACION.md y recrea el venv con una versión compatible.")
        return 1
    faltan = [m for m in ("requests", "dotenv") if importlib.util.find_spec(m) is None]
    if faltan:
        print("Faltan dependencias. Con el venv activo, ejecuta python -m pip install -r requirements.txt")
        return 1

    import config
    print(f"Python {sys.version.split()[0]} | Modelo: {config.MODELO} | Modo: {config.MODO}")
    try:
        if config.MODO not in {"real", "simulado"}:
            raise ValueError("CHARLA_MODO debe ser real o simulado.")
        if config.MODO == "real":
            config.obtener_api_key()
            if not config.MODELO:
                raise ValueError("Falta OPENROUTER_MODEL.")
            print("Clave presente (no mostrada). Aún no se ha validado con el proveedor.")
        else:
            print("Modo simulado: no requiere clave.")
        if args.api:
            from cliente_ia import preguntar_ia
            print(preguntar_ia([{"role": "user", "content": "Responde solo: OK"}]))
            print("Prueba de petición completada.")
        else:
            print("Configuración local correcta. Para probar el servicio: python verificar_instalacion.py --api")
    except (RuntimeError, ValueError) as error:
        print(f"Error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
