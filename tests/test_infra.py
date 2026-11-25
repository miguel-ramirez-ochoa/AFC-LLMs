# Prueba el cliente, los errores y el modo simulado sin acceder a Internet.
# Usa unittest y mocks para sustituir requests.post y la configuración.
# Estas pruebas deben pasar antes de comenzar los retos.

import unittest
from unittest.mock import patch, Mock
import requests
import cliente_ia
import config

MENSAJES = [{"role": "user", "content": "Hola"}]


class Infraestructura(unittest.TestCase):
    def test_mensajes_invalidos(self):
        with patch("cliente_ia.requests.post") as post:
            for mensajes in ([], [{"role": "otro", "content": "x"}], [{"role": "user", "content": ""}]):
                with self.assertRaises(ValueError):
                    cliente_ia.preguntar_ia(mensajes)
            post.assert_not_called()

    def test_simulacion_sin_red(self):
        with patch.object(config, "MODO", "simulado"), patch("cliente_ia.requests.post") as post:
            texto = cliente_ia.preguntar_ia(MENSAJES)
            self.assertIn("1 user", texto)
            self.assertIn("SIMULACIÓN", texto)
            post.assert_not_called()

    def test_peticion_y_respuesta(self):
        resultado = Mock(status_code=200)
        resultado.json.return_value = {"choices": [{"message": {"content": "  Hola  "}}]}
        with patch.object(config, "MODO", "real"), patch.object(config, "MODELO", "modelo-prueba"), patch.object(config, "obtener_api_key", return_value="clave-ficticia"), patch("cliente_ia.requests.post", return_value=resultado) as post:
            self.assertEqual(cliente_ia.preguntar_ia(MENSAJES), "Hola")
            self.assertEqual(post.call_args.kwargs["json"]["messages"], MENSAJES)
            self.assertEqual(post.call_args.kwargs["json"]["model"], "modelo-prueba")
            self.assertEqual(post.call_args.args[0], config.OPENROUTER_URL)

    def test_errores_http(self):
        with patch.object(config, "MODO", "real"), patch.object(config, "MODELO", "modelo-prueba"), patch.object(config, "obtener_api_key", return_value="clave-ficticia"), patch("cliente_ia.requests.post") as post:
            for codigo in (401, 402, 404, 429, 503):
                post.return_value = Mock(status_code=codigo)
                with self.assertRaisesRegex(RuntimeError, str(codigo)):
                    cliente_ia.preguntar_ia(MENSAJES)

    def test_timeout(self):
        with patch.object(config, "MODO", "real"), patch.object(config, "MODELO", "modelo-prueba"), patch.object(config, "obtener_api_key", return_value="clave-ficticia"), patch("cliente_ia.requests.post", side_effect=requests.Timeout):
            with self.assertRaisesRegex(RuntimeError, "demasiado"):
                cliente_ia.preguntar_ia(MENSAJES)

    def test_respuesta_invalida(self):
        resultado = Mock(status_code=200)
        resultado.json.return_value = {"choices": []}
        with patch.object(config, "MODO", "real"), patch.object(config, "MODELO", "modelo-prueba"), patch.object(config, "obtener_api_key", return_value="clave-ficticia"), patch("cliente_ia.requests.post", return_value=resultado):
            with self.assertRaisesRegex(RuntimeError, "sin texto"):
                cliente_ia.preguntar_ia(MENSAJES)


if __name__ == "__main__":
    unittest.main()
