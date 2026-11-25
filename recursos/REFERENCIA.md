# Referencia rápida (sin soluciones)

## Contrato del cliente

`preguntar_ia(mensajes)` recibe una lista de diccionarios con las claves `role` y `content`. Devuelve una cadena de texto. No guarda memoria ni modifica la lista. Cada llamada tiene su propio contexto. Puede lanzar `ValueError` si la entrada o configuración no es válida y `RuntimeError` si falla el servicio.

Roles: `system` describe el comportamiento; `user` contiene lo que pide el usuario; `assistant` representa una respuesta anterior. No confundas el rol con el nombre de la variable. El modelo puede incumplir instrucciones: comprueba su respuesta.

## Herramientas de Python para investigar

- [Listas y métodos](https://docs.python.org/es/3/tutorial/datastructures.html)
- [Lectura y escritura de archivos](https://docs.python.org/es/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Funciones y control de flujo](https://docs.python.org/es/3/tutorial/controlflow.html)
- [OpenRouter: primera petición](https://learn.openrouter.ai/courses/first-request/make-a-request)
- [OpenRouter: modelo del taller](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct)

Puedes utilizar buscadores, documentación o asistentes de IA. No les envíes tu `.env`, credenciales o información personal. Comprueba que entiendes cada línea antes de utilizarla.

## Errores frecuentes

Consulta también [Problemas frecuentes](../PROBLEMAS_FRECUENTES.md) y [la instalación](../INSTALACION.md).

| Error | Acción |
|---|---|
| No module named ... | Activa el entorno e instala requirements.txt; ejecuta desde la raíz con `python -m retos.reto01.reto`. |
| Pendiente / NotImplementedError | Es parte de un reto; completa el TODO correspondiente. |
| HTTP 401 | Pide al ponente comprobar la clave, sin mostrarla. |
| HTTP 402 | Saldo o límite de la clave; avisa al ponente. |
| HTTP 404 | Consulta al ponente por el modelo configurado. |
| HTTP 429 | No repitas peticiones en bucle; espera o consulta al ponente. |
| Sin conexión | Usa el modo simulado según el README. |

El modo simulado verifica el flujo y el número de mensajes, pero no demuestra personalidad, memoria semántica ni conocimiento real. Para eso hace falta una llamada a un modelo real.
