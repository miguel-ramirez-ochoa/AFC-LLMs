# Reto 04 · Enséñale algo nuevo

**10 minutos.** Queremos construir un asistente que responda sobre la documentación técnica de PyLLM, un proyecto ficticio de Python y LLMs. El modelo puede conocer Python, pero no tiene por qué conocer los detalles internos de este proyecto. Dale acceso a esa información sin entrenarlo de nuevo. Esto es incorporación directa de contexto, no un sistema RAG completo.


## Misión y criterios de éxito

- [ ] Leer `datos/contexto.txt` en UTF-8.
- [ ] Incluir el contenido del documento en los mensajes enviados a la IA.
- [ ] Pedir que responda a partir del documento y reconozca la información ausente.
- [ ] Comprobar la versión, el nombre en clave y una pregunta cuya respuesta no aparezca en el documento.

## Antes de programar

Abre `datos/contexto.txt`. Pregunta por el nombre en clave de la versión de PyLLM en un chatbot que no recibe el documento. ¿Por qué no podemos garantizar que sepa la respuesta? Después incorpora el documento y compara. No uses apuntes privados ni datos personales.

## Resultado de ejemplo

```text
Tú: ¿Cuál es la versión actual de PyLLM?
IA: Según la documentación, la versión actual es la 2.4.1.

Tú: ¿Cuál es el nombre en clave de esta versión?
IA: NeuralBridge.

Tú: ¿Cuál es el precio de la suscripción?
IA: No consta en el documento.
```

Ejemplo orientativo: la respuesta exacta de un LLM puede variar. Ejecuta nuevamente el programa para cada pregunta. Los datos de PyLLM son ficticios y no describen la configuración real del taller.

## Ejecuta y comprueba

Desde la raíz del proyecto:

```bash
python -m retos.reto04.reto
python -m unittest tests.comprobar_retos.Reto4 -v
```

Antes de cambiar código, observa qué ocurre al ejecutar la plantilla. Completa los TODO, prueba de nuevo y comprueba los criterios de éxito. Las pruebas automáticas (cuando existen) no consumen tokens y verifican la estructura del programa; la calidad de las respuestas se comprueba manualmente con la API real.

## Pistas (abre solo las necesarias, de una en una)

<details>
<summary>Pista 1</summary>

Busca cómo abrir y leer un archivo de texto usando `pathlib` o `with open(...)`.

</details>

<details>
<summary>Pista 2</summary>

El modelo no puede leer tu disco por sí solo. ¿Cómo le enviarías el texto junto con las instrucciones?

</details>

<details>
<summary>Pista 3</summary>

Distingue el documento de la pregunta y especifica que no debe inventar datos. Comprueba los casos sin respuesta.

</details>

## Ampliaciones opcionales

Permite escoger entre dos documentos ficticios y vuelve a cargar el contexto al cambiar. Puedes crear un segundo archivo de datos inventados. Evita rutas arbitrarias o datos personales.

[Volver al taller](../../README.md)
