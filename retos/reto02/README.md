# Reto 02 · Crea una personalidad

**10 minutos.** Convierte un modelo genérico en un tutor, entrenador o personaje con instrucciones concretas.


## Misión y criterios de éxito

- [ ] Asignar un nombre propio e instrucciones no vacías.
- [ ] Separar las instrucciones del asistente de la petición del usuario en los mensajes.
- [ ] Definir objetivo, público, restricción y formato en las instrucciones.
- [ ] Demostrar con dos preguntas que el asistente intenta respetarlas.

## Antes de programar

Elige un caso de uso (tutor, entrenador, personaje). ¿Qué debería hacer siempre y qué debería evitar? Compara la misma pregunta con el reto 1 y con tu asistente. Reutiliza la lógica que ya escribiste.

## Resultado de ejemplo

```text
Tú: Explícame un bucle.
Tutor: Imagina que tienes que repartir cartas una por una...
```

Ejemplo orientativo: la respuesta exacta de un LLM puede variar.

## Ejecuta y comprueba

Desde la raíz del proyecto:

```bash
python -m retos.reto02.reto
python -m unittest tests.comprobar_retos.Reto2 -v
```

Antes de cambiar código, observa qué ocurre al ejecutar la plantilla. Completa los TODO, prueba de nuevo y comprueba los criterios de éxito. Las pruebas automáticas (cuando existen) no consumen tokens y verifican la estructura del programa; la calidad de las respuestas se comprueba manualmente con la API real.

## Pistas (abre solo las necesarias, de una en una)

<details>
<summary>Pista 1</summary>

Investiga la diferencia entre los roles `system` y `user`.

</details>

<details>
<summary>Pista 2</summary>

Consulta los roles y el formato de mensajes en la referencia. Piensa qué información debe permanecer fija entre distintas preguntas.

</details>

<details>
<summary>Pista 3</summary>

Escribe tus propias instrucciones con objetivo, público, restricción y formato. Prueba una petición normal y otra que contradiga una de las restricciones.

</details>

## Ampliaciones opcionales

Intenta hacer que tu asistente incumpla sus instrucciones con una pregunta inocua. Mejora el prompt y explica por qué no garantiza el cumplimiento.

[Volver al taller](../../README.md)
