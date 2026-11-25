# Reto 03 · El problema de la memoria

**15 minutos.** Ejecuta primero el programa tal como está. El defecto es intencionado: el chatbot no recuerda las interacciones previas. Arréglalo.


## Misión y criterios de éxito

- [ ] Reutilizar las instrucciones de personalidad que diseñaste en el reto 2 y conservarlas durante la conversación.
- [ ] Almacenar cada pregunta y respuesta.
- [ ] Enviar los mensajes previos junto con la pregunta actual.
- [ ] Guardar roles `user` y `assistant` en orden.
- [ ] Conservar el comando `/salir` y demostrar que recuerda un nombre ficticio.

## Diagnóstico antes de programar

Ejecuta dos turnos: «Me llamo Alba» y «¿Cómo me llamo?». ¿Qué información recibe el modelo en el segundo turno? Puedes inspeccionar los argumentos de la llamada con un `print` temporal. Retíralo al terminar. Explica por qué esto no es reentrenar el modelo.

## Resultado de ejemplo

```text
Tú: Me llamo Alba.
IA: ¡Hola, Alba!
Tú: ¿Cómo me llamo?
IA: Te llamas Alba.
```

Ejemplo orientativo: la respuesta exacta de un LLM puede variar.

## Ejecuta y comprueba

Desde la raíz del proyecto:

```bash
python -m retos.reto03.reto
python -m unittest tests.comprobar_retos.Reto3 -v
```

Antes de cambiar código, observa qué ocurre al ejecutar la plantilla. Completa los TODO, prueba de nuevo y comprueba los criterios de éxito. Las pruebas automáticas (cuando existen) no consumen tokens y verifican la estructura del programa; la calidad de las respuestas se comprueba manualmente con la API real.

## Pistas (abre solo las necesarias, de una en una)

<details>
<summary>Pista 1</summary>

¿Qué estructura de datos ordenada puede crecer durante el bucle?

</details>

<details>
<summary>Pista 2</summary>

Investiga `list.append()`. Los mensajes anteriores usan los mismos roles que en el reto 2.

</details>

<details>
<summary>Pista 3</summary>

Antes de consultar la IA necesitas la pregunta actual y las anteriores; al terminar, conserva también su respuesta. Si falla la consulta, evita guardar una interacción incompleta.

</details>

## Ampliaciones opcionales

Si te sobra tiempo, implementa `/reset`, `/historial` o una ventana de cinco interacciones sin perder `system`. Comprueba que una consulta fallida no deja un turno incompleto.

[Volver al taller](../../README.md)
