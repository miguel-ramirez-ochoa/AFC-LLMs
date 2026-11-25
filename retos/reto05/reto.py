# Reto 5: diseña tu propio asistente en terminal.
# Puedes reutilizar tu trabajo anterior y cliente_ia.py.
# Implementa una personalidad, memoria y una funcionalidad nueva.

from cliente_ia import preguntar_ia
from recursos.terminal import ejecutar

# TODO: define el nombre, objetivo e instrucciones de tu asistente.
NOMBRE = "Mi proyecto"


def main():
    print(f"=== PROYECTO FINAL: {NOMBRE} ===")
    # TODO: desarrolla un asistente que resuelva el problema que has elegido.
    # Puedes copiar TU código de los retos anteriores y ampliarlo.
    raise NotImplementedError("tu propio asistente")


if __name__ == "__main__":
    raise SystemExit(ejecutar(main))
