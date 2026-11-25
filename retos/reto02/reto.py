# Reto 2: transforma el modelo en un asistente especializado.
# Conecta sus instrucciones con los mensajes de cliente_ia.py.
# Completa los TODO y diseña una personalidad propia.

from cliente_ia import preguntar_ia
from recursos.terminal import ejecutar

# TODO: diseña un asistente con identidad y comportamiento propios.
NOMBRE = "Mi asistente"
INSTRUCCIONES = ""


def construir_mensajes(pregunta, instrucciones):
    # TODO: haz que la IA reciba tanto su misión como la pregunta.
    raise NotImplementedError("construir_mensajes")


def responder(pregunta, instrucciones):
    # TODO: conecta la personalidad con la respuesta del modelo.
    raise NotImplementedError("responder")


def main():
    print(f"=== RETO 2: {NOMBRE} ===")
    pregunta = input("Tú: ").strip()
    if pregunta:
        print(f"{NOMBRE}: {responder(pregunta, INSTRUCCIONES)}")


if __name__ == "__main__":
    raise SystemExit(ejecutar(main))
