# Reto 4: permite responder preguntas sobre un documento del taller.
# Lee datos/contexto.txt y utiliza cliente_ia.py.
# Completa los TODO para aportar información externa en cada petición.

from pathlib import Path
from cliente_ia import preguntar_ia
from config import RAIZ
from recursos.terminal import ejecutar

ARCHIVO = RAIZ / "datos" / "contexto.txt"


def leer_conocimiento(ruta):
    # TODO: consigue que Python pueda utilizar la información del documento.
    raise NotImplementedError("leer_conocimiento")


def construir_mensajes(pregunta, conocimiento):
    # TODO: prepara una consulta que se apoye en la información disponible.
    raise NotImplementedError("construir_mensajes")


def responder(pregunta, conocimiento):
    # TODO: obtén la respuesta del asistente documental.
    raise NotImplementedError("responder")


def main():
    print("=== RETO 4: ENSÉÑALE ALGO NUEVO ===")
    conocimiento = leer_conocimiento(ARCHIVO)
    pregunta = input("Tú: ").strip()
    if pregunta:
        print("IA:", responder(pregunta, conocimiento))


if __name__ == "__main__":
    raise SystemExit(ejecutar(main))
