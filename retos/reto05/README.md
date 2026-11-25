# Reto 05 · Proyecto final: tu propio asistente

**15 minutos.** Crea tu propio asistente. Reutiliza tu código anterior y añade una funcionalidad que vaya más allá de cambiar el prompt.


## Misión y criterios de éxito

- [ ] Nombre, objetivo e instrucciones propias.
- [ ] Conversación de varios turnos y forma de salir.
- [ ] Al menos una funcionalidad de Python programada por ti (puntuación, comandos, inventario, selección de documentos, etc.).
- [ ] Demuestra cómo funciona y explica una decisión de implementación.

## Define tu proyecto

Antes de programar, decide en pareja o individualmente: ¿a quién ayuda?, ¿qué problema resuelve?, ¿qué función adicional controlará Python? Elige una idea pequeña y reutiliza tu propio código.

Ideas: Code Coach (comando de pistas), Study Buddy (contador de repasos), QuizGPT (puntuación), Dungeon Master (inventario) o asistente de documentos. Si te falta tiempo, consolida los retos 1–3 primero.

## Resultado de ejemplo

```text
Tú: /ayuda
Asistente: Comandos disponibles...
Tú: Hazme una pregunta de repaso.
Asistente: ¿Qué hace una API?
```

Ejemplo orientativo: la respuesta exacta de un LLM puede variar.

## Ejecuta y comprueba

Desde la raíz del proyecto:

```bash
python -m retos.reto05.reto
# Evaluación manual: no hay una única solución.
```

Antes de cambiar código, observa qué ocurre al ejecutar la plantilla. Completa los TODO, prueba de nuevo y comprueba los criterios de éxito. Las pruebas automáticas (cuando existen) no consumen tokens y verifican la estructura del programa; la calidad de las respuestas se comprueba manualmente con la API real.

## Pistas (abre solo las necesarias, de una en una)

<details>
<summary>Pista 1</summary>

Elige una idea pequeña con un comportamiento que puedas mostrar en 60 segundos.

</details>

<details>
<summary>Pista 2</summary>

Reutiliza tus funciones de los retos 2, 3 y/o 4.

</details>

<details>
<summary>Pista 3</summary>

Separa el estado que gestiona Python de lo que genera el modelo.

</details>

## Demo de 60 segundos

Enseña una pregunta normal, una de seguimiento que requiera memoria y tu función adicional. Explica qué hace Python y qué hace el modelo. En modo simulado, enseña el flujo de mensajes y la lógica de Python sin afirmar que hay un LLM real.

## Ampliaciones opcionales

Añade una segunda funcionalidad, usa el documento del reto 4, valida entradas o escribe pruebas propias. No hace falta hacerlo todo.

[Volver al taller](../../README.md)
