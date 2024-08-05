import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="Taller Git&GitHub", page_icon=":octopus:", layout="wide")

# Inicio de git, opciones y menus
st.markdown("<h1 style='text-align: center;'>Taller Completo de Git & GitHub</h1>", unsafe_allow_html=True)

# Función para verificar las respuestas
def verificar_respuesta(respuesta, correcta):
    if respuesta.strip() == correcta:
        st.success("¡Correcto!")
    else:
        st.error(f"Incorrecto. La respuesta correcta es `{correcta}`.")

def pagina_principal():
    # Crear columnas para centrar la imagen
    left_co, cent_co, right_co = st.columns(3)
    
    with cent_co:
        st.image("./img/git.png", caption="Control de versiones con Git & GitHub")
    
    # Título principal con un estilo más llamativo
    st.markdown("# **Bienvenido al Taller Completo de Git & GitHub** :computer:")
    
    # Subtítulos y texto con emojis para hacerlo más atractivo
    st.markdown("""
        ### 🚀 ¿Qué aprenderás?
        - **Comandos Básicos de Terminal**: Conocerás los comandos necesarios antes de empezar a usar Git.
        - **Configuración e Inicialización**: Cómo configurar e inicializar Git en tu sistema.
        - **Operaciones Básicas**: Clonar repositorios, añadir y eliminar archivos, hacer commits y ver el historial.
        - **Ramas y Colaboración**: Crear y gestionar ramas, realizar merges y resolver conflictos, estrategias de colaboración.
        - **Uso Avanzado de Git**: Técnicas avanzadas como rebase, stash, y cherry-pick para mejorar tu flujo de trabajo.
        - **Integración con GitHub**: Conectar repositorios locales con GitHub, realizar push y pull requests, colaborar eficazmente.
        - **Resumen del Taller**: Recapitulación de los conceptos aprendidos.
        - **Ejercicios Prácticos**: Aplicar tus conocimientos en ejercicios interactivos.
        - **Feedback**: Dar tu opinión para ayudar a mejorar continuamente.

        ¡Esperamos que disfrutes del taller y que te conviertas en un experto en Git y GitHub!
    """)

    # Añadir un botón para empezar el taller
    if st.button("¡Empecemos el taller!"):
        st.balloons()
        st.markdown("### ¡Vamos allá! Selecciona una sección del menú para comenzar.")


def comandos_basicos_terminal():
    st.title("Comandos Básicos de Terminal")
    st.markdown("""
    En esta sección, aprenderás algunos de los comandos más utilizados en la terminal para navegar y gestionar archivos y directorios en tu sistema operativo.

    ### Contenido
    1. 📁 **Navegación y Listado de Archivos**
    2. 📂 **Gestión de Directorios**
    3. 🗃️ **Gestión de Archivos**
    """)

    st.markdown("### 1. 📁 Navegación y Listado de Archivos")
    st.markdown("""
    Estos comandos te permitirán navegar por tu sistema de archivos y listar el contenido de los directorios.

    #### Listar Archivos y Directorios
    Utiliza el siguiente comando para listar los archivos y directorios en el directorio actual:
    ```bash
    ls
    ```

    **Ejemplo:** Lista el contenido de tu proyecto
    ```bash
    $ ls
    app.py  imágenes  README.md  notebooks
    ```
    Con este ejemplo podemos observar que tenemos 1 script `app.py`, una carpeta `imágenes`, un archivo `README.md` y otra carpeta denominada `notebooks`.

    #### Mostrar la Ruta del Directorio Actual
    Para mostrar la ruta completa del directorio actual, utiliza:
    ```bash
    pwd
    ```

    **Ejemplo:** Verifica tu ubicación actual en el sistema de archivos
    ```bash
    $ pwd
    /home/usuario/proyectos
    ```
    Esto nos muestra que actualmente estamos en el directorio `/home/usuario/proyectos`.

    #### Cambiar de Directorio
    Para cambiar al directorio especificado, utiliza:
    ```bash
    cd <nombre-del-directorio>
    ```

    **Ejemplo:** Cambia al directorio `documentos`
    ```bash
    $ ls
    app.py  documentos  imágenes
    $ cd documentos
    $ pwd
    /home/usuario/documentos
    ```
    Actualmente nos encontramos en el directorio `/home/usuario` y nos queremos mover a la carpeta `documentos`. Utilizamos el comando `cd` para movernos a dicho lugar y lo chequeamos mediante el comando `pwd` que nos arroja la ruta en la que nos situamos actualmente.

    📌 **Tip:** Usa `cd ..` para subir un nivel en la jerarquía de directorios.
    """)

    st.markdown("### 2. 📂 Gestión de Directorios")
    st.markdown("""
    Estos comandos te permitirán crear, eliminar y gestionar directorios en tu sistema.

    #### Crear un Nuevo Directorio
    Utiliza el siguiente comando para crear un nuevo directorio:
    ```bash
    mkdir <nombre-del-directorio>
    ```

    **Ejemplo:** Crea un nuevo directorio llamado `nuevo_directorio`
    ```bash
    $ mkdir nuevo_directorio
    $ ls
    app.py  documentos  imágenes  nuevo_directorio  README.md
    ```
    En este ejemplo, hemos creado un directorio llamado `nuevo_directorio`. Ahora, al listar el contenido del directorio actual con `ls`, podemos ver que `nuevo_directorio` ha sido añadido.

    #### Eliminar un Directorio
    Para eliminar un directorio y su contenido, utiliza:
    ```bash
    rm -r <nombre-del-directorio>
    ```

    **Ejemplo:** Elimina el directorio `viejo_directorio`
    ```bash
    $ rm -r viejo_directorio
    $ ls
    app.py  documentos  imágenes  README.md
    ```
    Aquí, hemos eliminado el directorio `viejo_directorio`. Al listar el contenido del directorio actual con `ls`, podemos ver que `viejo_directorio` ya no está presente.

    📌 **Tip:** Usa `rm -rf` con precaución, ya que elimina directorios de forma recursiva y forzada.
    """)

    st.markdown("### 3. 🗃️ Gestión de Archivos")
    st.markdown("""
    Estos comandos te permitirán crear, eliminar, copiar y mover archivos en tu sistema.

    #### Crear un Nuevo Archivo (Linux y MacOs)
    Utiliza el siguiente comando para crear un nuevo archivo vacío:
    ```bash
    touch <nombre-del-archivo>
    ```

    **Ejemplo:** Crea un archivo vacío llamado `archivo_nuevo.txt`
    ```bash
    touch archivo_nuevo.txt
    ls
    archivo_nuevo.txt  app.py  documentos  imágenes  README.md
    ```
    En este ejemplo, hemos creado un archivo vacío llamado `archivo_nuevo.txt`. Al listar el contenido del directorio actual con `ls`, podemos ver que `archivo_nuevo.txt` ha sido añadido.
                
    ### Crear un Nuevo Archivo (Windows)
    ```bash
    New-Item -ItemType file <nombre-del-archivo>
    ```
    **Ejemplo:** Crea un archivo vacío llamado `archivo_nuevo.txt`               
    ```bash
    New-Item -ItemType file archivo_nuevo.txt
    ls
    archivo_nuevo.txt  app.py  documentos  imágenes  README.md
    ```
    En este ejemplo, hemos creado un archivo vacío llamado `archivo_nuevo.txt`. Al listar el contenido del directorio actual con `ls`, podemos ver que `archivo_nuevo.txt` ha sido añadido.
   
    #### Eliminar un Archivo
    Para eliminar un archivo, utiliza:
    ```bash
    rm <nombre-del-archivo>
    ```

    **Ejemplo:** Elimina el archivo `archivo_viejo.txt`
    ```bash
    rm archivo_viejo.txt
    ls
    app.py  documentos  imágenes  README.md
    ```
    Aquí, hemos eliminado el archivo `archivo_viejo.txt`. Al listar el contenido del directorio actual con `ls`, podemos ver que `archivo_viejo.txt` ya no está presente.

    #### Copiar un Archivo
    Para copiar un archivo a otra ubicación, utiliza:
    ```bash
    cp <archivo_origen> <archivo_destino>
    ```

    **Ejemplo:** Copia el archivo `archivo.txt` a `copia_archivo.txt`
    ```bash
    $ cp archivo.txt copia_archivo.txt
    $ ls
    archivo.txt  app.py  copia_archivo.txt  documentos  imágenes  README.md
    ```
    En este ejemplo, hemos copiado `archivo.txt` a `copia_archivo.txt`. Al listar el contenido del directorio actual con `ls`, podemos ver que `copia_archivo.txt` ha sido añadido.

    #### Mover o Renombrar un Archivo
    Para mover o renombrar un archivo, utiliza:
    ```bash
    mv <archivo_origen> <archivo_destino>
    ```

    **Ejemplo:** Renombra `archivo.txt` a `nuevo_nombre.txt`
    ```bash
    $ mv archivo.txt nuevo_nombre.txt
    $ ls
    app.py  nuevo_nombre.txt  documentos  imágenes  README.md
    ```
    En este ejemplo, hemos renombrado `archivo.txt` a `nuevo_nombre.txt`. Al listar el contenido del directorio actual con `ls`, podemos ver que `archivo.txt` ha sido renombrado a `nuevo_nombre.txt`.

    📌 **Tip:** Usa `mv` para organizar tus archivos y directorios de manera eficiente.
    """)

    st.markdown("""
    ## Resumen de Comandos
    A continuación, se presenta un resumen de los comandos básicos de la terminal en formato de tabla.
    """)

    comandos = [
        {"Comando": "ls", "Descripción": "Lista los archivos y directorios en el directorio actual."},
        {"Comando": "cd nombre_del_directorio", "Descripción": "Cambia el directorio actual al especificado."},
        {"Comando": "cd ..", "Descripción": "Sube un nivel en la jerarquía de directorios."},
        {"Comando": "pwd", "Descripción": "Muestra la ruta completa del directorio actual."},
        {"Comando": "mkdir nombre_del_directorio", "Descripción": "Crea un nuevo directorio."},
        {"Comando": "touch nombre_del_archivo", "Descripción": "Crea un nuevo archivo vacío. (Linux y MacOs)"},
        {"Comando": "New-Item -ItemType file nombre_del_archivo", "Descripción": "Crea un nuevo archivo vacío. (Windows)"},
        {"Comando": "rm nombre_del_archivo", "Descripción": "Elimina archivos o directorios."},
        {"Comando": "cp archivo_origen archivo_destino", "Descripción": "Copia archivos o directorios."},
        {"Comando": "mv archivo_origen archivo_destino", "Descripción": "Mueve o renombra archivos o directorios."}
    ]

    # Crear un DataFrame con los comandos
    df_comandos_terminal = pd.DataFrame(comandos)
    st.dataframe(df_comandos_terminal, use_container_width=True)


