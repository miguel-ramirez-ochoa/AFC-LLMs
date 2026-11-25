# Construye tu propio ChatGPT

**Escuela Politécnica Superior · UFV | Ada Byron · Taller de LLMs con Python y OpenRouter**

**25 de noviembre de 2026 · 12:00–14:00 · Laboratorio de Informática · Actividad AFC (0,1 ECTS).**

Tu misión es construir un asistente desde la terminal. No necesitas conocimientos previos de IA: puedes trabajar en pareja y consultar documentación. Te proporcionamos una conexión funcional con la IA, cinco retos y pistas progresivas. Tú debes completar el código marcado con `TODO`. No instalarás Ollama ni descargarás modelos.

## 1. Empieza aquí: prepara tu ordenador (15 minutos)

**No necesitas instalar Ollama, descargar modelos, crear una cuenta de OpenRouter ni comprar créditos.** El taller utiliza Llama 3.3 70B Instruct a través de OpenRouter. Los ponentes facilitarán una clave temporal y limitada mediante un canal privado.

1. Abre [la guía de instalación](INSTALACION.md) y sigue las instrucciones de tu sistema operativo (Windows, macOS o Linux). Recomendamos Python 3.12; mínimo 3.10.
2. Descarga este repositorio con **Code → Download ZIP** (Git es opcional), descomprímelo y abre la carpeta que contiene `requirements.txt` en un editor y en una terminal.
3. Crea y activa `.venv`, instala las dependencias y configura `.env` según la guía. El enlace privado se entregará durante el taller: ábrelo en el navegador del ordenador, no en el móvil.
4. Comprueba que puedes ejecutar estos comandos desde la raíz:

```bash
python --version
python verificar_instalacion.py
python verificar_instalacion.py --api
```

Si la comprobación real termina con «Prueba de petición completada», ya puedes comenzar el reto 1. Una respuesta de texto a esa prueba es suficiente, aunque el modelo no escriba exactamente `OK`.

**¿Algo no funciona?** Consulta [Problemas frecuentes](PROBLEMAS_FRECUENTES.md) antes de reinstalar o repetir peticiones. Si no puedes activar el entorno, la guía ofrece comandos con el ejecutable del venv directamente.

No publiques tu `.env`, no lo pegues en un asistente de IA y no compartas el enlace privado. El repositorio solo contiene `.env.example`, sin clave. El modelo se mantiene fijo durante el taller salvo indicación de los ponentes.

## 2. Tu misión

| Horario | Actividad | Comando (desde la raíz) |
|---|---|---|
| 12:00–12:30 | Presentación y demostración | — |
| 12:30–12:45 | Preparación del entorno | `python verificar_instalacion.py` |
| 12:45–12:55 | [01 · Establece contacto](retos/reto01/README.md) | `python -m retos.reto01.reto` |
| 12:55–13:05 | [02 · Crea una personalidad](retos/reto02/README.md) | `python -m retos.reto02.reto` |
| 13:05–13:20 | [03 · El problema de la memoria](retos/reto03/README.md) | `python -m retos.reto03.reto` |
| 13:20–13:30 | [04 · Enséñale algo nuevo](retos/reto04/README.md) | `python -m retos.reto04.reto` |
| 13:30–13:45 | [05 · Proyecto final: tu propio asistente](retos/reto05/README.md) | `python -m retos.reto05.reto` |
| 13:45–13:55 | Margen, ayuda y ampliaciones | — |
| 13:55–14:00 | Demos y cierre | — |

### Elige tu nivel de avance

- **Objetivo mínimo:** retos 1–3. Un chatbot con personalidad y memoria desde terminal. Puedes trasladar tus instrucciones del reto 2 al reto 3.
- **Objetivo completo:** retos 4 y 5. Incorpora información externa y crea un asistente para un caso propio.
- **Ampliaciones:** comandos, memoria limitada, documentos alternativos, validación o funcionalidades adicionales.

No es un examen ni una carrera. La prioridad es comprender lo que programas; no es obligatorio terminar los extras. Si necesitas más tiempo, consolida los tres primeros retos y pide ayuda. Cualquier puntuación que propongan los ponentes será voluntaria; consulta los requisitos oficiales de reconocimiento AFC con la organización.

En cada reto: lee la misión, ejecuta la plantilla, observa qué falta o falla, investiga, modifica tu código, comprueba el resultado y explica cómo lo conseguiste. Los TODO indican el objetivo, no la solución. Abre las pistas de una en una. En las comprobaciones de retos 1–4, los fallos iniciales son intencionados; no significan que la instalación esté rota. Reto 5 se evalúa con una demostración. Mantén los nombres de las funciones para que las comprobaciones funcionen.

## 3. Mapa del repositorio

```text
CHARLA_LLMS/
├── .env.example              # Plantilla sin clave
├── .gitignore                # Excluye .env y .venv
├── config.py                # Configuración
├── cliente_ia.py            # Conexión a OpenRouter
├── verificar_instalacion.py # Comprobación de entorno
├── requirements.txt
├── README.md
├── INSTALACION.md           # Windows, macOS y Linux
├── PROBLEMAS_FRECUENTES.md  # Diagnóstico y soluciones
├── retos/                   # 5 carpetas con README y reto.py
├── datos/                   # Documentación técnica ficticia
│   └── contexto.txt         # PyLLM: datos del reto 4
├── recursos/                # Referencia y herramientas
└── tests/                   # Infraestructura y comprobaciones de retos
```

No necesitas modificar el cliente ni la configuración para resolver los ejercicios básicos. Consulta [la referencia rápida](recursos/REFERENCIA.md). El `.env` se crea localmente y no se publica.

## 4. Si se cae Internet o la API

En `.env` cambia `CHARLA_MODO=real` por `CHARLA_MODO=simulado`. Los retos pueden probar el flujo de mensajes sin clave y sin consumir créditos. No es una IA: la respuesta solo indica los roles recibidos. Para demostrar comportamiento real, vuelve a `real` cuando la API funcione. Las dependencias deben estar instaladas previamente.

## 5. Normas y cómo pedir ayuda

Puedes usar documentación, búsquedas, IA y ayuda de tus compañeros. Si te bloqueas, intenta explicar el problema, consulta una referencia y abre una pista antes de pedir la solución. En los retos 1–4, comprueba la estructura con los tests y luego el comportamiento con una consulta real, si hay conexión. Debes poder explicar tu código. No introduzcas datos personales ni claves en el chatbot. Limita las peticiones y no repitas automáticamente si la API falla. El documento `datos/contexto.txt` del reto 4 contiene documentación técnica de PyLLM, un proyecto ficticio. No describe la configuración real del taller.
