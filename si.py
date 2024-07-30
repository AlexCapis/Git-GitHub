import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="Taller Git&GitHub", page_icon=":octopus:", layout="wide")

# Inicio de git, opciones y menus
st.markdown("<h1 style='text-align: center;'>Taller Completo de Git y GitHub</h1>", unsafe_allow_html=True)

# SELECTOR DE TODO EL CONTENIDO
st.sidebar.title("Contenido")
contenido = st.sidebar.radio("Seleccione una sección", ("Home", "Operaciones Básicas", "Ramas y Colaboración", "Uso Avanzado de Git", "Integración con GitHub", "Resumen Taller", "Ejercicios", "Ponte a Prueba", "Feedback"))

if contenido == "Home":
    # st.markdown("<h1 style='text-align: center;'>Taller Completo de Git y GitHub</h1>", unsafe_allow_html=True) 
    st.image("./img/git_image.png")
    st.header("Bienvenido al Taller Completo de Git y GitHub")
    st.markdown("""
    En este taller, aprenderás los conceptos fundamentales y avanzados de Git y GitHub, herramientas esenciales para el desarrollo colaborativo y el control de versiones. 

    ### ¿Qué aprenderás?
    - **Operaciones Básicas con Git**: Cómo clonar repositorios, añadir y eliminar archivos, hacer commits y ver el historial.
    - **Ramas y Colaboración**: Cómo crear y gestionar ramas, realizar merges y resolver conflictos, y estrategias de colaboración en proyectos.
    - **Uso Avanzado de Git**: Técnicas avanzadas como rebase, stash, y cherry-pick para mejorar tu flujo de trabajo.
    - **Integración con GitHub**: Cómo conectar repositorios locales con GitHub, realizar push y pull requests, y colaborar eficazmente en GitHub.
    - **Ejercicios y Quizzes Dinámicos**: Preguntas interactivas, ejercicios prácticos y casos de estudio simulados para aplicar y evaluar tus conocimientos.

    ¡Esperamos que disfrutes del taller y que te conviertas en un experto en Git y GitHub!
    """)


