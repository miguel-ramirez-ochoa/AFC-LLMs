# Instalación desde cero

[← Volver al README](README.md) · [Problemas frecuentes](PROBLEMAS_FRECUENTES.md)

**Objetivo:** en 15 minutos, tener Python, un entorno virtual y una primera respuesta de OpenRouter. Sigue solo los comandos de tu sistema. No escribas los símbolos del prompt de terminal ni las explicaciones que acompañan a los comandos.

## 1. Comprueba Python antes de crear el entorno

Necesitas Python 3.10 o posterior; **recomendamos Python 3.12**, que hemos probado en macOS. Si ya tienes una versión compatible (3.10, 3.11, 3.12 o posterior), no necesitas instalar otra.

- **Windows:** abre PowerShell y prueba `py --version`. Para ver las versiones disponibles, `py -0p` (si el lanzador lo admite). Si `py` no existe, prueba `python --version`.
- **macOS:** abre Terminal y prueba `python3 --version` y `python3.12 --version`. Si `python3` indica 3.9 pero `python3.12` funciona, utiliza este último. En macOS no es raro que `python` no exista fuera de un venv.
- **Linux:** abre una terminal y prueba `python3 --version`.

Si no hay ninguna versión compatible:

| Sistema | Qué hacer |
|---|---|
| Windows | Abre [Python para Windows](https://www.python.org/downloads/windows/). Instala Python 3.12 o una versión compatible; si usas un instalador clásico, marca **Add python.exe to PATH** cuando aparezca. Cierra y abre PowerShell. |
| macOS | Abre [Python para macOS](https://www.python.org/downloads/macos/) y utiliza un instalador compatible. Si ya tienes Homebrew, puedes ejecutar `brew install python@3.12`. Abre una nueva terminal. |
| Linux | Usa el gestor de paquetes de tu distribución para instalar Python 3.10+ y el módulo `venv`. En Debian/Ubuntu, si la versión de la distribución es compatible, `sudo apt install python3 python3-venv`. Si no tienes permisos, solicita ayuda. |

En los ordenadores del laboratorio no instales software sin permiso; pregunta a los ponentes si falta Python. No elimines ni sustituyas el Python del sistema. Puedes trabajar por parejas si un equipo no está preparado.

## 2. Descarga el repositorio y abre la carpeta correcta

En la página de GitHub del taller, pulsa **Code → Download ZIP** y extrae el archivo. No trabajes dentro de un ZIP. Git es opcional; si lo conoces, puedes usar `git clone` con la URL HTTPS que ofrece GitHub.

Abre la carpeta extraída con tu editor (por ejemplo, [Visual Studio Code](https://code.visualstudio.com/), si está instalado). En VS Code puedes usar **Archivo → Abrir carpeta** y **Terminal → Nueva terminal**. La terminal debe estar en la carpeta que contiene `requirements.txt`, `config.py`, `verificar_instalacion.py` y `retos/`.

Compruébalo con `ls` en macOS/Linux, o `Get-ChildItem` en PowerShell. Si aparecen otras carpetas, entra en la correcta con `cd "nombre de la carpeta"`. Las comillas son importantes si hay espacios.

## 3. Crea y activa el entorno virtual

Un entorno virtual (`.venv`) es una carpeta con su propio intérprete y librerías. Así no instalamos dependencias de forma global ni interferimos con otros proyectos. **No hay que editar archivos de `.venv` manualmente.** Créalo una sola vez por proyecto y actívalo cada vez que abras una nueva terminal.

### Windows — PowerShell

Si tienes Python 3.12:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

Si tienes otra versión compatible, usa `py -3.11` o la versión que corresponda. Si no tienes `py` pero `python --version` es compatible, puedes crear el entorno con `python -m venv .venv`.

Si PowerShell bloquea la activación, **no cambies las políticas de seguridad del laboratorio**. Puedes seguir usando todos los comandos de esta guía sustituyendo `python` por `.\.venv\Scripts\python.exe`. Alternativamente, abre CMD en la raíz y ejecuta `.venv\Scripts\activate.bat`.

### macOS

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python --version
```

Si no tienes Python 3.12 pero `python3 --version` es 3.10 o posterior, sustituye `python3.12` por `python3`. Si tienes un intérprete específico compatible distinto, usa su nombre (por ejemplo `python3.11`).

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python --version
```

Asegúrate antes de que `python3` es compatible. Si hay varias versiones, usa el ejecutable de la que quieras utilizar. Si falta `venv`, consulta [Problemas frecuentes](PROBLEMAS_FRECUENTES.md).

### Verifica el resultado

La versión mostrada debe ser 3.10 o superior. Normalmente verás `(.venv)` al inicio de la terminal. Comprueba el intérprete si tienes dudas:

```bash
python -c "import sys; print(sys.executable)"
```

Debe apuntar a `.venv` dentro de este proyecto. Si es Python 3.9 o no pertenece a `.venv`, detente y consulta la guía de errores. Activar un entorno no cambia la versión con la que se creó.

## 4. Instala las dependencias

Desde la misma terminal:

```bash
python -m pip install -r requirements.txt
```

Se instalan `requests` (conexión HTTP) y `python-dotenv` (lectura de la configuración), más sus dependencias. No instalamos modelos ni Ollama. Si aparece un aviso de nueva versión de pip, normalmente puedes ignorarlo si la instalación termina correctamente.

## 5. Configura el archivo `.env`

Copia la plantilla sin modificarla. Si ya tienes un `.env`, **no lo sobrescribas**: ábrelo directamente.

**Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
notepad .env
```

**macOS/Linux:**

```bash
cp .env.example .env
nano .env
```

También puedes usar tu editor habitual. En `nano` guarda con Ctrl+O, Enter y sal con Ctrl+X. En Windows comprueba que el nombre no termine en `.txt`.

Abre el enlace privado facilitado por los ponentes **en el navegador del ordenador**. Si pide contraseña, utiliza la que se comunique en el laboratorio. Copia el contenido de configuración en `.env`, sin compartirlo con otras personas. La clave real nunca se incluye en GitHub ni en esta guía. La estructura es:

```dotenv
OPENROUTER_API_KEY=
OPENROUTER_MODEL=meta-llama/llama-3.3-70b-instruct
CHARLA_MODO=real
```

La primera línea debe contener la clave temporal real después del `=`. No cambies el modelo. Guarda el archivo. Si recibes el bloque de configuración completo, reemplaza el contenido de `.env` (evita duplicar las variables).

**Seguridad:** `.gitignore` excluye `.env`, pero aun así no lo subas a GitHub, no lo envíes por chat y no lo proyectes. La clave tiene un límite compartido y una caducidad; no la utilices fuera de la actividad.

## 6. Comprueba la instalación y la API

```bash
python verificar_instalacion.py
python verificar_instalacion.py --api
```

La primera orden verifica Python, librerías y configuración sin consumir créditos. La segunda realiza una petición a OpenRouter (consume una pequeña cantidad de saldo). Espera un resultado parecido a:

```text
Python 3.12.x | Modelo: meta-llama/llama-3.3-70b-instruct | Modo: real
Clave presente (no mostrada). Aún no se ha validado con el proveedor.
OK
Prueba de petición completada.
```

Si hay un error, consulta [Problemas frecuentes](PROBLEMAS_FRECUENTES.md). No repitas peticiones en bucle. No necesitas ejecutar las pruebas automáticas de infraestructura para empezar, pero puedes hacerlo sin gastar saldo:

```bash
python -m unittest discover -s tests -v
```

## 7. Empieza a programar

Abre el [README del reto 1](retos/reto01/README.md) y ejecuta desde la raíz:

```bash
python -m retos.reto01.reto
```

El mensaje «Pendiente» es **intencionado**: debes completar los TODO del ejercicio. No es un problema con la API. Usa los enunciados y las pistas en GitHub, o los README descargados si no tienes acceso a la web.

Al terminar, puedes salir del entorno con `deactivate` (si lo activaste). No borres `.venv` para pasar al siguiente reto. Vuelve al [README](README.md) para ver el recorrido completo.