def configuracion_e_inicializacion_git():
    st.title("Configuración e Inicialización de Git")
    st.markdown("""
    En esta sección, aprenderás cómo configurar Git para tu entorno y cómo inicializar un nuevo repositorio, pero antes trataremos.......
    ### ¿Qué es Git?
    Git es un sistema de control de versiones distribuido que te permite rastrear cambios en tus archivos y colaborar con otros desarrolladores. Es una herramienta esencial en el desarrollo de software moderno.

    **Beneficios de Git:**
    - **Distribución**: Cada desarrollador tiene una copia completa del historial del proyecto, lo que facilita el trabajo sin conexión y mejora la seguridad.
    - **Velocidad**: Optimizado para rendimiento, Git maneja grandes proyectos de forma rápida y eficiente.
    - **Colaboración**: Facilita la colaboración entre múltiples desarrolladores, permitiendo trabajar en paralelo y fusionar cambios de manera efectiva.
    ### Contenido
    1. ⚙️ **Configuración de Git**
    2. 🚀 **Inicialización de Repositorios**
    """)

    st.markdown("### 1. ⚙️ Configuración de Git")
    st.markdown("""
    Configurar Git adecuadamente es esencial para un uso efectivo. Aquí te mostramos cómo establecer tus configuraciones iniciales.

    #### Configurar el Nombre de Usuario
    Utiliza el siguiente comando para configurar tu nombre de usuario global:
    ```bash
    git config --global user.name "Tu Nombre"
    ```

    **Ejemplo:** Configura el nombre de usuario
    ```bash
    $ git config --global user.name "Alex Marza"
    ```

    #### Configurar el Correo Electrónico
    Configura tu correo electrónico global con:
    ```bash
    git config --global user.email "tuemail@example.com"
    ```

    **Ejemplo:** Configura el correo electrónico
    ```bash
    $ git config --global user.email "alex.marza@example.com"
    ```

    #### Verificar la Configuración Actual
    Para revisar la configuración actual de Git, usa:
    ```bash
    git config --list
    ```

    **Ejemplo:** Verifica la configuración de Git
    ```bash
    $ git config --list
    user.name=Alex Marza
    user.email=alex.marza@example.com
    ```

    #### Configuración Local
    Si deseas establecer configuraciones específicas para un repositorio, omite el flag `--global`:
    ```bash
    git config user.name "Nombre Local"
    ```

    **Ejemplo:** Configura el nombre de usuario local
    ```bash
    $ git config user.name "Alex Marza Local"
    ```

    📌 **Tip:** Usa `--global` para configuraciones que se aplicarán a todos los repositorios en tu máquina.
    """)

    st.markdown("""
    ## Resumen de Comandos
    A continuación, se presenta un resumen de los comandos básicos para configuración e inicialización en Git.
    """)

    comandos = [
        {"Comando": "git config --global user.name 'Tu Nombre'", "Descripción": "Configura el nombre de usuario global en Git."},
        {"Comando": "git config --global user.email 'tuemail@example.com'", "Descripción": "Configura el correo electrónico global en Git."},
        {"Comando": "git config --list", "Descripción": "Muestra la configuración actual de Git."},
        {"Comando": "git init", "Descripción": "Inicializa un nuevo repositorio Git en el directorio actual."}
    ]

    # Crear un DataFrame con los comandos
    df_comandos_git = pd.DataFrame(comandos)
    st.dataframe(df_comandos_git, use_container_width=True)

    st.markdown("### 2. 🚀 Inicialización de Repositorios en Git")
    st.markdown("""
    Una vez que Git esté configurado, puedes comenzar a gestionar tus proyectos con él. Aquí te mostramos cómo inicializar un nuevo repositorio.

    ### Pasos para Inicializar un Repositorio en GitHub

    #### Paso 1: Crea el Repositorio en GitHub
    Ve a [GitHub](https://github.com/) y crea un nuevo repositorio. Copia la URL del repositorio que has creado.

    #### Paso 2: Crea la Carpeta y Ficheros Necesarios para tu Proyecto
    En la terminal de Visual Studio Code editor de código fuente preferid0), navega hasta la ubicación donde deseas crear tu proyecto y crea una nueva carpeta:
    ```bash
    $ mkdir mi_proyecto
    $ cd mi_proyecto
    ```

    #### Paso 3: Inicializa el Repositorio Git
    Inicializa un repositorio en la carpeta del proyecto:
    ```bash
    $ git init
    Initialized empty Git repository in /home/usuario/mi_proyecto/.git/
    ```

    #### Paso 4: Añade los Archivos al Índice
    Añade todos los archivos de tu proyecto al índice de Git:
    ```bash
    $ git add .
    ```

    #### Paso 5: Realiza un Commit Inicial
    Realiza un commit inicial con un mensaje descriptivo:
    ```bash
    $ git commit -m "versión 1 del proyecto"
    ```

    #### Paso 6: Renombra la Rama Principal a 'main'
    Renombra la rama principal a 'main' (opcional, pero recomendado):
    ```bash
    $ git branch -M main
    ```

    #### Paso 7: Vincula el Repositorio Local con GitHub
    Añade la URL del repositorio remoto que copiaste en el paso 1:
    ```bash
    $ git remote add origin https://github.com/usuario/mi_proyecto.git
    ```

    #### Paso 8: Envía los Cambios al Repositorio Remoto
    Envía los cambios de la rama 'main' al repositorio remoto en GitHub:
    ```bash
    $ git push -u origin main
    ```

    📌 **Tip:** Asegúrate de que tienes permisos de escritura en el repositorio remoto.
    """)

    st.markdown("""
    ## Resumen de Comandos
    A continuación, se presenta un resumen de los comandos básicos para inicialización en Git.
    """)

    comandos_inicializacion = [
        {"Comando": "mkdir nombre_carpeta", "Descripción": "Crea una nueva carpeta."},
        {"Comando": "cd nombre_carpeta", "Descripción": "Cambia al directorio especificado."},
        {"Comando": "git init", "Descripción": "Inicializa un nuevo repositorio Git en el directorio actual."},
        {"Comando": "git add .", "Descripción": "Añade todos los archivos al índice de Git."},
        {"Comando": "git commit -m 'mensaje'", "Descripción": "Realiza un commit con el mensaje especificado."},
        {"Comando": "git branch -M main", "Descripción": "Renombra la rama principal a 'main'."},
        {"Comando": "git remote add origin URL", "Descripción": "Vincula el repositorio local con el remoto en GitHub."},
        {"Comando": "git push -u origin main", "Descripción": "Envía los cambios al repositorio remoto en GitHub."}
    ]

    df_comandos_inicializacion = pd.DataFrame(comandos_inicializacion)
    st.dataframe(df_comandos_inicializacion, use_container_width=True)



