# Comprueba requisitos de programación de los retos 1 a 4.
# Importa los módulos de retos y simula las respuestas de cliente_ia.py.
# Los fallos iniciales son esperados: completa los TODO hasta superarlos.

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from retos.reto01 import reto as r1
from retos.reto02 import reto as r2
from retos.reto03 import reto as r3
from retos.reto04 import reto as r4


class Reto1(unittest.TestCase):
    def test_mensaje(self):
        self.assertEqual(r1.construir_mensajes("Hola"), [{"role": "user", "content": "Hola"}])

    def test_responder(self):
        with patch.object(r1, "preguntar_ia", return_value="respuesta") as consulta:
            self.assertEqual(r1.responder("Hola"), "respuesta")
            consulta.assert_called_once_with([{"role": "user", "content": "Hola"}])


class Reto2(unittest.TestCase):
    def test_roles(self):
        mensajes = r2.construir_mensajes("Hola", "Sé breve")
        self.assertEqual(mensajes[0], {"role": "system", "content": "Sé breve"})
        self.assertEqual(mensajes[1], {"role": "user", "content": "Hola"})
        self.assertEqual(len(mensajes), 2)

    def test_personalizacion(self):
        self.assertTrue(r2.INSTRUCCIONES.strip(), "Escribe tus propias instrucciones")
        self.assertNotEqual(r2.NOMBRE, "Mi asistente")

    def test_responder(self):
        with patch.object(r2, "preguntar_ia", return_value="respuesta") as consulta:
            self.assertEqual(r2.responder("Hola", "Sé breve"), "respuesta")
            consulta.assert_called_once_with(r2.construir_mensajes("Hola", "Sé breve"))


class Reto3(unittest.TestCase):
    def test_conserva_y_envia_historial(self):
        historial = r3.iniciar_historial()
        inicial = historial[0].copy()
        enviados = []

        # Copiamos los mensajes en el instante de la petición.
        def falso(mensajes):
            enviados.append([m.copy() for m in mensajes])
            return "Respuesta simulada"

        with patch.object(r3, "preguntar_ia", side_effect=falso):
            r3.responder(historial, "Me llamo Alba")
            r3.responder(historial, "¿Cómo me llamo?")
        self.assertEqual(historial[0], inicial)
        self.assertEqual([m["role"] for m in historial], ["system", "user", "assistant", "user", "assistant"])
        self.assertEqual(enviados[1][1]["content"], "Me llamo Alba")
        self.assertEqual(enviados[1][-1]["content"], "¿Cómo me llamo?")
        self.assertEqual(enviados[1], historial[:-1])


class Reto4(unittest.TestCase):
    def test_lectura(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "contexto.txt"
            ruta.write_text("Nombre en clave: NeuralBridge", encoding="utf-8")
            self.assertEqual(r4.leer_conocimiento(ruta).strip(), "Nombre en clave: NeuralBridge")

    def test_contexto(self):
        mensajes = r4.construir_mensajes("¿Nombre en clave?", "Nombre en clave: NeuralBridge")
        self.assertTrue(any("NeuralBridge" in m["content"] for m in mensajes))
        self.assertTrue(any(m["role"] == "user" and "¿Nombre en clave?" in m["content"] for m in mensajes))

    def test_responder(self):
        with patch.object(r4, "preguntar_ia", return_value="NeuralBridge") as consulta:
            self.assertEqual(r4.responder("¿Nombre en clave?", "Nombre en clave: NeuralBridge"), "NeuralBridge")
            consulta.assert_called_once()
            mensajes = consulta.call_args.args[0]
            self.assertTrue(any("NeuralBridge" in m["content"] for m in mensajes))


if __name__ == "__main__":
    unittest.main()