if contenido == "Operaciones Básicas":
    st.title("Operaciones Básicas con Git")
    st.markdown("""
    En esta sección, cubriremos las operaciones básicas que puedes realizar con Git, incluyendo cómo clonar repositorios, añadir y eliminar archivos, y cómo hacer commits y ver el historial.

    ### ¿Qué es Git?
    Git es un sistema de control de versiones distribuido que te permite rastrear cambios en tus archivos y colaborar con otros desarrolladores. Es una herramienta esencial en el desarrollo de software moderno.

    **Beneficios de Git:**
    - **Distribución**: Cada desarrollador tiene una copia completa del historial del proyecto, lo que facilita el trabajo sin conexión y mejora la seguridad.
    - **Velocidad**: Optimizado para rendimiento, Git maneja grandes proyectos de forma rápida y eficiente.
    - **Colaboración**: Facilita la colaboración entre múltiples desarrolladores, permitiendo trabajar en paralelo y fusionar cambios de manera efectiva.

    ### Contenido
    1. 📂 **Clonar Repositorios**
    2. ✏️ **Añadir y Eliminar Archivos**
    3. 📜 **Hacer Commits y Ver Historial**
    """)

    # st.image("path/to/your/image.png", caption="Git: Sistema de Control de Versiones Distribuido")

    st.markdown("""
    ### Clonar Repositorios
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

    Ejemplo: Para clonar el repositorio `Git` de GitHub, usa el comando:
    ```bash
    git clone https://github.com/AlexCapis/Git.git
    ```

    #### ¿Qué Ocurre Después de Clonar?
    - **Creación de un Directorio Local**: Se crea una carpeta con el nombre del repositorio.
    - **Copia del Historial Completo**: Todo el historial de cambios es copiado a tu máquina local.
    - **Configuración de Orígenes Remotos**: El repositorio clonado estará vinculado al origen remoto de donde se clonó.

    #### Visualización del Proceso
    ![Clonar un repositorio](https://example.com/path/to/clone_image.png) ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

    📌 **Tip:** Si el repositorio es privado, necesitarás autenticación (nombre de usuario y contraseña, token de acceso, etc.) para clonar.

    **Beneficios de Clonar Correctamente**
    - **Sincronización Fácil**: Puedes sincronizar tu copia local con los cambios más recientes del repositorio remoto.
    - **Desarrollo y Pruebas Locales**: Puedes probar y desarrollar nuevas funcionalidades en tu entorno local sin afectar a otros colaboradores.

    **Resumen del Comando Clonado**
    ```bash
    git clone <URL-del-repositorio>
    ```
    - **`git clone`**: Comando para clonar repositorios.
    - **`<URL-del-repositorio>`**: La URL del repositorio remoto que deseas clonar.

    ¡Ahora estás listo para comenzar a trabajar con Git clonando repositorios de manera efectiva!
    """)



    st.markdown("""
        ### Añadir y Eliminar Archivos
        Git te permite añadir nuevos archivos a tu repositorio y eliminar los que ya no necesitas. Esto te ayuda a gestionar los cambios y mantener tu proyecto limpio y organizado.
    """)

    st.markdown("""
        #### ¿Qué es el Área de Staging?
        El área de staging es una zona intermedia donde se almacenan los cambios que quieres confirmar en el próximo commit. Esto te permite preparar y revisar los cambios antes de hacerlos permanentes.
    """)

    st.image("https://example.com/path/to/staging_area_image.png", caption="Flujo del área de staging en Git")

    st.markdown("""
        #### Añadir Archivos al Repositorio
        Para añadir nuevos archivos al área de staging, utiliza el comando `git add`.
    """)

    st.code("git add <archivo>", language='bash')

    st.markdown("Ejemplo: Añade un nuevo archivo al área de staging:")
    st.code("git add nuevo-archivo.txt", language='bash')

    st.markdown("""
        #### Eliminar Archivos del Repositorio
        Para eliminar un archivo del repositorio y del área de staging, usa el comando `git rm`.
    """)

    st.code("git rm <archivo>", language='bash')

    st.markdown("Ejemplo: Elimina un archivo específico:")
    st.code("git rm archivo-a-eliminar.txt", language='bash')

    st.markdown("📌 **Tip:** Si te encuentras con un error, verifica que el archivo que estás intentando añadir o eliminar existe y que tienes los permisos adecuados.")



    st.markdown("""
        ### Hacer Commits y Ver Historial
        Realizar commits es una de las funciones más importantes de Git, ya que te permite guardar el estado de tu proyecto en un punto específico en el tiempo. También puedes ver el historial de commits para rastrear los cambios realizados y entender cómo ha evolucionado tu proyecto.
    """)

    st.markdown("""
        #### Hacer un Commit
        Para guardar los cambios en el repositorio, usa el comando `git commit` con un mensaje descriptivo.
    """)

    st.code("git commit -m \"Mensaje del commit\"", language='bash')

    st.markdown("Ejemplo: Guarda tus cambios con un mensaje descriptivo:")
    st.code("git commit -m \"Añadido nuevo archivo de configuración\"", language='bash')

    st.markdown("""
        #### Ver el Historial de Commits
        Para ver el historial de commits, utiliza el comando `git log`.
    """)

    st.code("git log", language='bash')

    st.markdown("Ejemplo: Muestra el historial de commits en tu terminal:")
    st.code("git log", language='bash')

    st.markdown("📌 **Tip:** Usa `git log --oneline` para ver un historial más compacto y legible.")






    # Título de la sección
    st.markdown("### Resumen de Comandos Básicos")

    # Crear un DataFrame para la tabla de comandos
    data = {
        "Comando": [
            "`git clone <URL>`",
            "`git add <archivo>`",
            "`git rm <archivo>`",
            "`git commit -m \"mensaje\"`",
            "`git log`"
        ],
        "Descripción": [
            "Clona un repositorio",
            "Añade un archivo al área de staging",
            "Elimina un archivo del repositorio",
            "Guarda los cambios con un mensaje",
            "Muestra el historial de commits"
        ]
    }

    df = pd.DataFrame(data)

    # Mostrar la tabla usando Streamlit
    st.table(df)

    # Mensaje adicional
    st.markdown("""
    ¡Con estos comandos básicos, ya puedes comenzar a trabajar con Git y gestionar tu código de manera efectiva!
    """)

    st.markdown("""
    ### Resumen de Comandos Básicos
    Aquí tienes un resumen de los comandos básicos que hemos cubierto:

    | Comando                     | Descripción                           |
    |-----------------------------|---------------------------------------|
    | `git clone <URL>`           | Clona un repositorio                  |
    | `git add <archivo>`         | Añade un archivo al área de staging   |
    | `git rm <archivo>`          | Elimina un archivo del repositorio    |
    | `git commit -m "mensaje"`   | Guarda los cambios con un mensaje     |
    | `git log`                   | Muestra el historial de commits       |

    ¡Con estos comandos básicos, ya puedes comenzar a trabajar con Git y gestionar tu código de manera efectiva!
    """)






