# Taller Interactivo de Git y GitHub

Bienvenido al Taller Interactivo de Git y GitHub, diseñado para ayudarte a aprender y dominar el uso de Git y GitHub de manera práctica y efectiva. Este proyecto utiliza Streamlit para proporcionar una interfaz sencilla y una experiencia de aprendizaje interactiva.

## Tabla de Contenidos

- [Introducción](#introducción)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Características](#características)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Introducción

Este taller está estructurado en varias secciones que cubren desde los conceptos básicos hasta el uso avanzado de Git y la integración con GitHub. Cada sección incluye explicaciones teóricas, ejemplos prácticos y ejercicios interactivos para consolidar tus conocimientos.

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

1. **Clona el repositorio**:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. **Crea y activa un entorno virtual** (opcional pero recomendado):

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecuta la aplicación**:

    ```bash
    streamlit run app.py
    ```

## Estructura del Proyecto

- `app.py`: Archivo principal que ejecuta la aplicación Streamlit.
- `pages/`: Directorio que contiene las diferentes secciones del taller.
- `requirements.txt`: Archivo con las dependencias necesarias para el proyecto.
- `README.md`: Este archivo.

La navegación del taller se realiza mediante un diccionario de páginas:

```python
# Diccionario para la navegación
paginas = {
    "Home": pagina_principal,
    "Comandos Básicos Terminal": comandos_basicos_terminal,
    "Configuración e Inicialización": configuracion_e_inicializacion_git,
    "Operaciones Básicas": operaciones_basicas,
    "Ramas y Colaboración": ramas_colaboracion,
    "Uso Avanzado de Git": avanzado_git,
    "Integración con GitHub": integracion_github,
    "Resumen Taller": resumen_taller,
    "Ejercicios": ejercicios,
    "Feedback": feedback
}
