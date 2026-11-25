# Reto 01 · Establece contacto

**10 minutos.** Haz que Python envíe tu primera pregunta a un LLM. Investiga el contrato del cliente; no necesitas modificarlo.


## Misión y criterios de éxito

- [ ] Enviar la pregunta en el formato que acepta el cliente.
- [ ] Usar `preguntar_ia()` y devolver su respuesta.
- [ ] Mostrar la respuesta por terminal.

## Antes de programar

Localiza `preguntar_ia` en `cliente_ia.py`. ¿Qué recibe y qué devuelve? Busca cómo representar una pregunta en Python. No modifiques el cliente.

## Resultado de ejemplo

```text
Tú: ¿Qué es una variable?
IA: Una variable es un nombre que representa un valor.
```

Ejemplo orientativo: la respuesta exacta de un LLM puede variar.

## Ejecuta y comprueba

Desde la raíz del proyecto:

```bash
python -m retos.reto01.reto
python -m unittest tests.comprobar_retos.Reto1 -v
```

Antes de cambiar código, observa qué ocurre al ejecutar la plantilla. Completa los TODO, prueba de nuevo y comprueba los criterios de éxito. Las pruebas automáticas (cuando existen) no consumen tokens y verifican la estructura del programa; la calidad de las respuestas se comprueba manualmente con la API real.

## Pistas (abre solo las necesarias, de una en una)

<details>
<summary>Pista 1</summary>

Lee `recursos/REFERENCIA.md` y el docstring de `preguntar_ia`. ¿Qué recibe y devuelve?

</details>

<details>
<summary>Pista 2</summary>

Busca cómo crear una lista de diccionarios en Python.

</details>

<details>
<summary>Pista 3</summary>

Consulta la firma de `preguntar_ia` y prueba cada función por separado: preparar la entrada, obtener la respuesta y mostrarla.

</details>

## Ampliaciones opcionales

Prueba dos preguntas diferentes y explica qué cambia en la entrada. Si el ponente lo autoriza, compara dos modelos permitidos y restaura el inicial.

[Volver al taller](../../README.md)
