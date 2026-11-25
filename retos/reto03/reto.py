# Reto 3: repara un chatbot que pierde el contexto de la conversación.
# Conecta los mensajes guardados por Python con cliente_ia.py.
# El programa de partida funciona, pero no conserva las interacciones.

from cliente_ia import preguntar_ia
from recursos.terminal import ejecutar

INSTRUCCIONES = "Eres un asistente amable y breve."


def iniciar_historial():
    # Conservamos las instrucciones iniciales de la conversación.
    return [{"role": "system", "content": INSTRUCCIONES}]


def responder(historial, pregunta):
    # TODO: repara la pérdida de memoria entre turnos.
    # Comportamiento inicial: no recuerda la conversación anterior.
    return preguntar_ia([historial[0], {"role": "user", "content": pregunta}])


def main():
    print("=== RETO 3: EL PROBLEMA DE LA MEMORIA ===")
    historial = iniciar_historial()
    while True:
        pregunta = input("Tú (/salir): ").strip()
        if pregunta.lower() == "/salir":
            break
        if not pregunta:
            continue
        # TODO opcional: permite consultar o reiniciar la memoria sin llamar al modelo.
        try:
            print("IA:", responder(historial, pregunta))
        except RuntimeError as error:
            print("Error:", error)


if __name__ == "__main__":
    raise SystemExit(ejecutar(main))
