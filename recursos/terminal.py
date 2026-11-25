# Proporciona una salida uniforme para errores de los retos.
# Se conecta con los scripts de retos al ejecutar sus funciones main.
# Evita mostrar trazas innecesarias a alumnos principiantes.


def ejecutar(main):
    """Ejecuta un reto y devuelve un código de salida."""
    try:
        main()
    except NotImplementedError as error:
        print(f"Pendiente: {error}")
        print("Lee el README del reto y abre una pista si la necesitas.")
        return 1
    except (ValueError, RuntimeError, OSError) as error:
        print(f"Error: {error}")
        return 1
    except (KeyboardInterrupt, EOFError):
        print("\nHasta pronto.")
    return 0
