# Reto 1: envía una pregunta a un modelo desde la terminal.
# Utiliza preguntar_ia() de cliente_ia.py para obtener texto.
# Completa los TODO siguiendo el README de este reto.

from cliente_ia import preguntar_ia
from recursos.terminal import ejecutar


def construir_mensajes(pregunta):
    # TODO: prepara una entrada que el cliente de IA pueda interpretar.
    raise NotImplementedError("construir_mensajes")


def responder(pregunta):
    # TODO: consigue que esta función devuelva una respuesta del modelo.
    raise NotImplementedError("responder")


def main():
    print("=== RETO 1: ESTABLECE CONTACTO ===")
    pregunta = input("Tú: ").strip()
    if not pregunta:
        print("Escribe una pregunta no vacía.")
        return
    # TODO: haz visible la respuesta al usuario.
    raise NotImplementedError("mostrar la respuesta")


if __name__ == "__main__":
    raise SystemExit(ejecutar(main))