def operaciones_basicas():
    st.title("Operaciones Básicas con Git")
    st.markdown("""
    En esta sección, cubriremos las operaciones básicas que puedes realizar con Git, incluyendo cómo clonar repositorios, añadir y eliminar archivos, y cómo hacer commits y ver el historial.

    ### Contenido
    1. 📂 **Clonar Repositorios**
    2. ✏️ **Añadir y Eliminar Archivos**
    3. 📜 **Hacer Commits y Ver Historial**
    4. 🔄 **Actualizar y Sincronizar Repositorios**
    """)

    # Clonar Repositorios
    st.markdown("""
    ### 1. Clonar Repositorios
    Clonar un repositorio es el primer paso para empezar a colaborar en un proyecto existente o para trabajar en un proyecto desde otra máquina. Este proceso copia todo el contenido del repositorio desde el servidor remoto a tu máquina local.

    #### ¿Por Qué Clonar un Repositorio?
    - **Colaboración**: Permite trabajar en equipo en el mismo proyecto.
    - **Acceso Completo**: Obtienes todo el historial del proyecto, facilitando el seguimiento de cambios.
    - **Desarrollo Local**: Puedes trabajar en tu propio entorno de desarrollo sin afectar el repositorio original hasta que decidas enviar tus cambios.

    #### Pasos para Clonar un Repositorio
    1. **Obtener la URL del Repositorio**: La URL puede ser encontrada en la página principal del repositorio en plataformas como GitHub, GitLab, o Bitbucket.
    2. **Ejecutar el Comando de Clonado**: Abre tu terminal y utiliza el siguiente comando:
    ```bash
    git clone <URL-del-repositorio>
    ```

    **Ejemplo Real:**
    Para clonar el repositorio `Git` de GitHub, usa el siguiente comando:
    ```bash
    git clone https://github.com/AlexCapis/Git.git
    ```

    **Explicación del Ejemplo:**
    - `git clone https://github.com/AlexCapis/Git.git`: Este comando clona el repositorio desde la URL proporcionada a tu directorio actual. El repositorio será copiado en una nueva carpeta llamada `Git` en tu máquina local.

    📌 **Tip:** Si el repositorio es privado, necesitarás autenticación (nombre de usuario y contraseña, token de acceso, etc.) para clonar.

    **Resumen del Comando Clonado**
    ```bash
    git clone <URL-del-repositorio>
    ```
    - **`git clone`**: Comando para clonar repositorios.
    - **`<URL-del-repositorio>`**: La URL del repositorio remoto que deseas clonar.

    ¡Ahora estás listo para comenzar a trabajar con Git clonando repositorios de manera efectiva!
    """)

    # Añadir y Eliminar Archivos
    st.markdown("""
    ### 2. Añadir y Eliminar Archivos
    Git te permite añadir nuevos archivos a tu repositorio y eliminar los que ya no necesitas. Esto te ayuda a gestionar los cambios y mantener tu proyecto limpio y organizado.

    #### ¿Qué es el Área de Staging?
    El área de staging es una zona intermedia donde se almacenan los cambios que quieres confirmar en el próximo commit. Esto te permite preparar y revisar los cambios antes de hacerlos permanentes.

    ![Flujo del área de staging en Git](https://example.com/path/to/staging_area_image.png)
    """)

    st.markdown("""
    #### Añadir Archivos al Repositorio
    Para añadir nuevos archivos al área de staging, utiliza el comando `git add`.
    """)

    st.code("git add <archivo>", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para añadir un archivo llamado `nuevo-archivo.txt` al área de staging, usa el siguiente comando:
    ```bash
    git add nuevo-archivo.txt
    ```

    **Explicación del Ejemplo:**
    - `git add nuevo-archivo.txt`: Este comando agrega el archivo `nuevo-archivo.txt` al área de staging, preparándolo para el siguiente commit. No se realizan cambios en el repositorio hasta que se haga un commit.
                
    **Explicación del Comando:**
    - `git add .`: Este comando agrega todos los archivos en el directorio actual y sus subdirectorios al área de staging. Es una manera rápida de añadir múltiples archivos a la vez.

    **Advertencia:**
    - **Uso Cauteloso:** `git add .` añade todos los archivos modificados, nuevos y eliminados en el directorio actual y sus subdirectorios al área de staging. Esto puede incluir archivos que no deseas agregar, como archivos temporales, de configuración o de compilación. Es recomendable revisar los archivos antes de usar este comando para evitar agregar cambios no deseados.

    📌 **Tip:** Utiliza `git status` para revisar qué archivos están a punto de ser añadidos al área de staging antes de ejecutar `git add .`.


                



    #### Eliminar Archivos del Repositorio
    Para eliminar un archivo del repositorio y del área de staging, usa el comando `git rm`.
    """)
    

    st.code("git rm <archivo>", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para eliminar un archivo llamado `archivo-a-eliminar.txt`, usa el siguiente comando:
    ```bash
    git rm archivo-a-eliminar.txt
    ```

    **Explicación del Ejemplo:**
    - `git rm archivo-a-eliminar.txt`: Este comando elimina el archivo `archivo-a-eliminar.txt` tanto del repositorio como del área de staging. El archivo ya no estará disponible en el repositorio después de hacer un commit.

    📌 **Tip:** Si solo deseas eliminar el archivo del área de staging pero mantenerlo en tu directorio de trabajo, usa `git reset HEAD <archivo>` en lugar de `git rm`.

    """)

    # Hacer Commits y Ver Historial
    st.markdown("""
    ### 3. Hacer Commits y Ver Historial
    Realizar commits es una de las funciones más importantes de Git, ya que te permite guardar el estado de tu proyecto en un punto específico en el tiempo. También puedes ver el historial de commits para rastrear los cambios realizados y entender cómo ha evolucionado tu proyecto.
    """)

    st.markdown("""
    #### Hacer un Commit
    Para guardar los cambios en el repositorio, usa el comando `git commit` con un mensaje descriptivo.
    """)

    st.code("git commit -m \"Mensaje del commit\"", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para guardar tus cambios con un mensaje descriptivo, usa el siguiente comando:
    ```bash
    git commit -m "Añadido nuevo archivo de configuración"
    ```

    **Explicación del Ejemplo:**
    - `git commit -m "Añadido nuevo archivo de configuración"`: Este comando crea un nuevo commit con el mensaje `"Añadido nuevo archivo de configuración"`. El commit guardará los cambios que están en el área de staging.

    #### Ver el Historial de Commits
    Para ver el historial de commits, utiliza el comando `git log`.
    """)

    st.code("git log", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para ver el historial de commits, usa el siguiente comando:
    ```bash
    git log
    ```

    **Explicación del Ejemplo:**
    - `git log`: Muestra el historial de commits del repositorio, incluyendo los mensajes de commit, el autor, la fecha y el hash del commit. Esto te permite rastrear la evolución de tu proyecto y revisar los cambios realizados.

    📌 **Tip:** Usa `git log --oneline` para ver un historial más compacto y legible.

    """)

    # Actualizar y Sincronizar Repositorios
    st.markdown("""
    ### 4. Actualizar y Sincronizar Repositorios
    Mantener tu repositorio local actualizado con los cambios del repositorio remoto es esencial para colaborar efectivamente y evitar conflictos.

    #### Actualizar el Repositorio Local
    Usa `git pull` para descargar y fusionar los cambios del repositorio remoto con tu repositorio local.
    """)

    st.code("git pull", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para actualizar tu repositorio local con los cambios del remoto, usa el siguiente comando:
    ```bash
    git pull
    ```

    **Explicación del Ejemplo:**
    - `git pull`: Este comando descarga los cambios del repositorio remoto y los fusiona con tu repositorio local. Es útil para mantener tu copia local al día con los últimos cambios realizados por otros colaboradores.

    #### Enviar Cambios al Repositorio Remoto
    Usa `git push` para enviar tus cambios locales al repositorio remoto.
    """)

    st.code("git push", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para enviar tus cambios al repositorio remoto, usa el siguiente comando:
    ```bash
    git push
    ```

    **Explicación del Ejemplo:**
    - `git push`: Este comando envía los commits de tu rama local al repositorio remoto. Es necesario para compartir tus cambios con otros colaboradores o para realizar una copia de seguridad de tu trabajo en el servidor remoto.

    #### Verificar el Estado del Repositorio
    Usa `git status` para ver el estado actual de tu repositorio, incluyendo los archivos modificados y el estado del área de staging.
    """)

    st.code("git status", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para verificar el estado de tu repositorio, usa el siguiente comando:
    ```bash
    git status
    ```

    **Explicación del Ejemplo:**
    - `git status`: Muestra información sobre el estado actual del repositorio, como los archivos modificados, los archivos en el área de staging y la rama en la que te encuentras. Es útil para obtener una visión general de los cambios que están listos para ser confirmados o los archivos que necesitan atención.

    #### Estado Compacto del Repositorio
    Usa `git status -s` para ver el estado del repositorio en un formato compacto.
    """)

    st.code("git status -s", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para ver el estado de tu repositorio en un formato compacto, usa el siguiente comando:
    ```bash
    git status -s
    ```

    **Explicación del Ejemplo:**
    - `git status -s`: Muestra el estado del repositorio en un formato compacto, lo que facilita una visión rápida de los cambios. Los cambios se representan con códigos de estado abreviados, como `A` para archivos añadidos y `M` para archivos modificados.

    #### Crear Alias para Comandos
    Los alias en Git te permiten crear atajos para comandos largos.
    """)

    st.code("git config --global alias.<nombre-alias> '<comando>'", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para crear un alias para el comando `git status`, usa el siguiente comando:
    ```bash
    git config --global alias.st status
    ```

    Después puedes usar el alias así:
    ```bash
    git st
    ```

    **Explicación del Ejemplo:**
    - `git config --global alias.st status`: Este comando crea un alias `st` para el comando `git status`. Luego, puedes usar `git st` en lugar de `git status`, lo que ahorra tiempo al escribir comandos largos.""")

    # Resumen de Comandos Básicos
    st.markdown("""
    ### Resumen de Comandos Básicos

    Aquí tienes un resumen de los comandos básicos que hemos cubierto:

    """)

    data = {
        "Comando": [
            "git clone <URL>",
            "git add <archivo>",
            "git add ."
            "git rm <archivo>",
            "git commit -m \"mensaje\"",
            "git log",
            "git pull",
            "git push",
            "git status",
            "git status -s",
            "git config --global alias.<nombre-alias> '<comando>'"
        ],
        "Descripción": [
            "Clona un repositorio",
            "Añade un archivo al área de staging",
            "Añade todo lo que esté en el área de staging",
            "Elimina un archivo del repositorio",
            "Guarda los cambios con un mensaje",
            "Muestra el historial de commits",
            "Descarga y fusiona cambios del remoto",
            "Envía cambios locales al remoto",
            "Muestra el estado del repositorio",
            "Muestra el estado en formato compacto",
            "Crea un alias para un comando largo"
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

    st.markdown("""
    ¡Con estos comandos básicos, ya puedes comenzar a trabajar con Git y gestionar tu código de manera efectiva!
    """)

def ramas_colaboracion():
    st.title("Ramas y Colaboración")
    st.markdown("""
    En esta sección, aprenderás a crear y gestionar ramas, realizar merges y resolver conflictos, y estrategias de colaboración en proyectos.

    ### Contenido
    1. 🌿 **Crear y Gestionar Ramas**
    2. 🔀 **Realizar Merges y Resolver Conflictos**
    3. 🤝 **Estrategias de Colaboración en Proyectos**
    """)

    st.markdown("### 1. 🌿 Crear y Gestionar Ramas")
    st.markdown("""
    Las ramas en Git te permiten trabajar en diferentes características o arreglos de manera aislada. Esto es esencial para una colaboración eficiente.

    #### Crear una Nueva Rama
    Utiliza el siguiente comando para crear una nueva rama:
    ```bash
    git branch <nombre-de-la-rama>
    ```

    **Ejemplo Real:**
    ```bash
    git branch feature-nueva
    ```

    **Explicación del Ejemplo:**
    - `git branch feature-nueva`: Crea una nueva rama llamada `feature-nueva`. Esto te permite trabajar en nuevas características sin afectar la rama principal.

    #### Cambiar a una Rama Diferente
    Para cambiar a una rama existente, utiliza:
    ```bash
    git checkout <nombre-de-la-rama>
    ```

    **Ejemplo Real:**
    ```bash
    git checkout feature-nueva
    ```

    **Explicación del Ejemplo:**
    - `git checkout feature-nueva`: Cambia a la rama `feature-nueva`, permitiéndote trabajar en los cambios realizados en esa rama.

    #### Crear y Cambiar a una Nueva Rama en un Solo Paso
    Utiliza el siguiente comando para crear una nueva rama y cambiarte a ella en un solo paso:
    ```bash
    git checkout -b <nombre-de-la-rama>
    ```

    **Ejemplo Real:**
    ```bash
    git checkout -b feature-nueva
    ```

    **Explicación del Ejemplo:**
    - `git checkout -b feature-nueva`: Crea una nueva rama llamada `feature-nueva` y cambia a ella inmediatamente.

    #### Ver todas las Ramas
    Puedes listar todas las ramas en tu repositorio con:
    ```bash
    git branch
    ```

    **Ejemplo Real:**
    ```bash
    git branch
    ```

    **Explicación del Ejemplo:**
    - `git branch`: Muestra una lista de todas las ramas en tu repositorio, con un asterisco (*) indicando la rama activa.

    📌 **Tip:** Usa nombres descriptivos para tus ramas para mantener tu proyecto organizado, por ejemplo, `feature/nueva-funcionalidad` o `bugfix/arreglo-error`.

    📌 **Tip:** Si deseas eliminar una rama que ya no necesitas, usa `git branch -d <nombre-de-la-rama>`. Asegúrate de que la rama haya sido fusionada antes de eliminarla para evitar la pérdida de trabajo.

    """)

    st.markdown("### 2. 🔀 Realizar Merges y Resolver Conflictos")
    st.markdown("""
    Una vez que has terminado de trabajar en una rama, puedes integrar esos cambios en otra rama (por ejemplo, la rama principal) utilizando el comando de merge.

    #### Realizar un Merge
    Primero, cambia a la rama donde quieres integrar los cambios:
    ```bash
    git checkout main
    ```

    Luego, realiza el merge:
    ```bash
    git merge <nombre-de-la-rama>
    ```

    **Ejemplo Real:**
    ```bash
    git merge feature-nueva
    ```

    **Explicación del Ejemplo:**
    - `git merge feature-nueva`: Integra los cambios de `feature-nueva` en la rama actual (en este caso, `main`). Asegúrate de resolver cualquier conflicto si es necesario.

    #### Resolver Conflictos
    Si Git encuentra cambios conflictivos, te pedirá que los resuelvas manualmente. Abre los archivos conflictivos, edita y guarda los cambios, y luego añade los archivos resueltos al área de staging:
    ```bash
    git add <archivo-conflictivo>
    ```

    **Ejemplo Real:**
    ```bash
    git add archivo-conflictivo.txt
    ```

    **Explicación del Ejemplo:**
    - `git add archivo-conflictivo.txt`: Añade el archivo `archivo-conflictivo.txt` al área de staging después de haber resuelto los conflictos.

    Una vez resueltos todos los conflictos, realiza el commit:
    ```bash
    git commit -m "Resolver conflictos de merge"
    ```

    **Explicación del Ejemplo:**
    - `git commit -m "Resolver conflictos de merge"`: Guarda los cambios después de resolver los conflictos. El mensaje del commit debe describir los conflictos que se resolvieron.

    📌 **Tip:** Usa herramientas de merge como `kdiff3`, `meld`, o editores como VS Code para facilitar la resolución de conflictos. Estas herramientas te proporcionan una interfaz visual para comparar y fusionar los cambios.

    """)

    st.markdown("### 3. 🤝 Estrategias de Colaboración en Proyectos")
    st.markdown("""
    La colaboración en proyectos implica coordinarse eficientemente con tu equipo. Aquí hay algunas estrategias y buenas prácticas:

    #### Uso de Pull Requests
    - **Pull Requests (PR)** permiten revisar y discutir los cambios antes de integrarlos en la rama principal.
    - Utiliza plataformas como GitHub, GitLab, o Bitbucket para gestionar PRs.

    #### Revisión de Código
    - Realiza revisiones de código regularmente para mantener la calidad del código.
    - Asigna revisores y utiliza comentarios para discutir posibles mejoras.

    #### Integración Continua
    - Configura **CI/CD** para realizar pruebas automáticas y asegurar que los cambios no rompan el proyecto.
    - Herramientas como Jenkins, Travis CI, y GitHub Actions son útiles para la integración continua.

    📌 **Tip:** Establece convenciones de commits y flujo de trabajo (como GitFlow) para mantener el orden y la coherencia en el proyecto.

    """)

    # Título de la sección
    st.markdown("### Resumen de Comandos para Ramas y Colaboración")

    # Crear un DataFrame para la tabla de comandos
    data = {
        "Comando": [
            "`git branch <nombre-de-la-rama>`",
            "`git checkout <nombre-de-la-rama>`",
            "`git checkout -b <nombre-de-la-rama>`",
            "`git branch`",
            "`git merge <nombre-de-la-rama>`",
            "`git add <archivo-conflictivo>`",
            "`git commit -m \"Resolver conflictos de merge\"`",
            "`git branch -d <nombre-de-la-rama>`"
        ],
        "Descripción": [
            "Crea una nueva rama",
            "Cambia a una rama diferente",
            "Crea una nueva rama y cambia a ella en un solo paso",
            "Ver todas las ramas",
            "Realizar un merge",
            "Añadir archivos conflictivos resueltos al área de staging",
            "Guardar los cambios después de resolver conflictos de merge",
            "Eliminar una rama"
        ]
    }

    df = pd.DataFrame(data)

    # Mostrar la tabla usando Streamlit
    st.table(df)

    st.markdown("""
    ### Estrategias de Colaboración en Proyectos
    - **Uso de Pull Requests**: Revisar y discutir cambios antes de integrarlos. Utilizar plataformas como GitHub, GitLab, o Bitbucket para gestionar PRs.
    - **Revisión de Código**: Realizar revisiones de código regularmente. Asignar revisores y utilizar comentarios para discutir mejoras.
    - **Integración Continua**: Configurar CI/CD para pruebas automáticas. Herramientas útiles: Jenkins, Travis CI, GitHub Actions.
    
    📌 **Tip:** Establecer convenciones de commits y flujo de trabajo (como GitFlow) para mantener el orden y la coherencia en el proyecto.
    """)

    st.markdown("""
    ¡Con estas estrategias y comandos, estarás listo para colaborar efectivamente y gestionar tus ramas en Git!
    """)




def avanzado_git():
    st.title("Uso Avanzado de Git")
    
    st.markdown("""
    En esta sección, exploraremos técnicas avanzadas como rebase, stash, cherry-pick y otros comandos útiles para mejorar tu flujo de trabajo. Estas herramientas te permiten mantener un historial de commits limpio y manejar cambios de forma eficiente.

    ### Contenido
    1. 🔄 **Rebase**
    2. 🗂️ **Stash**
    3. 🍒 **Cherry-Pick**
    4. 🔄 **Reset**
    5. 🔄 **Diff y Reflog**
    6. 🏷️ **Tag**
    """)

    st.markdown("### 🔄 Rebase")
    st.markdown("""
    Rebase te permite reescribir el historial de commits, haciendo que tu historia de commits sea más lineal y fácil de seguir.

    #### Comando de Rebase
    ```bash
    git rebase <rama-base>
    ```

    **Ejemplo Real:**
    Supongamos que estás trabajando en una rama `feature` y quieres actualizarla con los últimos cambios de la rama `main`:
    ```bash
    git checkout feature
    git rebase main
    ```

    **Explicación del Ejemplo:**
    - `git rebase main`: Reescribe el historial de la rama `feature` para que parezca que se basó en la punta actual de `main`. Esto hace que la historia sea más limpia y evita un merge commit adicional.

    📌 **Tip:** Utiliza `rebase` en lugar de `merge` para mantener un historial de commits más lineal. Sin embargo, evita rebase en ramas compartidas, ya que puede reescribir el historial y causar problemas a otros colaboradores.

    """)

    st.markdown("### 🗂️ Stash")
    st.markdown("""
    Stash guarda temporalmente tus cambios sin hacer un commit, lo que te permite cambiar de ramas sin perder tu trabajo.

    #### Comando de Stash
    ```bash
    git stash
    ```

    **Ejemplo Real:**
    Si estás trabajando en la rama `feature` y necesitas cambiar a la rama `main` para resolver un problema urgente, pero no has terminado tus cambios, usa:
    ```bash
    git stash
    git checkout main
    ```

    **Explicación del Ejemplo:**
    - `git stash`: Guarda tus cambios actuales en un stash temporal y limpia tu área de trabajo. Puedes luego cambiar de rama sin perder los cambios.

    #### Aplicar y Eliminar Stash
    ```bash
    git stash apply
    git stash pop
    ```

    **Ejemplo Real:**
    Después de resolver el problema en `main`, regresa a `feature` y aplica los cambios guardados:
    ```bash
    git checkout feature
    git stash apply
    ```

    **Explicación del Ejemplo:**
    - `git stash apply`: Aplica los cambios guardados en el stash a tu área de trabajo actual.
    - `git stash pop`: Aplica los cambios del stash y luego elimina el stash de la lista.

    📌 **Tip:** Usa `git stash list` para ver todos los stashes guardados. Esto te ayudará a gestionar múltiples stashes si los estás utilizando.

    """)

    st.markdown("### 🍒 Cherry-Pick")
    st.markdown("""
    Cherry-pick te permite aplicar cambios de commits específicos a tu rama actual, sin necesidad de hacer un merge completo.

    #### Comando de Cherry-Pick
    ```bash
    git cherry-pick <id-del-commit>
    ```

    **Ejemplo Real:**
    Supongamos que tienes un commit específico en la rama `bugfix` que deseas aplicar a la rama `main`:
    ```bash
    git checkout main
    git cherry-pick a1b2c3d4
    ```

    **Explicación del Ejemplo:**
    - `git cherry-pick a1b2c3d4`: Aplica el commit con el ID `a1b2c3d4` a la rama `main`. Esto es útil para aplicar correcciones o cambios específicos sin fusionar todas las ramas.

    📌 **Tip:** Ideal para aplicar hotfixes en ramas de producción sin mezclar cambios innecesarios de otras ramas.

    """)

    st.markdown("### 🔄 Reset")
    st.markdown("""
    `git reset` te permite deshacer cambios y volver a un estado anterior en tu repositorio.

    #### Comando de Reset
    ```bash
    git reset --hard <commit-id>
    ```

    **Ejemplo Real:**
    Si quieres deshacer todos los cambios recientes y volver a un commit anterior, usa:
    ```bash
    git reset --hard a1b2c3d4
    ```

    **Explicación del Ejemplo:**
    - `git reset --hard a1b2c3d4`: Reestablece tu repositorio al commit con el ID `a1b2c3d4`. Todos los cambios no confirmados y commits posteriores se perderán.

    #### Reset Suave
    ```bash
    git reset --soft HEAD~1
    ```

    **Ejemplo Real:**
    Si deseas deshacer el último commit pero conservar los cambios en el área de staging:
    ```bash
    git reset --soft HEAD~1
    ```

    **Explicación del Ejemplo:**
    - `git reset --soft HEAD~1`: Deshace el último commit pero mantiene los cambios en el área de staging, permitiéndote corregir el commit y hacer uno nuevo.

    📌 **Tip:** Usa `git reset --hard` con precaución, ya que perderás todos los cambios no confirmados. `git reset --soft` es útil para modificar commits recientes sin perder cambios.

    """)

    st.markdown("### 🔄 Diff y Reflog")
    st.markdown("""
    #### Diff
    `git diff` muestra las diferencias entre archivos en tu repositorio.

    ```bash
    git diff
    ```

    **Ejemplo Real:**
    Para ver las diferencias entre tus cambios actuales y el último commit:
    ```bash
    git diff
    ```

    **Explicación del Ejemplo:**
    - `git diff`: Muestra los cambios en los archivos no confirmados en comparación con el último commit.

    #### Reflog
    `git reflog` muestra el historial de los cambios en los HEADs de tu repositorio, lo que te permite recuperar commits perdidos.

    ```bash
    git reflog
    ```

    **Ejemplo Real:**
    Para ver el historial de movimientos del HEAD:
    ```bash
    git reflog
    ```

    **Explicación del Ejemplo:**
    - `git reflog`: Muestra el historial de todos los cambios en el HEAD, útil para recuperar commits o revertir cambios.

    📌 **Tip:** Usa `git diff` para revisar cambios antes de hacer un commit y `git reflog` para recuperar commits que hayas perdido accidentalmente.

    """)

    st.markdown("### 🏷️ Tag")
    st.markdown("""
    `git tag` te permite crear etiquetas en puntos específicos del historial de commits, a menudo usado para marcar versiones de software.

    #### Comando de Tag
    ```bash
    git tag <nombre-del-tag>
    ```

    **Ejemplo Real:**
    Para marcar un commit como versión `v1.0`:
    ```bash
    git tag v1.0
    ```

    **Explicación del Ejemplo:**
    - `git tag v1.0`: Crea una etiqueta `v1.0` en el commit actual. Las etiquetas son útiles para marcar versiones estables en tu proyecto.

    📌 **Tip:** Usa etiquetas para marcar versiones de lanzamiento en tu repositorio y facilitar el seguimiento de versiones.

    """)

    # Resumen de Comandos
    st.markdown("### Resumen de Comandos Avanzados")

    data = {
        "Comando": [
            "`git rebase <rama-base>`",
            "`git stash`",
            "`git stash apply`",
            "`git cherry-pick <id-del-commit>`",
            "`git reset --hard <commit-id>`",
            "`git reset --soft HEAD~1`",
            "`git diff`",
            "`git reflog`",
            "`git tag <nombre-del-tag>`"
        ],
        "Descripción": [
            "Reescribe el historial de commits",
            "Guarda temporalmente tus cambios",
            "Aplica los cambios guardados con stash",
            "Aplica cambios de un commit específico",
            "Deshace cambios y vuelve a un commit anterior",
            "Deshace el último commit pero conserva los cambios",
            "Muestra las diferencias entre archivos",
            "Muestra el historial de movimientos del HEAD",
            "Crea una etiqueta en el historial de commits"
        ]
    }

    df = pd.DataFrame(data)
    st.table(df)


def integracion_github():
    st.title("Integración con GitHub")
    
    st.markdown("""
    En esta sección, aprenderás cómo conectar tu repositorio local con GitHub, crear y gestionar pull requests, y algunos consejos útiles para mejorar tu flujo de trabajo con Git.

    ### Contenido
    1. 🌐 **Conectar Repositorio Local a GitHub**
    2. 🚀 **Pull Requests**
    3. 🔍 **Consejos y Comandos Útiles**

    ### Conectar Repositorio Local a GitHub
    Para trabajar con GitHub, primero necesitas conectar tu repositorio local a un repositorio remoto en GitHub.

    #### Crear un Nuevo Repositorio en GitHub
    1. Ve a [GitHub](https://github.com) y accede a tu cuenta.
    2. Haz clic en el botón "New repository".
    3. Rellena los campos necesarios y haz clic en "Create repository".

    #### Conectar tu Repositorio Local
    ```bash
    git remote add origin <URL-del-repositorio>
    git branch -M main
    git push -u origin main
    ```

    **Ejemplo Real:**
    ```bash
    git remote add origin https://github.com/usuario/repositorio.git
    git branch -M main
    git push -u origin main
    ```

    **Explicación del Ejemplo:**
    - `git remote add origin <URL-del-repositorio>`: Conecta tu repositorio local con el remoto en GitHub.
    - `git branch -M main`: Renombra la rama actual a `main`, si no lo has hecho ya.
    - `git push -u origin main`: Sube la rama `main` al repositorio remoto y establece el seguimiento para futuros `push` y `pull`.

    📌 **Tip:** Asegúrate de reemplazar `<URL-del-repositorio>` con la URL de tu repositorio en GitHub.

    """)

    st.markdown("### 🚀 Pull Requests")
    st.markdown("""
    Las pull requests permiten que otros revisen tus cambios antes de fusionarlos con la rama principal del proyecto.

    #### Crear una Pull Request
    1. Crea y realiza commits en una nueva rama:
    ```bash
    git checkout -b <nombre-de-la-rama>
    # realiza cambios y commits
    git push origin <nombre-de-la-rama>
    ```
    2. En GitHub, ve a la página de tu repositorio y haz clic en "Compare & pull request".
    3. Completa los detalles necesarios y haz clic en "Create pull request".

    **Ejemplo Real:**
    ```bash
    git checkout -b feature/nueva-funcionalidad
    # realiza cambios
    git add .
    git commit -m "Añadir nueva funcionalidad"
    git push origin feature/nueva-funcionalidad
    ```

    **Explicación del Ejemplo:**
    - `git checkout -b <nombre-de-la-rama>`: Crea una nueva rama y cambia a ella.
    - `git push origin <nombre-de-la-rama>`: Sube tu rama al repositorio remoto en GitHub.
    - En GitHub, puedes abrir una pull request para integrar los cambios de la nueva rama en la rama principal.

    📌 **Tip:** Usa descripciones claras y detalladas en tus pull requests para facilitar la revisión y colaboración.

    """)

    st.markdown("### 🔍 Consejos y Comandos Útiles")
    st.markdown("""
    Aquí te presentamos algunos consejos y comandos adicionales que pueden ser útiles al trabajar con Git y GitHub.

    #### Comando de Verificación del Estado del Repositorio
    ```bash
    git status
    ```

    **Ejemplo Real:**
    ```bash
    git status
    ```

    **Explicación del Ejemplo:**
    - `git status`: Muestra el estado actual de tu repositorio, incluyendo archivos modificados y el estado de tus ramas.

    #### Sincronizar tu Repositorio con GitHub
    ```bash
    git fetch origin
    git pull origin main
    ```

    **Ejemplo Real:**
    ```bash
    git fetch origin
    git pull origin main
    ```

    **Explicación del Ejemplo:**
    - `git fetch origin`: Obtiene actualizaciones del repositorio remoto sin aplicarlas.
    - `git pull origin main`: Actualiza tu rama local con los últimos cambios de la rama `main` del repositorio remoto.

    #### Comando para Cambiar el Nombre de una Rama Remota
    ```bash
    git push origin :<nombre-antiguo>
    git push origin <nombre-nuevo>
    ```

    **Ejemplo Real:**
    ```bash
    git push origin :old-branch-name
    git push origin new-branch-name
    ```

    **Explicación del Ejemplo:**
    - `git push origin :<nombre-antiguo>`: Elimina la rama remota con el nombre antiguo.
    - `git push origin <nombre-nuevo>`: Sube una nueva rama con el nombre nuevo al repositorio remoto.

    📌 **Tip:** Mantén tus ramas y repositorios organizados para facilitar la colaboración y la gestión del proyecto.

    """)

    # Resumen de Comandos
    st.markdown("### Resumen de Comandos de Integración en GitHub")

    data = {
        "Comando": [
            "`git remote add origin <URL-del-repositorio>`",
            "`git branch -M main`",
            "`git push -u origin main`",
            "`git push origin <nombre-de-la-rama>`",
            "`git status`",
            "`git fetch origin`",
            "`git pull origin main`",
            "`git push origin :<nombre-antiguo>`",
            "`git push origin <nombre-nuevo>`"
        ],
        "Descripción": [
            "Conecta el repositorio local con el remoto en GitHub",
            "Renombra la rama actual a 'main'",
            "Sube la rama 'main' al repositorio remoto y establece el seguimiento",
            "Sube la rama especificada al repositorio remoto",
            "Muestra el estado actual del repositorio",
            "Obtiene actualizaciones del repositorio remoto",
            "Actualiza tu rama local con los últimos cambios del remoto",
            "Elimina una rama remota",
            "Sube una nueva rama remota con un nombre nuevo"
        ]
    }

    df = pd.DataFrame(data)
    st.table(df)


def resumen_taller():
    st.title("Resumen del Taller de Git")

    st.header("Comandos de Git Tratados")

    st.markdown("""
    En esta sección, encontrarás una tabla con los comandos clave de Git que hemos cubierto en el taller. Cada comando viene con una descripción, un ejemplo práctico y enlaces a la documentación oficial para que puedas aprender más en profundidad.

    Esta referencia rápida está diseñada para ayudarte a recordar y aplicar los comandos básicos y avanzados de Git de manera efectiva.
    """)

    # Crear un DataFrame con todos los comandos
    comandos = [
        {"Comando": "ls", "Descripción": "Lista los archivos y directorios en el directorio actual."},
        {"Comando": "cd nombre_del_directorio", "Descripción": "Cambia el directorio actual al especificado."},
        {"Comando": "cd ..", "Descripción": "Sube un nivel en la jerarquía de directorios."},
        {"Comando": "pwd", "Descripción": "Muestra la ruta completa del directorio actual."},
        {"Comando": "mkdir nombre_del_directorio", "Descripción": "Crea un nuevo directorio."},
        {"Comando": "touch nombre_del_archivo", "Descripción": "Crea un nuevo archivo vacío. (Linux y MacOS)"},
        {"Comando": "New-Item -ItemType file nombre_del_archivo", "Descripción": "Crea un nuevo archivo vacío. (Windows)"},
        {"Comando": "rm nombre_del_archivo", "Descripción": "Elimina archivos o directorios."},
        {"Comando": "cp archivo_origen archivo_destino", "Descripción": "Copia archivos o directorios."},
        {"Comando": "mv archivo_origen archivo_destino", "Descripción": "Mueve o renombra archivos o directorios."},
        {"Comando": "mkdir nombre_carpeta", "Descripción": "Crea una nueva carpeta."},
        {"Comando": "cd nombre_carpeta", "Descripción": "Cambia al directorio especificado."},
        {"Comando": "git init", "Descripción": "Inicializa un nuevo repositorio Git en el directorio actual."},
        {"Comando": "git add .", "Descripción": "Añade todos los archivos al índice de Git."},
        {"Comando": "git commit -m 'mensaje'", "Descripción": "Realiza un commit con el mensaje especificado."},
        {"Comando": "git branch -M main", "Descripción": "Renombra la rama principal a 'main'."},
        {"Comando": "git remote add origin URL", "Descripción": "Vincula el repositorio local con el remoto en GitHub."},
        {"Comando": "git push -u origin main", "Descripción": "Envía los cambios al repositorio remoto en GitHub."},
        {"Comando": "git clone <URL>", "Descripción": "Clona un repositorio remoto a tu máquina local."},
        {"Comando": "git add <archivo>", "Descripción": "Añade un archivo específico al área de staging."},
        {"Comando": "git rm <archivo>", "Descripción": "Elimina un archivo del repositorio."},
        {"Comando": "git log", "Descripción": "Muestra el historial de commits realizados en el repositorio."},
        {"Comando": "git pull", "Descripción": "Descarga y fusiona cambios del repositorio remoto."},
        {"Comando": "git push", "Descripción": "Envía cambios locales al repositorio remoto."},
        {"Comando": "git status", "Descripción": "Muestra el estado actual del repositorio."},
        {"Comando": "git status -s", "Descripción": "Muestra el estado en formato compacto."},
        {"Comando": "git config --global alias.<nombre-alias> '<comando>'", "Descripción": "Crea un alias para un comando largo."},
        {"Comando": "git rebase <rama-base>", "Descripción": "Reescribe el historial de commits para una historia más lineal."},
        {"Comando": "git stash", "Descripción": "Guarda temporalmente tus cambios no confirmados."},
        {"Comando": "git stash apply", "Descripción": "Aplica los cambios guardados con stash."},
        {"Comando": "git cherry-pick <id-del-commit>", "Descripción": "Aplica cambios de un commit específico a tu rama actual."},
        {"Comando": "git reset --hard <commit-id>", "Descripción": "Deshace cambios y vuelve a un commit anterior eliminando los cambios actuales."},
        {"Comando": "git reset --soft HEAD~1", "Descripción": "Deshace el último commit pero conserva los cambios en el área de staging."},
        {"Comando": "git diff", "Descripción": "Muestra las diferencias entre archivos o entre commits."},
        {"Comando": "git reflog", "Descripción": "Muestra el historial de movimientos del HEAD."},
        {"Comando": "git tag <nombre-del-tag>", "Descripción": "Crea una etiqueta en el historial de commits."},
        {"Comando": "git remote add origin <URL-del-repositorio>", "Descripción": "Conecta el repositorio local con el remoto en GitHub."},
        {"Comando": "git branch -M main", "Descripción": "Renombra la rama actual a 'main'."},
        {"Comando": "git push -u origin main", "Descripción": "Sube la rama 'main' al repositorio remoto y establece el seguimiento."},
        {"Comando": "git push origin <nombre-de-la-rama>", "Descripción": "Sube la rama especificada al repositorio remoto."},
        {"Comando": "git fetch origin", "Descripción": "Obtiene actualizaciones del repositorio remoto."},
        {"Comando": "git pull origin main", "Descripción": "Actualiza tu rama local con los últimos cambios del remoto."},
        {"Comando": "git push origin :<nombre-antiguo>", "Descripción": "Elimina una rama remota con el nombre antiguo."},
        {"Comando": "git push origin <nombre-nuevo>", "Descripción": "Sube una nueva rama remota con un nombre nuevo."}
    ]

    df_comandos = pd.DataFrame(comandos)
    st.dataframe(df_comandos, use_container_width=True)

    st.header("Tips y Trucos Útiles")
    st.markdown("""
    A continuación, se presentan algunos consejos y trucos que pueden ayudarte a mejorar tu flujo de trabajo con Git. Cada consejo viene con un ejemplo práctico y una explicación para ilustrar su uso.

    - **Utiliza alias en Git:** Configura alias para comandos comunes para ahorrar tiempo.
      - **Ejemplo:** Para usar `git st` en lugar de `git status`, configura un alias así:
        ```bash
        git config --global alias.st status
        ```
        **Explicación:** Este comando crea un alias llamado `st` que puedes usar en lugar de escribir `git status` cada vez. Es útil para acelerar tu flujo de trabajo con Git.

    - **Revertir un commit:** Usa `git revert <commit>` para crear un nuevo commit que revierta los cambios del commit especificado, sin eliminar el historial.
      - **Ejemplo:** Para revertir el commit con ID `abc123`, usa:
        ```bash
        git revert abc123
        ```
        **Explicación:** Este comando crea un nuevo commit que deshace los cambios introducidos en el commit `abc123`. Es una forma segura de revertir cambios sin modificar el historial de commits.

    - **Comparar cambios:** Usa `git diff` para ver las diferencias entre tu área de trabajo y el área de staging, o entre commits.
      - **Ejemplo:** Para comparar cambios en tu área de trabajo:
        ```bash
        git diff
        ```
        **Explicación:** Muestra las diferencias entre los archivos modificados en tu directorio de trabajo y el último commit. Es útil para revisar cambios antes de hacer un commit.

      - **Ejemplo:** Para comparar cambios entre el último commit y tu área de staging:
        ```bash
        git diff --cached
        ```
        **Explicación:** Muestra las diferencias entre el área de staging y el último commit. Es útil para revisar qué cambios se han preparado para el próximo commit.

    - **Deshacer cambios en un archivo:** Usa `git restore <archivo>` para descartar cambios en un archivo específico que no has añadido al área de staging.
      - **Ejemplo:** Para descartar cambios en `archivo.txt`:
        ```bash
        git restore archivo.txt
        ```
        **Explicación:** Este comando descarta los cambios realizados en `archivo.txt` que no se han añadido al área de staging. Es útil si decides que no quieres mantener las modificaciones en un archivo específico.

    - **Ver cambios en un archivo específico:** Usa `git log -p <archivo>` para revisar los cambios realizados en un archivo a lo largo del tiempo.
      - **Ejemplo:** Para ver el historial de cambios en `archivo.txt`:
        ```bash
        git log -p archivo.txt
        ```
        **Explicación:** Muestra el historial de commits que han modificado `archivo.txt`, incluyendo los detalles de cada cambio. Es útil para rastrear cómo ha evolucionado un archivo a lo largo del tiempo.

    - **Colores en el terminal:** Activa colores en el terminal para diferenciar mejor los cambios.
      - **Ejemplo:** Para habilitar colores en Git:
        ```bash
        git config --global color.ui auto
        ```
        **Explicación:** Este comando habilita la coloración automática de la salida de los comandos de Git, lo que facilita la lectura de la información en el terminal, especialmente para distinguir entre cambios añadidos, modificados o eliminados.

    - **Búsqueda en el historial de commits:** Usa `git log --grep="texto"` para buscar commits que contienen un texto específico en el mensaje.
      - **Ejemplo:** Para buscar commits que contienen la palabra "bug":
        ```bash
        git log --grep="bug"
        ```
        **Explicación:** Muestra una lista de commits cuyos mensajes contienen el texto "bug". Es útil para encontrar cambios relacionados con un tema específico, como un error o una característica.

    - **Modificar el último commit:** Si necesitas hacer cambios en el último commit, usa `git commit --amend` para editar el mensaje o agregar más cambios.
      - **Ejemplo:** Para cambiar el mensaje del último commit:
        ```bash
        git commit --amend -m "Nuevo mensaje del commit"
        ```
        **Explicación:** Permite modificar el mensaje del último commit sin crear un nuevo commit. Es útil para corregir errores en el mensaje de commit original.

      - **Ejemplo:** Para agregar más cambios al último commit:
        ```bash
        git add archivo_modificado
        git commit --amend --no-edit
        ```
        **Explicación:** Añade cambios adicionales al último commit sin cambiar el mensaje. Es útil para incluir correcciones adicionales sin crear un nuevo commit.

    """)
    st.header("Documentación")
    st.markdown("""
    **Recursos Adicionales:**
    - [Libro Pro Git Gratuito](https://git-scm.com/book/en/v2)
    - [Cheat Sheet Git](https://training.github.com/downloads/es_ES/github-git-cheat-sheet/)
    - [Documentación GitHub](docs.github.com/es)
    - [Git Official Documentation](https://git-scm.com/doc)
    - [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
    """)


# Inicializar variables de estado para las respuestas y puntuación
if 'correctas' not in st.session_state:
    st.session_state.correctas = 0
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}
if 'opciones' not in st.session_state:
    st.session_state.opciones = {}
if 'respuestas_correctas' not in st.session_state:
    st.session_state.respuestas_correctas = {
        "q1": "git clone <URL>",
        "q2": "git add <archivo>",
        "q3": 'git commit -m "mensaje"',
        "q4": "git log",
        "q5": "git stash",
        "q6": "git merge feature-x",
        "q7": "git rm deprecated_feature.py",
        "q8": "git diff abc123 def456",
        "q9": "git push origin feature-y",
        "q10": "git reset --soft HEAD~1"
    }

def inicializar_opciones():
    st.session_state.opciones = {
        "q1": [ "git pull <URL>", "git fetch <URL>","git clone <URL>", "git clone --bare <URL>"],
        "q2": ["git add <archivo>", "git commit <archivo>", "git push <archivo>", "git remove <archivo>"],
        "q3": [ 'git commit -a -m "mensaje"', 'git commit --message "mensaje"','git commit -m "mensaje"', 'git commit -m "nuevo mensaje"'],
        "q4": ["git status", "git log", "git history", "git log --oneline"],
        "q5": ["git tag", "git commit --amend", "git reset","git stash"],
        "q6": [ "git rebase feature-x", "git cherry-pick feature-x","git merge feature-x", "git merge main"],
        "q7": ["git delete deprecated_feature.py", "git remove deprecated_feature.py", "git drop deprecated_feature.py""git rm deprecated_feature.py"],
        "q8": ["git diff abc123 def456", "git log abc123 def456", "git status abc123 def456", "git show abc123 def456"],
        "q9": [ "git upload feature-y","git push origin feature-y", "git push --set-upstream origin feature-y", "git push --new-branch feature-y"],
        "q10": ["git reset --soft HEAD~1", "git revert HEAD", "git reset --hard HEAD~1", "git restore --source HEAD~1"]
    }

def verificar_respuesta(respuesta_usuario, pregunta_id):
    respuesta_correcta = st.session_state.respuestas_correctas[pregunta_id]
    if respuesta_usuario.strip() == respuesta_correcta:
        st.success("¡Correcto!")
        st.session_state.correctas += 1
    else:
        st.error(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")
    st.session_state.respuestas[pregunta_id] = respuesta_usuario

def ejercicios():
    if not st.session_state.opciones:
        inicializar_opciones()
    
    st.title("Ejercicios de Git")
    
    # Ejercicio 1
    st.header("Ejercicio 1: Clonar un Repositorio")
    st.markdown("""
    Imagina que te han proporcionado la URL de un repositorio Git y quieres empezar a trabajar en él en tu máquina local.
    ¿Cuál de los siguientes comandos usarías para clonar el repositorio?
    """)
    opciones1 = st.session_state.opciones["q1"]
    respuesta1 = st.radio("Selecciona la respuesta correcta:", opciones1, key="q1_respuesta")
    if st.button("Verificar Respuesta 1", key="q1_btn"):
        verificar_respuesta(respuesta1, "q1")

    # Ejercicio 2
    st.header("Ejercicio 2: Añadir Archivos al Área de Staging")
    st.markdown("""
    Has hecho cambios en un archivo llamado `index.html` y ahora quieres prepararlo para el próximo commit.
    ¿Qué comando usarías para añadir este archivo al área de staging?
    """)
    respuesta2 = st.text_input("Introduce el comando completo:", key="q2_respuesta")
    if st.button("Verificar Respuesta 2", key="q2_btn"):
        verificar_respuesta(respuesta2, "q2")

    # Ejercicio 3
    st.header("Ejercicio 3: Hacer un Commit con un Mensaje")
    st.markdown("""
    Has realizado cambios significativos en el archivo `main.py` y quieres guardar estos cambios con el mensaje 'Añadida nueva función'.
    ¿Cuál es el comando que debes usar?
    """)
    opciones3 = st.session_state.opciones["q3"]
    respuesta3 = st.radio("Selecciona la respuesta correcta:", opciones3, key="q3_respuesta")
    if st.button("Verificar Respuesta 3", key="q3_btn"):
        verificar_respuesta(respuesta3, "q3")

    # Ejercicio 4
    st.header("Ejercicio 4: Ver el Historial de Commits")
    st.markdown("""
    Quieres revisar todos los commits realizados en el repositorio para entender qué cambios se han hecho.
    ¿Qué comando utilizarías para ver el historial de commits?
    """)
    opciones4 = st.session_state.opciones["q4"]
    respuesta4 = st.radio("Selecciona la respuesta correcta:", opciones4, key="q4_respuesta")
    if st.button("Verificar Respuesta 4", key="q4_btn"):
        verificar_respuesta(respuesta4, "q4")

    # Ejercicio 5
    st.header("Ejercicio 5: Guardar Cambios Temporalmente")
    st.markdown("""
    Estás trabajando en una nueva característica pero necesitas cambiar de rama para corregir un error urgente. 
    Quieres guardar tus cambios actuales sin hacer commit. ¿Cuál de los siguientes comandos usarías?
    """)
    opciones5 = st.session_state.opciones["q5"]
    respuesta5 = st.radio("Selecciona la respuesta correcta:", opciones5, key="q5_respuesta")
    if st.button("Verificar Respuesta 5", key="q5_btn"):
        verificar_respuesta(respuesta5, "q5")

    # Ejercicio 6
    st.header("Ejercicio 6: Fusionar Cambios de una Rama")
    st.markdown("""
    Has terminado de trabajar en una rama llamada `feature-x` y quieres fusionar estos cambios a la rama `main`.
    ¿Cuál de los siguientes comandos usarías para hacer la fusión?
    """)
    opciones6 = st.session_state.opciones["q6"]
    respuesta6 = st.radio("Selecciona la respuesta correcta:", opciones6, key="q6_respuesta")
    if st.button("Verificar Respuesta 6", key="q6_btn"):
        verificar_respuesta(respuesta6, "q6")

    # Ejercicio 7
    st.header("Ejercicio 7: Eliminar un Archivo del Repositorio")
    st.markdown("""
    Decidiste que el archivo `deprecated_feature.py` ya no es necesario en el repositorio y quieres eliminarlo.
    ¿Qué comando utilizarías para eliminar este archivo del repositorio?
    """)
    opciones7 = st.session_state.opciones["q7"]
    respuesta7 = st.radio("Selecciona la respuesta correcta:", opciones7, key="q7_respuesta")
    if st.button("Verificar Respuesta 7", key="q7_btn"):
        verificar_respuesta(respuesta7, "q7")

    # Ejercicio 8
    st.header("Ejercicio 8: Ver Cambios entre Commits")
    st.markdown("""
    Necesitas revisar las diferencias entre dos commits específicos en el historial para entender los cambios realizados.
    Supongamos que los commits tienen los siguientes IDs: `abc123` y `def456`. ¿Qué comando utilizarías para comparar estos dos commits?
    """)
    opciones8 = st.session_state.opciones["q8"]
    respuesta8 = st.radio("Selecciona la respuesta correcta:", opciones8, key="q8_respuesta")
    if st.button("Verificar Respuesta 8", key="q8_btn"):
        verificar_respuesta(respuesta8, "q8")

    # Ejercicio 9
    st.header("Ejercicio 9: Subir una Nueva Rama al Repositorio Remoto")
    st.markdown("""
    Has creado una nueva rama local llamada `feature-y` y quieres subirla al repositorio remoto.
    ¿Cuál es el comando que usarías?
    """)
    opciones9 = st.session_state.opciones["q9"]
    respuesta9 = st.radio("Selecciona la respuesta correcta:", opciones9, key="q9_respuesta")
    if st.button("Verificar Respuesta 9", key="q9_btn"):
        verificar_respuesta(respuesta9, "q9")

    # Ejercicio 10
    st.header("Ejercicio 10: Revertir el Último Commit")
    st.markdown("""
    Cometiste un error en el último commit y decides revertirlo. 
    ¿Cuál de los siguientes comandos usarías para deshacer el último commit pero conservar los cambios en el área de staging?
    """)
    opciones10 = st.session_state.opciones["q10"]
    respuesta10 = st.radio("Selecciona la respuesta correcta:", opciones10, key="q10_respuesta")
    if st.button("Verificar Respuesta 10", key="q10_btn"):
        verificar_respuesta(respuesta10, "q10")

    # Resultado Final
    if st.button("Ver Resultado", key="result_btn"):
        puntuacion = (st.session_state.correctas / 10) * 100
        st.write(f"Puntuación: {puntuacion:.2f}%")

        if puntuacion < 50:
            st.error("Lamentablemente, has suspendido el test. Te recomendamos repasar los conceptos básicos de Git.")
        elif puntuacion <= 75:
            st.warning("Has aprobado el test, pero hay margen para mejorar. Sigue estudiando para afianzar tus conocimientos.")
        else:
            st.success("¡Excelente trabajo! Has demostrado un gran dominio de Git. Sigue así.")

# Función para la sección Uso Avanzado de Git

def feedback():
    st.title("Feedback del Taller")
    st.markdown("""
    ¡Gracias por participar en el taller! Nos gustaría conocer tu opinión para poder mejorar futuras ediciones.
    
    ### Preguntas de Feedback
    """)

    # Pregunta 1
    st.subheader("1. ¿Qué te ha parecido el contenido del taller?")
    contenido = st.text_area("Tu respuesta:", key="contenido")

    # Pregunta 2
    st.subheader("2. ¿Hubo algún tema que te resultó especialmente útil o interesante?")
    tema_util = st.text_area("Tu respuesta:", key="tema_util")

    # Pregunta 3
    st.subheader("3. ¿Hay algún aspecto que crees que deberíamos mejorar?")
    mejoras = st.text_area("Tu respuesta:", key="mejoras")

    # Pregunta 4
    st.subheader("4. ¿Te gustaría participar en futuros talleres?")
    futuros_talleres = st.radio("Selecciona una opción:", ["Sí", "No"], key="futuros_talleres")

    # Espacio para otros comentarios
    st.subheader("Otros comentarios")
    otros_comentarios = st.text_area("Tu respuesta:", key="otros_comentarios")

    # Botón para enviar feedback
    if st.button("Enviar Feedback", key="enviar_feedback"):
        st.success("¡Gracias por tu feedback!")
        # Aquí puedes añadir el código para guardar las respuestas (por ejemplo, en una base de datos o archivo)


# Diccionario para la navegación
paginas = {
    "Home": pagina_principal,
    "Comandos Básicos Terminal": comandos_basicos_terminal,
    "Configuración e Inicialización": configuracion_e_inicializacion_git,
    "Operaciones Básicas": operaciones_basicas,
    "Ramas y Colaboración": ramas_colaboracion,
    "Uso Avanzado de Git": avanzado_git,
    "Integración con GitHub": integracion_github,
    "Resumen, Tips y Documentación": resumen_taller,
    "Ejercicios Prácticos": ejercicios,
    "Feedback": feedback
}

# Sidebar para la selección de página
st.sidebar.title("Contenido")
seleccion = st.sidebar.radio("Selecciona una sección", list(paginas.keys()))

# Ejecutar la función correspondiente a la selección de página
paginas[seleccion]()