if contenido == "Ramas y Colaboración":
    st.markdown("## Ramas y Colaboración")
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

    Ejemplo:
    ```bash
    git branch feature-nueva
    ```

    #### Cambiar a una Rama Diferente
    Para cambiar a una rama existente, utiliza:
    ```bash
    git checkout <nombre-de-la-rama>
    ```

    Ejemplo:
    ```bash
    git checkout feature-nueva
    ```

    #### Ver todas las Ramas
    Puedes listar todas las ramas en tu repositorio con:
    ```bash
    git branch
    ```

    📌 **Tip:** Usa ramas descriptivas para mantener tu proyecto organizado.
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

    Ejemplo:
    ```bash
    git merge feature-nueva
    ```

    #### Resolver Conflictos
    Si Git encuentra cambios conflictivos, te pedirá que los resuelvas manualmente. Abre los archivos conflictivos, edita y guarda los cambios, y luego añade los archivos resueltos al área de staging:
    ```bash
    git add <archivo-conflictivo>
    ```

    Una vez resueltos todos los conflictos, realiza el commit:
    ```bash
    git commit -m "Resolver conflictos de merge"
    ```

    📌 **Tip:** Usa herramientas de merge como `kdiff3`, `meld`, o editores como VS Code para facilitar la resolución de conflictos.
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

    st.markdown("""
    ¡Con estas estrategias y comandos, estarás listo para colaborar efectivamente y gestionar tus ramas en Git!
    """)



    # Título de la sección
    st.markdown("### Resumen de Comandos para Ramas y Colaboración")

    # Crear un DataFrame para la tabla de comandos
    data = {
        "Comando": [
            "`git branch <nombre-de-la-rama>`",
            "`git checkout <nombre-de-la-rama>`",
            "`git branch`",
            "`git checkout main`",
            "`git merge <nombre-de-la-rama>`",
            "`git add <archivo-conflictivo>`",
            "`git commit -m \"Resolver conflictos de merge\"`"
        ],
        "Descripción": [
            "Crea una nueva rama",
            "Cambia a una rama diferente",
            "Ver todas las ramas",
            "Cambiar a la rama principal (o la rama destino del merge)",
            "Realizar un merge",
            "Añadir archivos conflictivos resueltos al área de staging",
            "Guardar los cambios después de resolver conflictos de merge"
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


import streamlit as st
import pandas as pd

if contenido == "Uso Avanzado de Git":
    st.markdown("## Uso Avanzado de Git")
    st.markdown("""
    En esta sección, exploraremos técnicas avanzadas como rebase, stash y cherry-pick para mejorar tu flujo de trabajo. Estas herramientas te permiten mantener un historial de commits limpio y manejar cambios de forma eficiente.

    ### Contenido
    1. 🔄 **Rebase**
    2. 🗂️ **Stash**
    3. 🍒 **Cherry-Pick**

    ### Rebase
    Rebase te permite reescribir el historial de commits, haciendo que tu historia de commits sea más lineal y fácil de seguir.

    #### Comando de Rebase
    ```bash
    git rebase <rama-base>
    ```

    Ejemplo:
    ```bash
    git rebase main
    ```

    📌 **Tip:** Utiliza `rebase` en vez de `merge` para mantener un historial de commits más limpio.

    ### Stash
    Stash guarda temporalmente tus cambios sin hacer un commit, lo que te permite cambiar de ramas sin perder tu trabajo.

    #### Comando de Stash
    ```bash
    git stash
    ```

    Para aplicar los cambios guardados:
    ```bash
    git stash apply
    ```

    📌 **Tip:** Usa `git stash list` para ver todos los stashes guardados y `git stash pop` para aplicar y eliminar el stash.

    ### Cherry-Pick
    Cherry-pick te permite aplicar cambios de commits específicos a tu rama actual, sin necesidad de hacer un merge completo.

    #### Comando de Cherry-Pick
    ```bash
    git cherry-pick <id-del-commit>
    ```

    Ejemplo:
    ```bash
    git cherry-pick a1b2c3d4
    ```

    📌 **Tip:** Ideal para aplicar hotfixes en ramas de producción sin mezclar cambios innecesarios.
    """)

    # Resumen de Comandos
    st.markdown("### Resumen de Comandos Avanzados")

    data = {
        "Comando": [
            "`git rebase <rama-base>`",
            "`git stash`",
            "`git stash apply`",
            "`git cherry-pick <id-del-commit>`"
        ],
        "Descripción": [
            "Reescribe el historial de commits",
            "Guarda temporalmente tus cambios",
            "Aplica los cambios guardados con stash",
            "Aplica cambios de un commit específico"
        ]
    }

    df = pd.DataFrame(data)
    st.table(df)




if contenido == "Integración con GitHub":
    st.markdown("## Integración con GitHub")
    st.markdown("""
    En esta sección, aprenderás cómo integrar tu repositorio local con GitHub, manejar pull requests y trabajar con GitHub Actions.

    ### Contenido
    1. 🌐 **Conectar Repositorio Local a GitHub**
    2. 🚀 **Pull Requests**
    3. ⚙️ **GitHub Actions**

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

    Ejemplo:
    ```bash
    git remote add origin https://github.com/usuario/repositorio.git
    git branch -M main
    git push -u origin main
    ```

    📌 **Tip:** Asegúrate de reemplazar `<URL-del-repositorio>` con la URL de tu repositorio en GitHub.

    ### Pull Requests
    Las pull requests te permiten proponer cambios en el código que pueden ser revisados y fusionados por otros colaboradores.

    #### Crear una Pull Request
    1. Haz commits de tus cambios en una nueva rama.
    2. Sube tu rama a GitHub:
    ```bash
    git push origin <nombre-de-la-rama>
    ```
    3. En GitHub, ve a la página de tu repositorio y haz clic en "Compare & pull request".
    4. Rellena los detalles necesarios y haz clic en "Create pull request".

    ### GitHub Actions
    GitHub Actions te permite automatizar flujos de trabajo como la construcción, prueba y despliegue de tu código.

    #### Crear un Workflow de GitHub Actions
    1. En tu repositorio de GitHub, ve a la pestaña "Actions".
    2. Selecciona un flujo de trabajo predefinido o crea uno nuevo.
    3. Sigue las instrucciones para configurar el flujo de trabajo.

    Ejemplo de archivo YAML para un workflow simple:
    ```yaml
    name: CI

    on:
      push:
        branches: [ main ]
      pull_request:
        branches: [ main ]

    jobs:
      build:

        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v2
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.x'
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
        - name: Run tests
          run: |
            pytest
    ```

    📌 **Tip:** Adapta el archivo YAML a las necesidades específicas de tu proyecto.

    """)

    # Resumen de Comandos
    st.markdown("### Resumen de Comandos de Integración en GitHub")

    data = {
        "Comando": [
            "`git remote add origin <URL-del-repositorio>`",
            "`git branch -M main`",
            "`git push -u origin main`",
            "`git push origin <nombre-de-la-rama>`"
        ],
        "Descripción": [
            "Conecta el repositorio local con el remoto en GitHub",
            "Renombra la rama actual a 'main'",
            "Sube la rama 'main' al repositorio remoto y establece el seguimiento",
            "Sube la rama especificada al repositorio remoto"
        ]
    }

    df = pd.DataFrame(data)
    st.table(df)



# Función para verificar las respuestas
def verificar_respuesta(respuesta, correcta):
    if respuesta.strip() == correcta:
        st.success("¡Correcto!")
    else:
        st.error(f"Incorrecto. La respuesta correcta es `{correcta}`.")

# Función principal
def main():
    # Título de la página
    st.title("Ejercicios de Git")

        # Pregunta 1
    st.header("Pregunta 1: ¿Cuál es el comando para clonar un repositorio?")
    respuesta1 = st.text_input("Introduce el comando completo:")
    if st.button("Verificar Respuesta 1", key="q1"): # Cambia la clave a "q1"
        verificar_respuesta(respuesta1, "git clone <URL>")

    # Pregunta 2
    st.header("Pregunta 2: ¿Cómo añades un archivo al área de staging?")
    respuesta2 = st.radio("Selecciona la respuesta correcta:", 
                            ["git add <archivo>", "git commit <archivo>", "git push <archivo>"])
    if st.button("Verificar Respuesta 2", key="q2"): # Cambia la clave a "q2"
        verificar_respuesta(respuesta2, "git add <archivo>")

    # Pregunta 3
    st.header("Pregunta 3: ¿Cuál es el comando para guardar cambios en el repositorio con un mensaje?")
    respuesta3 = st.text_input("Introduce el comando completo:")
    if st.button("Verificar Respuesta 3", key="q3"): # Cambia la clave a "q3"
        verificar_respuesta(respuesta3, 'git commit -m "mensaje"')

    # Pregunta 4
    st.header("Pregunta 4: ¿Qué comando se usa para ver el historial de commits?")
    respuesta4 = st.radio("Selecciona la respuesta correcta:", 
                            ["git log", "git status", "git history"])
    if st.button("Verificar Respuesta 4", key="q4"): # Cambia la clave a "q4"
        verificar_respuesta(respuesta4, "git log")

    # Pregunta 5
    st.header("Pregunta 5: ¿Cómo guardas temporalmente tus cambios sin hacer commit?")
    respuesta5 = st.text_input("Introduce el comando completo:", key="q5")
    if st.button("Verificar Respuesta 5", key="q5"): # Cambia la clave a "q5"
        verificar_respuesta(respuesta5, "git stash")
if __name__ == "__main__":
    main()


elif contenido == "Feedback":
    st.title("Feedback del Taller")
    st.markdown("""
    ¡Gracias por participar en el taller! Nos gustaría conocer tu opinión para poder mejorar futuras ediciones.

    ### Preguntas de Feedback
    1. ¿Qué te ha parecido el contenido del taller?
    2. ¿Hubo algún tema que te resultó especialmente útil o interesante?
    3. ¿Hay algún aspecto que crees que deberíamos mejorar?
    4. ¿Te gustaría participar en futuros talleres sobre Git y GitHub?

    Puedes enviar tus respuestas a estas preguntas y cualquier otro comentario que tengas a [nuestro correo electrónico](mailto:contacto@taller.com).

    ¡Gracias por tu tiempo y tus comentarios!
    """)















