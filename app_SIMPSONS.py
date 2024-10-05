import streamlit as st
import os
import pandas as pd


# Configuración de la página
st.set_page_config(page_title="Taller de Git con Los Simpsons", page_icon="::", layout="wide")

# Función para verificar las respuestas
def verificar_respuesta(respuesta, correcta):
    if respuesta.strip() == correcta:
        st.success("¡Correcto!")
    else:
        st.error(f"Incorrecto. La respuesta correcta es `{correcta}`.")

# Función para la página principal
def pagina_principal():
    # Título y bienvenida
    st.markdown("<h1 style='text-align: center;'>¡Bienvenidos al Taller de Git con Los Simpsons!</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center;'>
        <img src='https://upload.wikimedia.org/wikipedia/en/a/a0/The_Simpsons_-_logo.png' width='400'>
    </div>
    """, unsafe_allow_html=True)
    
    # Historia de introducción
    st.markdown("""
    ### ¡Bienvenidos a Springfield!

    Springfield está revolucionado porque Homer ha sido nombrado el nuevo encargado del control de versiones en la Planta Nuclear... ¡y no tiene ni idea de cómo funciona Git! Pero no te preocupes, porque Lisa está aquí para asegurarse de que no cause un desastre que borre todo el código... de nuevo.

    En este taller de Git, los personajes de Los Simpsons te enseñarán cómo dominar el control de versiones mientras intentan salvar el día en Springfield. ¡Vamos a aprender Git de la manera más divertida posible!

    **¿Cómo funciona esto?**  
    - Homer añadirá commits de forma caótica y aleatoria, pero tú aprenderás a hacerlo de forma correcta.
    - Marge te ayudará a organizar tu proyecto con la misma dedicación con la que limpia la casa, y sin olvidarse de ninguna rama.
    - Bart te mostrará cómo crear y destruir ramas con su usual anarquía, pero también aprenderás cómo hacerlo bien y no dejar un caos tras de ti.
    - Lisa te enseñará a ser eficiente, meticuloso y perfecto con tu código... aunque seguro que Homer no sigue todas sus recomendaciones.

    ### Menú de Navegación

    - **Comandos Básicos con Ralph Wiggum**: "Hola, ¡Hola, soy Ralph! No te preocupes, aprenderemos lo básico del terminal. ¡No habrá nada raro como una cebolla en el parque, lo prometo!
                
    - **Configuración e Inicialización con Marge**: "Hola, soy Marge. Configurar Git es como organizar la despensa: una vez que todo está en su sitio, la vida es mucho más fácil. ¡Vamos a evitar que Homer borre todo accidentalmente!"
    
    - **Operaciones Básicas con Milhouse**: "¡Hey, soy Milhouse! A lo mejor no soy el más popular del colegio, pero cuando se trata de Git, ¡puedo enseñarte algunos trucos geniales! Solo prometo no llorar si algo sale mal."
    
    - **Ramas y Colaboración con Bart**: "¡Yo soy el Barto! Vamos a liarla con unas cuantas ramas de Git, pero no te preocupes, ¡Lisa nos salvará antes de que se nos vaya todo de las manos!"
    
    - **Uso Avanzado de Git con Lisa**: "Soy Lisa Simpson y, como siempre, me toca poner un poco de orden. Aprenderemos técnicas avanzadas para que tu proyecto sea tan eficiente como mi saxofón los domingos por la tarde."
    
    - **Integración con GitHub con Ned Flanders**: "¡Hola holita, vecinitos! Integrar Git con GitHub es más fácil que una limonada bien fresquita en una tarde de verano. ¡Nada complicado, lo prometo!"
    
    - **Resumen del Taller con Nelson Muntz**: "Ha-ha! Soy Nelson y aquí no te escapas sin aprender Git. Repasaremos todo lo que hemos visto porque, ¡eh!, si hasta Milhouse ha aprendido, tú también puedes."
    
    - **Ejercicios Prácticos con Apu**: "¡Gracias, vuelve pronto! Soy Apu, y no te preocupes, te tengo preparado un surtido de ejercicios prácticos para que domines Git mejor que los precios en el Badulaque."
    
    - **Feedback con Maggie**: Incluso Maggie tiene algo que decir, ¿por qué no tú? ¡Tu feedback es valioso! Déjanos tus comentarios y sugerencias para que podamos mejorar y hacer que este taller sea todavía más increíble.
                
    ¡Estamos emocionados de que te unas a nosotros en esta aventura Git al estilo de Springfield! Y recuerda, como diría Homer: "En caso de duda, ¡haz un commit!" 🍩
    """)







def comandos_basicos_terminal():
    st.title("Comandos Básicos de Terminal con Ralph Wiggum: ¡Donde la Terminal es Magia!")
    st.markdown("""
    Bienvenido a esta clase especial de comandos de terminal, ¡guiada por el mismísimo Ralph Wiggum! Si Ralph puede aprender esto (aunque piense que la terminal es un dinosaurio), tú también puedes. ¡Prepárate para aprender con ejemplos ridículos y divertidos al estilo de Springfield!

    ### Contenido
    1. 🦖 **Navegación y Listado de Archivos con Ralph el Explorador**
    2. 🏗️ **Gestión de Directorios: Construyendo la Casa de la Familia Simpson**
    3. 📦 **Gestión de Archivos con Bart y sus Bromas**
    """)

    st.markdown("### 1. 🦖 Navegación y Listado de Archivos con Ralph el Explorador")
    st.markdown("""
    Ralph ha encontrado un fósil... o eso cree. En realidad, está intentando listar los archivos de su ordenador porque piensa que ahí vive el dinosaurio. Vamos a ayudarle a entender cómo funciona.

    #### Listar Archivos y Directorios (¡Buscando Dinosaurios!)
    Ralph se pregunta: "¿Dónde están mis dinosaurios?". Para listar lo que hay en el directorio actual, usa el siguiente comando:
    ```bash
    ls
    ```

    **Ejemplo:** Ralph quiere ver qué hay en su carpeta de dinosaurios:
    ```bash
    $ ls
    raptor.txt  tiranosaurio.jpg  velociraptor_cosas.txt  rosquillas.txt
    ```
    Ralph se da cuenta de que no solo hay dinosaurios, ¡también hay rosquillas! Ahora está en una encrucijada: ¿buscar más dinosaurios o comerse una rosquilla? 🤷‍♂️

    #### Mostrar la Ruta del Directorio Actual (¡Para no Perderse!)
    Ralph suele perderse con facilidad, pero con este comando puede saber exactamente dónde está:
    ```bash
    pwd
    ```

    **Ejemplo:** Ralph quiere saber en qué carpeta está:
    ```bash
    $ pwd
    /home/springfield/dinosaurios
    ```
    Ralph descubre que está en la carpeta de dinosaurios y no en la cocina de los Simpson, como pensaba. Así evita volver a perderse... al menos por ahora.

    #### Cambiar de Directorio (¡Explorando Otras Zonas!)
    Ralph decide que necesita ir a la carpeta de `rosquillas` porque tiene hambre. Para cambiar de directorio, se usa este comando:
    ```bash
    cd <nombre-del-directorio>
    ```

    **Ejemplo:** Ralph quiere ir a la carpeta `rosquillas`:
    ```bash
    $ cd rosquillas
    $ pwd
    /home/springfield/rosquillas
    ```
    Ralph ha llegado a la carpeta correcta y ahora puede disfrutar de sus rosquillas... hasta que Homer las descubra.

    📌 **Tip de Lisa:** Ralph, si alguna vez te pierdes de nuevo, recuerda que puedes "subir" a la carpeta anterior usando `cd ..`. Así es como funciona:
    
    **Ejemplo:** Si Ralph está en la carpeta `rosquillas` pero quiere volver a la carpeta `springfield`:
    ```bash
    $ cd ..
    $ pwd
    /home/springfield
    ```
    ¡Enhorabuena, Ralph! Has vuelto a la carpeta `springfield` sano y salvo. Ahora puedes seguir buscando dinosaurios... o más rosquillas.
    """)

    # Imagen recomendada:
    # **Ubicación**: Justo después de la primera sección de Ralph el Explorador.
    # **Contenido**: Ralph con una lupa buscando "dinosaurios" en su computadora, y al fondo, un dinosaurio falso hecho de archivos en una carpeta. Puedes incluir en la imagen algo que luzca como un monitor antiguo de los Simpson.
    
    st.markdown("### 2. 🏗️ Gestión de Directorios: Construyendo la Casa de los Simpson")
    st.markdown("""
    Ralph ha decidido que quiere ayudar a construir una nueva casa para los Simpson. Aunque su sentido de la arquitectura es un poco... peculiar, vamos a guiarlo en este proceso. Usaremos comandos de terminal para crear y gestionar directorios, como si estuviéramos levantando las habitaciones de la casa de los Simpson.

    #### Crear un Nuevo Directorio (¡Construyendo la Habitación de Bart!)
    Ralph está muy emocionado. Su primera misión es construir una habitación especial para Bart, donde pueda esconder todas sus travesuras (y de paso, evitar que Homer lo pille). Utiliza este comando para crear un nuevo directorio (que Ralph imagina como la habitación de Bart):
    ```bash
    mkdir <nombre-del-directorio>
    ```

    **Ejemplo:** Ralph crea la habitación de Bart, donde podrá guardar todas sus bromas y juguetes:
    ```bash
    $ mkdir habitacion_de_bart
    $ ls
    dinosaurios  rosquillas  habitacion_de_bart
    ```
    ¡Ralph ha creado una nueva habitación en la casa! Bart ahora tiene su espacio propio para hacer travesuras sin molestar a Lisa... al menos por ahora.

    #### Crear Otras Habitaciones (¡La Casa Sigue Creciendo!)
    Ralph está en racha y decide que todos los Simpson necesitan su propia habitación. Ahora quiere construir una habitación para Lisa, otra para Homer (¡cerca de la nevera, claro!) y una para Maggie.

    **Ejemplo:** Ralph construye las demás habitaciones:
    ```bash
    $ mkdir habitacion_de_lisa
    $ mkdir habitacion_de_homer_marge
    $ mkdir habitacion_de_maggie
    $ ls
    dinosaurios  rosquillas  habitacion_de_bart  habitacion_de_lisa  habitacion_de_homer_marge  habitacion_de_maggie
    ```
    La casa de los Simpson está tomando forma, y Ralph no podría estar más orgulloso.

    #### Eliminar un Directorio (¡Ups, Ralph Derriba una Habitación por Error!)
    Ralph, en su entusiasmo, construyó una habitación para el dinosaurio sin darse cuenta de que no era realmente necesaria. Ahora debe derribarla. Para eliminar un directorio (o "derribar una habitación", según Ralph), usa este comando:
    ```bash
    rm -r <nombre-del-directorio>
    ```

    **Ejemplo:** Ralph derriba la habitación del dinosaurio:
    ```bash
    $ rm -r dinosaurios
    $ ls
    rosquillas  habitacion_de_bart  habitacion_de_lisa  habitacion_de_homer_marge  habitacion_de_maggie
    ```
    La habitación del dinosaurio ya no está, pero Ralph sigue adelante con su proyecto.

    #### Advertencia de Marge: ¡Cuidado al Demoler Habitaciones!
    Marge se acerca a Ralph y le advierte que tenga cuidado al usar comandos para eliminar directorios. Es como cuando Homer entra a la cocina: si no tienes cuidado, todo podría desaparecer en un abrir y cerrar de ojos.

    📌 **Advertencia de Marge:** No uses `rm -rf` sin pensarlo dos veces, ya que podrías borrar toda la casa digital de los Simpson (¡como cuando Homer se come una tarta entera en segundos!). Asegúrate de estar en el directorio correcto antes de borrar algo importante.

    #### Ejemplo de lo que NO debes hacer:
    Ralph está a punto de cometer un error. Intenta borrar la habitación de Homer, pero accidentalmente se encuentra en el directorio principal de la casa. Al usar `rm -rf *`, ¡podría borrar toda la casa de los Simpson!

    **Ejemplo Incorrecto:**
    ```bash
    $ rm -rf *
    ```

    Si Ralph ejecuta este comando desde el directorio principal, todos los archivos y directorios de la casa serán eliminados.

    **Resultado:**
    ```bash
    $ ls
    (nada...)
    ```
    ¡Oh no! Ralph ha borrado toda la casa de los Simpson por accidente. Marge se enfada, y Homer se queda sin su habitación y sin su preciada nevera.

    **Lección:** Asegúrate siempre de estar en el directorio correcto antes de eliminar algo. Un paso en falso puede tener consecuencias desastrosas.
    """)



    # Imagen recomendada:
    # **Ubicación**: Después de la sección de construir directorios.
    # **Contenido**: Una casa de los Simpson siendo construida digitalmente, con Ralph y Bart trabajando juntos. Ralph podría estar usando comandos, y Bart preparando alguna travesura en una carpeta. Añade detalles divertidos como una habitación que Homer ha demolido por accidente.

    st.markdown("### 3. 📦 Gestión de Archivos con Bart y Sus Bromas: Ralph Aprende a Ser Travieso")
    st.markdown("""
    Ralph ha encontrado a su nuevo mejor amigo y socio de travesuras: ¡Bart Simpson! Bart es un experto en hacer bromas a la gente de Springfield, y ahora Ralph quiere aprender a hacer bromas usando la terminal. Vamos a enseñar a Ralph y Bart cómo gestionar archivos mientras preparan sus travesuras.

    #### Crear un Nuevo Archivo (¡Bart y Ralph Preparan una Broma!)
    Bart le muestra a Ralph cómo crear archivos para sus bromas. Utilizan el siguiente comando para crear un archivo vacío, donde escribirán sus ideas de bromas:
    ```bash
    touch <nombre-del-archivo>
    ```

    **Ejemplo:** Bart y Ralph crean un archivo llamado `broma_homer.txt`:
    ```bash
    $ touch broma_homer.txt
    $ ls
    broma_homero.txt  travesuras_de_bart  dinosaurios  rosquillas
    ```
    Ahora tienen un archivo listo para llenarlo de ideas graciosas. Ralph está emocionado porque Homer ni siquiera sospechará de la broma que están planeando.

    #### Eliminar un Archivo (¡Bart y Ralph Borran las Evidencias!)
    Después de que una de sus bromas se sale de control (como suele pasar cuando Ralph está involucrado), necesitan borrar las pruebas rápidamente. Bart le enseña a Ralph cómo eliminar archivos para no ser atrapados:
    ```bash
    rm <nombre-del-archivo>
    ```

    **Ejemplo:** Bart y Ralph eliminan el archivo `broma_homer.txt` para que Homer no descubra su plan:
    ```bash
    $ rm broma_homer.txt
    $ ls
    travesuras_de_bart  dinosaurios  rosquillas
    ```
    ¡Uf! El archivo ha sido eliminado justo a tiempo. Ralph suspira aliviado porque no quiere que Homer lo descubra.

    #### Copiar un Archivo (¡Bart y Ralph Multiplican Sus Bromas!)
    Bart le explica a Ralph cómo copiar un archivo para que las bromas puedan expandirse por todo Springfield. Usan este comando para copiar sus archivos de broma:
    ```bash
    cp <archivo_origen> <archivo_destino>
    ```

    **Ejemplo:** Bart y Ralph copian la broma de Homer para asegurarse de que llegue a todos los rincones de la casa:
    ```bash
    $ cp broma_homer.txt broma_homer_copia.txt
    $ ls
    broma_homer.txt  broma_homer_copia.txt  travesuras_de_bart  dinosaurios
    ```
    ¡Misión cumplida! Ahora tienen copias de su broma en varios lugares, por si alguna se pierde en el camino. Ralph sonríe porque es más probable que la broma funcione.

    #### Mover un Archivo (¡Bart y Ralph Ocultan las Bromas!)
    Ralph quiere esconder sus bromas y Bart le enseña a usar `mv` para mover los archivos a nuevos lugares, como cuando Bart esconde su tirachinas en la nevera:
    ```bash
    mv <archivo_origen> <destino>
    ```

    **Ejemplo:** Bart y Ralph mueven el archivo de broma de Homer a otro lugar en la casa para confundirlo aún más:
    ```bash
    $ mv broma_homer.txt /casa_de_los_simpson/nevera/
    $ ls
    broma_homer_copia.txt  travesuras_de_bart  dinosaurios
    ```
    ¡Perfecto! El archivo ha sido movido a un lugar secreto. Ahora Homero jamás encontrará el archivo de la broma.

    📌 **Tip de Bart:** ¡Siempre es divertido mover los archivos! Solo asegúrate de recordar dónde los dejaste, o podrías perderlos para siempre...
                

     #### Leer el Contenido de un Archivo (¡Ralph Leeendo las Ideas de Bart!)
    Bart quiere mostrarle a Ralph sus ideas de bromas, así que usa el siguiente comando para leer el contenido del archivo:
    ```bash
    cat <nombre-del-archivo>
    ```

    **Ejemplo:** Bart lee el contenido de su archivo de travesuras:
    ```bash
    $ cat travesuras_de_bart
    - Poner una bomba de ruido en la nevera de Homer.
    - Cambiar el shampoo de Lisa por pegamento.
    ```
    Ralph se ríe a carcajadas y ya está pensando en cómo llevar a cabo algunas de estas ideas locas.

    **Conclusión:** Así es como Ralph y Bart aprenden a gestionar archivos mientras planifican travesuras en Springfield.¡Que se preparen los vecinos de Springfield! 🎉
    """)               



    # Imagen recomendada:
    # **Ubicación**: Al final de la sección de gestión de archivos.
    # **Contenido**: Bart trabajando en su computadora creando archivos con nombres divertidos y copiándolos por todas partes. Podría haber una pantalla mostrando las bromas, y Homero al fondo, ajeno a lo que ocurre.
    
    st.markdown("""
    ## Resumen de Comandos
    A continuación, se presenta un resumen de los comandos básicos de la terminal en formato de tabla, inspirado en las locuras de Springfield. ¡Porque aprender puede ser divertido!
    """)
      # Resumen de comandos
    comandos = [
        {"Comando": "ls", "Descripción": "Lista los archivos en el directorio actual (Ralph busca dinosaurios)."},
        {"Comando": "pwd", "Descripción": "Muestra la ruta del directorio actual (Ralph se asegura de no perderse)."},
        {"Comando": "cd <directorio>", "Descripción": "Cambia de directorio (Ralph va a buscar más rosquillas)."},
        {"Comando": "mkdir <nombre>", "Descripción": "Crea un nuevo directorio (Ralph construye nuevas habitaciones)."},
        {"Comando": "rm -r <directorio>", "Descripción": "Elimina un directorio (Ralph derriba una habitación por error)."},
        {"Comando": "rm -rf *", "Descripción": "Elimina todo en el directorio actual (Ralph derriba todo como un tornado)."},
        {"Comando": "touch <archivo>", "Descripción": "Crea un nuevo archivo vacío (Bart y Ralph preparan una broma)."},
        {"Comando": "rm <archivo>", "Descripción": "Elimina un archivo (Bart y Ralph borran las pruebas)."},
        {"Comando": "cp <origen> <destino>", "Descripción": "Copia un archivo (Bart y Ralph multiplican sus bromas)."},
        {"Comando": "mv <origen> <destino>", "Descripción": "Mueve o renombra un archivo (Bart y Ralph cambian el nombre de su última broma)."},
        {"Comando": "cat <archivo>", "Descripción": "Muestra el contenido de un archivo (Ralph lee las ideas de Bart)."},
    ]

    df_comandos = pd.DataFrame(comandos)
    st.dataframe(df_comandos)

    st.markdown("""
    Con estos comandos, ¡serás tan eficiente como Bart organizando sus bromas o Ralph buscando dinosaurios! Practica y diviértete con la terminal. Si Ralph puede aprender, tú también puedes hacerlo.
    """)




def configuracion_e_inicializacion_git():
    st.title("Configuración e Inicialización de Git con Marge")
    st.markdown("""
    ¡Hola, amigos! Soy Marge Simpson, y hoy te llevaré a un viaje en el tiempo y el espacio, a través de las complejidades del mundo de Git. Piensa en esto como una de esas aventuras locas que la familia Simpson suele tener, pero esta vez, no se trata de evitar que Bart se cuela en la tienda de donuts, sino de asegurarnos de que tus proyectos digitales estén perfectamente organizados.

    ### ¿Qué es Git?
    Imagina que estás en la cocina, donde cada receta es un proyecto. A veces, la cocina se convierte en un verdadero campo de batalla, con ingredientes volando y mi famoso pastel de manzana en riesgo de quemarse. ¡Ah, la vida en Springfield! Git es como ese viejo y confiable libro de recetas que utilizo, que guarda cada pequeño cambio que hago. Cada vez que modifico un pastel, puedo volver y ver exactamente qué hice, evitando que todo se convierta en un desastre, como cuando Bart trató de hacer un pastel para mi cumpleaños y terminó usando salsa de tomate como decoración.

    **Beneficios de Git:**
    - **Distribución**: Cada desarrollador tiene su propia copia del proyecto, ¡lo que significa que pueden trabajar sin preocuparse de que Lisa les interrumpa con preguntas sobre sus tareas!
    - **Velocidad**: Git es más rápido que Homero tratando de hacer una hamburguesa; maneja proyectos grandes sin despeinarse.
    - **Colaboración**: Permite que todos trabajen juntos sin pisarse los dedos de los pies, como cuando intentamos hacer una cena familiar. Cada uno tiene un rol, ¡y juntos creamos una cena espectacular!

    ### Contenido
    1. ⚙️ **Configuración de Git**
    2. 🚀 **Inicialización de Repositorios**
    """)

    st.markdown("### 1. ⚙️ Configuración de Git")
    st.markdown("""
    Antes de sumergirnos en la creación de nuestros proyectos, debemos asegurarnos de que Git esté configurado correctamente. Es como asegurarte de que todos los ingredientes estén listos antes de empezar a cocinar mi famosa lasaña.

    #### Configurar el Nombre de Usuario
    Primero, necesitamos configurar nuestro nombre de usuario global. Es como firmar tu libro de recetas:
    ```bash
    git config --global user.name "Tu Nombre"
    ```

    **Ejemplo:** Supongamos que estás firmando un libro de recetas muy especial:
    ```bash
    $ git config --global user.name "Marge Simpson"
    ```

    #### Configurar el Correo Electrónico
    Ahora, configuremos tu correo electrónico global, como poner tu dirección en una carta que enviarías a tus amigos para invitarlos a cenar:
    ```bash
    git config --global user.email "tuemail@example.com"
    ```

    **Ejemplo:** Asegúrate de que tus amigos puedan contactarte fácilmente, especialmente si alguna vez me piden la receta de mis galletas de chocolate:
    ```bash
    $ git config --global user.email "marge.simpson@example.com"
    ```

    #### Verificar la Configuración Actual
    Para asegurarte de que todo esté en orden, puedes usar el siguiente comando:
    ```bash
    git config --list
    ```

    **Ejemplo:** Verifica si tu firma está bien puesta, como cuando reviso la lista de ingredientes antes de hacer mis galletas:
    ```bash
    $ git config --list
    user.name=Marge Simpson
    user.email=marge.simpson@example.com
    ```

    #### Configuración Local
    Si tienes un proyecto especial, puedes configurarlo específicamente. Solo omite el `--global`:
    ```bash
    git config user.name "Nombre Local"
    ```

    **Ejemplo:** Para un proyecto único, hazlo así, como cuando me aseguro de que la cena de Navidad esté perfecta:
    ```bash
    $ git config user.name "Marge Proyectos Especiales"
    ```

    📌 **Tip:** Usa `--global` para que se aplique a todos tus proyectos, como cuando organizo mis utensilios de cocina.

    """)

    st.markdown("""
    ## Resumen de Comandos
    Aquí tienes un resumen de los comandos básicos para configurar tu Git, como una lista de recetas que siempre debes tener a mano:
    """)

    comandos = [
        {"Comando": "git config --global user.name 'Tu Nombre'", "Descripción": "Configura el nombre de usuario global en Git."},
        {"Comando": "git config --global user.email 'tuemail@example.com'", "Descripción": "Configura el correo electrónico global en Git."},
        {"Comando": "git config --list", "Descripción": "Muestra la configuración actual de Git."},
        {"Comando": "git init", "Descripción": "Inicializa un nuevo repositorio Git en el directorio actual."}
    ]

    df_comandos_git = pd.DataFrame(comandos)
    st.dataframe(df_comandos_git, use_container_width=True)

    st.markdown("### 2. 🚀 Inicialización de Repositorios en GitHub")
    st.markdown("""
    Ahora que tienes todo configurado, ¡es hora de comenzar tu proyecto! Imagina que estás haciendo una nueva receta para una cena especial. Estoy aquí para guiarte en cada paso del camino.

    ### Pasos para Inicializar un Repositorio en GitHub

    #### Paso 1: Crea el Repositorio en GitHub
    Primero, dirígete a [GitHub](https://github.com/) y crea un nuevo repositorio. Copia la URL del repositorio, como si estuvieras guardando una receta especial en tu libro de cocina. ¡Asegúrate de que la URL sea más sólida que la casa de los Simpson!

    #### Paso 2: Crea la Carpeta y Archivos Necesarios para tu Proyecto
    En tu terminal, navega hasta el lugar donde quieres comenzar tu proyecto y crea una nueva carpeta. Es como preparar el área de trabajo antes de empezar a cocinar mi famosa lasaña:
    ```bash
    $ mkdir mi_proyecto
    $ cd mi_proyecto
    ```

    #### Paso 3: Inicializa el Repositorio Git
    Ahora es el momento de dar el primer paso y preparar tu cocina:
    ```bash
    $ git init
    Initialized empty Git repository in /home/usuario/mi_proyecto/.git/
    ```

    #### Paso 4: Añade los Archivos al Índice
    Añade todos los archivos de tu proyecto, como agregar los ingredientes a tu mezcla de lasaña:
    ```bash
    $ git add .
    ```

    #### Paso 5: Realiza un Commit Inicial
    Realiza un commit inicial, como hacer la primera prueba de tu pastel. Asegúrate de que todo esté bien mezclado:
    ```bash
    $ git commit -m "versión 1 del proyecto"
    ```

    #### Paso 6: Renombra la Rama Principal a 'main'
    Renombra la rama principal para que suene más formal, como un menú especial en nuestra mesa. Esto es como asegurarme de que la decoración de la mesa esté a la altura:
    ```bash
    $ git branch -M main
    ```

    #### Paso 7: Vincula el Repositorio Local con GitHub
    Ahora añade la URL del repositorio que copiaste antes. Es como enviar tu receta a la familia para que la prueben:
    ```bash
    $ git remote add origin https://github.com/usuario/mi_proyecto.git
    ```

    #### Paso 8: Envía los Cambios al Repositorio Remoto
    Finalmente, envía tus cambios al repositorio remoto. Asegúrate de que todo esté en orden, como cuando verifico que todos los ingredientes estén listos para la cena:
    ```bash
    $ git push -u origin main
    ```

    📌 **Tip:** Asegúrate de tener permisos de escritura en el repositorio remoto. ¡No querrás tener problemas como cuando Bart y Lisa discuten por el control remoto!

    """)

    st.markdown("""
    ## Resumen de Comandos
    Aquí tienes un resumen de los comandos básicos para inicializar tu repositorio, como un recetario bien organizado que siempre debes tener a mano:
    """)

    comandos_inicializacion = [
        {"Comando": "mkdir nombre_carpeta", "Descripción": "Crea una nueva carpeta."},
        {"Comando": "cd nombre_carpeta", "Descripción": "Cambia al directorio especificado."},
        {"Comando": "git init", "Descripción": "Inicializa un nuevo repositorio Git en el directorio actual."},
        {"Comando": "git add .", "Descripción": "Añade todos los archivos al índice de Git."},
        {"Comando": "git commit -m 'mensaje'", "Descripción": "Realiza un commit con el mensaje especificado."},
        {"Comando": "git branch -M main", "Descripción": "Renombra la rama principal a 'main'."},
        {"Comando": "git remote add origin URL", "Descripción": "Vincula el repositorio local con el remoto."},
        {"Comando": "git push -u origin main", "Descripción": "Envía los cambios al repositorio remoto."}
    ]

    df_comandos_inicializacion = pd.DataFrame(comandos_inicializacion)
    st.dataframe(df_comandos_inicializacion, use_container_width=True)

    st.markdown("""
    ### Conclusión
    ¡Y ahí lo tienes! Desde la configuración inicial hasta la creación de tu primer repositorio, ahora estás listo para sumergirte en el mundo de Git. Recuerda que, como en la cocina, la práctica es clave. Cada pequeño paso que tomas te acerca a convertirte en un maestro en este arte.

    Si tienes preguntas, ¡no dudes en preguntar! Estoy aquí para ayudarte, al igual que cuando ayudo a Bart y Lisa a hacer su tarea (aunque eso a veces puede ser un desafío).

    ¡Feliz codificación y que disfrutes de tus proyectos tanto como disfruto yo de mis galletas de chocolate! 🍪
    """)







def operaciones_basicas():
    st.title("Operaciones Básicas con Git y Homer Simpson")

    st.markdown("""
    ¡Bienvenidos, amigos! Hoy aprenderemos a usar Git, pero no será un día cualquiera. Homer Simpson, el icónico padre de Springfield, nos acompañará en esta aventura. 
    ¿Listos para aprender y reír al mismo tiempo? ¡Vamos!

    ### Contenido
    1. 📂 **Clonar Repositorios**
    2. ✏️ **Añadir y Eliminar Archivos**
    3. 📜 **Hacer Commits y Ver Historial**
    4. 🔄 **Actualizar y Sincronizar Repositorios**
    5. ✨ **Crear Alias para Comandos**
    """)

    # Clonar Repositorios
    st.markdown("""
    ### 1. Clonar Repositorios
    **Homer**: *¡D'oh! Clonar es como copiar las rosquillas de Moe... solo que en el mundo digital, ¡y sin que te atrapen!*

    Clonar un repositorio es el primer paso para empezar a colaborar en un proyecto existente o para trabajar en un proyecto desde otra máquina. Este proceso copia todo el contenido del repositorio desde el servidor remoto a tu máquina local.

    #### ¿Por Qué Clonar un Repositorio?
    - **Colaboración**: Permite trabajar en equipo en el mismo proyecto.
    - **Acceso Completo**: Obtienes todo el historial del proyecto, facilitando el seguimiento de cambios.
    - **Desarrollo Local**: Puedes trabajar en tu propio entorno de desarrollo sin afectar el repositorio original hasta que decidas enviar tus cambios.

    #### Pasos para Clonar un Repositorio
    1. **Obtener la URL del Repositorio**: Encuentra la URL en la página principal del repositorio en plataformas como GitHub, GitLab, o Bitbucket.
    2. **Ejecutar el Comando de Clonado**: Abre tu terminal y utiliza el siguiente comando:
    ```bash
    git clone <URL-del-repositorio>
    ```

    **Ejemplo Real:**
    Para clonar el repositorio `Git` de GitHub, usa el siguiente comando:
    ```bash
    git clone https://github.com/AlexCapis/Git.git
    ```

    📌 **Tip:** Si el repositorio es privado, necesitarás autenticación. Por ejemplo, si usas GitHub, puedes usar tu usuario y token de acceso en lugar de tu contraseña.

    **Homer**: *¡Y así, mis amigos, comienza nuestra aventura! Listos para explorar el mundo de Git como verdaderos héroes de la tecnología, ¡igual que cuando trato de evitar el ejercicio mientras disfruto de una buena cerveza Duff!*
    """)

    # Añadir y Eliminar Archivos
    st.markdown("""
    ### 2. Añadir y Eliminar Archivos
    **Homer**: *¿Sabías que añadir archivos es como añadir más rosquillas a mi dieta? ¡No puedo dejar de hacerlo, especialmente después de un día en el buffet!*

    Git te permite añadir nuevos archivos a tu repositorio y eliminar los que ya no necesitas. Esto te ayuda a gestionar los cambios y mantener tu proyecto limpio y organizado.

    #### Añadir Archivos al Repositorio
    Para añadir nuevos archivos al área de staging, utiliza el comando `git add`.
    """)
    
    st.code("git add <archivo>", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Homer decidió que su colección de recetas de rosquillas necesitaba un nuevo archivo llamado `Receta_Rosquilla.txt`. Para añadirlo, usa el siguiente comando:
    ```bash
    git add Receta_Rosquilla.txt
    ```

    #### Eliminar Archivos del Repositorio
    Pero, un día, se dio cuenta de que había demasiadas recetas en su colección, así que tuvo que eliminar un archivo. Para hacerlo, usa el comando `git rm`.
    """)
    
    st.code("git rm <archivo>", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Si decide que el archivo `Receta_Pizza.txt` ya no es necesario porque ya tiene su receta favorita, puede eliminarlo con este comando:
    ```bash
    git rm Receta_Pizza.txt
    ```

    📌 **Tip:** Si solo deseas eliminar el archivo del área de staging pero mantenerlo en tu directorio de trabajo, usa `git reset HEAD <archivo>` en lugar de `git rm`.

    **Ejemplo del Tip:**
    Si Homer se arrepiente de añadir `Receta_Rosquilla.txt` al área de staging, puede deshacerlo con:
    ```bash
    git reset HEAD Receta_Rosquilla.txt
    ```
    Esto mantendrá el archivo en su directorio, pero lo eliminará del área de staging.
    """)

    # Hacer Commits y Ver Historial
    st.markdown("""
    ### 3. Hacer Commits y Ver Historial
    **Homer**: *¡Hacer commits es como guardar mis episodios de televisión favoritos! Siempre quiero saber cómo han evolucionado mis aventuras en Springfield mientras disfruto de un buffet sin fin.*

    Realizar commits es una de las funciones más importantes de Git. Te permite guardar el estado de tu proyecto en un punto específico en el tiempo y ver el historial de cambios.

    #### Hacer un Commit
    Para guardar los cambios en el repositorio, usa el comando `git commit` con un mensaje descriptivo.
    """)
    
    st.code("git commit -m \"Mensaje del commit\"", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Homer decidió que había añadido su nueva receta, así que lo guardó en su historia culinaria con gran entusiasmo:
    ```bash
    git commit -m "Añadida nueva receta de rosquilla"
    ```

    #### Ver el Historial de Commits
    Para ver el historial de commits, utiliza el comando `git log`.
    """)
    
    st.code("git log", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Homer, emocionado, quiere ver cómo ha crecido su colección de recetas y qué aventuras ha vivido, así que ejecuta:
    ```bash
    git log
    ```

    📌 **Tip:** Usa `git log --oneline` para un historial más compacto y legible, como un resumen de sus aventuras culinarias.

    **Ejemplo del Tip:**
    Homer usa el siguiente comando para obtener un resumen rápido:
    ```bash
    git log --oneline
    ```
    Esto le mostrará solo el mensaje de cada commit, permitiéndole revisar rápidamente la historia de su colección.
    """)

    # Actualizar y Sincronizar Repositorios
    st.markdown("""
    ### 4. Actualizar y Sincronizar Repositorios
    **Homer**: *Actualizar es como recibir una nueva temporada de mi serie favorita... ¡Siempre quiero estar al día con las aventuras de mis amigos mientras me tomo una Duff en el bar de Moe!*

    Mantener tu repositorio local actualizado con los cambios del repositorio remoto es esencial para colaborar efectivamente.

    #### Actualizar el Repositorio Local
    Usa `git pull` para descargar y fusionar los cambios del repositorio remoto con tu repositorio local.
    """)
    
    st.code("git pull", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Homer se entera de que Bart ha añadido nuevas recetas a su colección y quiere actualizarlas en su propia colección. Para hacerlo, utiliza:
    ```bash
    git pull
    ```

    #### Enviar Cambios al Repositorio Remoto
    Pero, Homer también quiere compartir su nueva receta con Bart, así que usa `git push` para enviar sus cambios locales al repositorio remoto.
    """)
    
    st.code("git push", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para compartir su receta con Bart y hacer que todos en Springfield se enteren de sus delicias culinarias, Homer ejecuta:
    ```bash
    git push
    ```

    #### Verificar el Estado del Repositorio
    Finalmente, para asegurarse de que todo está en orden, utiliza `git status` para ver el estado actual de su repositorio.
    """)
    
    st.code("git status", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Homer, siempre curioso y un poco nervioso, chequea el estado con:
    ```bash
    git status
    ```

    #### Estado Compacto del Repositorio
    También puede usar `git status -s` para ver el estado del repositorio en un formato compacto.
    """)
    
    st.code("git status -s", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Para ver el estado en un formato compacto, Homer usa:
    ```bash
    git status -s
    ```

    📌 **Tip:** Si necesitas un estado más detallado, simplemente utiliza `git status` sin la opción `-s`.
    """)

    # Crear Alias para Comandos
    st.markdown("""
    ### 5. Crear Alias para Comandos
    **Homer**: *¡Crear alias es como ponerle un nombre divertido a mis recetas de rosquillas! ¡Así puedo ser más eficiente mientras me como una!*

    Puedes crear alias para comandos frecuentes de Git para facilitar tu flujo de trabajo.

    #### Cómo Crear un Alias
    Puedes crear un alias utilizando el comando `git config`.
    """)
    
    st.code("git config --global alias.<alias> '<comando>'", language='bash')

    st.markdown("""
    **Ejemplo Real:**
    Si Homer desea crear un alias para `git status`, podría hacer lo siguiente:
    ```bash
    git config --global alias.s 'status'
    ```

    Ahora, en lugar de escribir `git status`, puede simplemente usar `git s`.

    **Homer**: *¡Esto es increíble! ¡Ahora puedo ser más eficiente y aún así parecer genial, como un experto en rosquillas mientras disfruto de una Duff!*

    **Resumen de Comandos**
    Para ayudarte a recordar, aquí tienes un resumen de los comandos básicos que hemos aprendido:
    """)

    # Resumen de comandos en un DataFrame
    df_resumen = pd.DataFrame({
        "Comando": [
            "git clone <URL>",
            "git add <archivo>",
            "git rm <archivo>",
            "git commit -m '<mensaje>'",
            "git log",
            "git pull",
            "git push",
            "git status",
            "git config --global alias.<alias> '<comando>'"
        ],
        "Descripción": [
            "Clona un repositorio desde una URL.",
            "Añade un archivo al área de staging.",
            "Elimina un archivo del repositorio.",
            "Guarda los cambios con un mensaje.",
            "Muestra el historial de commits.",
            "Actualiza el repositorio local con cambios remotos.",
            "Envía los cambios locales al repositorio remoto.",
            "Muestra el estado actual del repositorio.",
            "Crea un alias para un comando."
        ]
    })

    st.dataframe(df_resumen)

    st.markdown("""
    **Homer**: *Ahora que tienes estas herramientas, ¡estás listo para convertirte en un maestro de Git y hacer que tus amigos se mueran de envidia con tus habilidades tecnológicas mientras devoras rosquillas y disfrutas de unas Duff en el bar de Moe!*

    ¡Recuerda! Practicar es la clave. Así que ve y haz que tus proyectos brillen, ¡como la mejor rosquilla de Springfield! ¡Hasta la próxima, amigos!
    """)






def ramas_colaboracion():
    st.title("Ramas y Colaboración con Bart y El Barto")
    st.markdown("""
    En esta sección, descubrirás cómo Bart y su alter ego, El Barto, manejan las ramas y la colaboración en sus épicas aventuras, y cómo tú también puedes hacer lo mismo en tus proyectos de Git.

    ### Contenido
    1. 🌿 **Crear y Gestionar Ramas**
    2. 🔀 **Realizar Merges y Resolver Conflictos**
    3. 🤝 **Estrategias de Colaboración en Proyectos**
    """)

    st.markdown("### 1. 🌿 Crear y Gestionar Ramas")
    st.markdown("""
    Imagina que Bart Simpson, conocido por sus bromas, decide organizar su vida para tener más tiempo para jugar. ¿Cómo lo hace? Creando ramas en su proyecto personal: *La aventura del skate*.

    #### Crear una Nueva Rama
    Bart decide que necesita una nueva estrategia, así que se crea una nueva rama en su proyecto. Usa el siguiente comando para crear una nueva rama:
    ```bash
    git branch aventura-skate
    ```
    Con `git branch aventura-skate` Bart crea una rama llamada `aventura-skate` donde podrá planificar su próximo truco en la patineta sin afectar el resto de sus travesuras.

    #### Cambiar a una Rama Diferente
    Una vez que ha creado la rama, Bart quiere entrar en acción. Para hacerlo, usa:
    ```bash
    git checkout aventura-skate
    ```

    Con `git checkout aventura-skate` Bart cambia a la rama `aventura-skate`, permitiéndole enfocarse en sus nuevos trucos mientras mantiene sus otras aventuras intactas.

    #### Crear y Cambiar a una Nueva Rama en un Solo Paso
    A veces, Bart como es muy vago es muy eficiente. Entonces, decide hacer todo en un solo paso:
    ```bash
    git checkout -b aventura-nueva
    ```

    Con `git checkout -b aventura-nueva` Bart crea y cambia a una nueva rama llamada `aventura-nueva` para comenzar su próxima travesura sin perder tiempo.

    #### Ver todas las Ramas
    En su cuaderno de skater, Bart quiere ver qué ramas ha creado:
    ```bash
    git branch
    ```

    Con `git branch` Muestra todas las ramas en su repositorio, ayudando a Bart a recordar sus locuras anteriores.

    📌 **Tip:** Bart siempre usa nombres creativos para sus ramas, como `feature/skate_futurista`, para que no se confunda.

    📌 **Tip:** Si alguna de sus ramas (bromas) está vieja, Bart la elimina con:
    ```bash
    git branch -d aventura_olvidada
    ```

    Esto asegura que su cuaderno siempre esté ordenado.

    """)

    st.markdown("### 2. 🔀 Realizar Merges y Resolver Conflictos")
    st.markdown("""
    Después de un día lleno de aventuras, Bart quiere compartir sus nuevos trucos con sus amigos. Así que necesita mezclar sus cambios de la rama `aventura-skate` a la rama principal, `main`.

    #### Realizar un Merge
    Primero, Bart cambia a la rama donde quiere integrar los cambios:
    ```bash
    git checkout main
    ```

    Luego, realiza el merge:
    ```bash
    git merge aventura-skate
    ```

    Con `git merge aventura-skate` Bart integra los cambios de `aventura-skate` en la rama principal, compartiendo sus trucos con todos.

    #### Resolver Conflictos
    Pero, ¡oh no! Alguien más estaba trabajando en la misma sección del proyecto y Bart se enfrenta a un conflicto. Así que debe resolverlo. Abre el archivo conflictivo y lo edita, y luego añade los cambios al área de staging:
    ```bash
    git add conflictivo.txt
    ```

    Con `git add conflictivo.txt` Bart añade el archivo después de resolver el conflicto, asegurándose de que sus amigos tengan lo mejor de sus aventuras.

    Una vez resueltos todos los conflictos, Bart guarda los cambios:
    ```bash
    git commit -m "Resolver conflictos de merge"
    ```

    Con `git commit -m "Resolver conflictos de merge"`Bart guarda sus cambios y da un mensaje claro sobre lo que resolvió.

    """)

    st.markdown("### 3. 🤝 Estrategias de Colaboración en Proyectos")
    st.markdown("""
    Para asegurarse de que sus aventuras sean aún más épicas, Bart implementa algunas estrategias de colaboración.

    #### Uso de Pull Requests
    Bart sabe que es importante recibir feedback, así que crea un Pull Request (PR) para que sus amigos revisen su nuevo truco. Los PRs son una excelente manera de discutir cambios antes de integrarlos en la rama principal.

    #### Revisión de Código
    Organiza sesiones de revisión de código con sus amigos, donde todos pueden aportar ideas y mejorar los trucos de skate. Las revisiones regulares aseguran que el equipo mantenga la calidad de sus trucos y bromas.

    #### Integración Continua
    Bart se da cuenta de que configurar CI/CD es clave. Así que integra herramientas como Jenkins para asegurarse de que sus trucos no rompan la diversión. Las pruebas automáticas garantizan que todo esté en su lugar.

    📌 **Tip:** Establecer convenciones de commits y flujos de trabajo como GitFlow ayuda a Bart a mantener su proyecto organizado y fácil de seguir.

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
    Así, con la creatividad y inteligencia de Bart para salirse siempre con la suya, y las herramientas adecuadas de Git, podrás colaborar y gestionar tus proyectos como un verdadero maestro del skate. ¡A practicar y aplicar lo que has aprendido!
    """)






def avanzado_git():
    st.title("Las Aventuras de Lisa en el Mundo de Git")

    st.markdown("""
    ¡Hola, amigos del código! Soy Lisa Simpson, y hoy seré su guía en esta emocionante aventura por el vasto universo de Git. 🌌
    Con cada comando que aprendamos, también exploraremos algunos de mis momentos favoritos de la serie. ¡Prepárense para aprender y divertirse! 

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
    Recuerden esa vez en que intenté organizar un grupo de estudio para un examen de ciencias, y Homer interrumpió con su versión de 'Música para Dormir'. 🎶
    El rebase es como asegurarte de que tu grupo de estudio tenga toda la información más reciente y útil, para que todos estén al tanto sin perder el hilo de la conversación.

    #### Comando de Rebase
    ```bash
    git rebase <rama-base>
    ```

    **Ejemplo Real:**
    Imagina que estás trabajando en un proyecto sobre biología y tu maestro, el Sr. Skinner, ha añadido algunos cambios importantes a su trabajo en `main`:
    ```bash
    git checkout feature
    git rebase main
    ```
    Con `git rebase main` te ayuda a llevar todos esos cambios valiosos a tu proyecto, como si estuvieras pidiendo las notas de tu maestro para estar siempre al día.

    📌 **Tip:** Usa `rebase` para mantener la historia de tus proyectos clara y organizada, así como tus apuntes en la biblioteca. 📚
    """)

    st.markdown("### 🗂️ Stash")
    st.markdown("""
    ¿Alguna vez has tenido que guardar tu saxofón mientras intentabas resolver un complicado problema de matemáticas? 🎷🧩
    Eso es lo que hace `stash`: te permite guardar tus cambios temporalmente para que puedas concentrarte en otras cosas.

    #### Comando de Stash
    ```bash
    git stash
    ```

    **Ejemplo Real:**
    Estás trabajando en tu investigación sobre el medio ambiente, pero de repente debes ayudar a Bart a escapar de un problema. ¡Es momento de guardar tus notas!
    ```bash
    git stash
    git checkout main
    ```

    - Con `git stash`, guardas tu trabajo a salvo para atender a tu hermano, ¡igual que guardas tu saxofón para ayudar a Bart!

    #### Aplicar y Eliminar Stash
    ```bash
    git stash apply
    git stash pop
    ```

    **Ejemplo Real:**
    Después de ayudar a Bart, vuelves a tu proyecto:
    ```bash
    git checkout feature
    git stash apply
    ```

    **Explicación del Ejemplo:**
    - `git stash apply` saca tus notas del cofre, listas para seguir con tu investigación.

    📌 **Tip:** Usa `git stash list` para ver todos tus trabajos guardados, como tus proyectos en la biblioteca. 🏫
    """)

    st.markdown("### 🍒 Cherry-Pick")
    st.markdown("""
    En una competencia de inteligencia, siempre hay un momento clave donde puedes tomar la respuesta correcta sin seguir todo el proceso. 🍒
    Así es como funciona `cherry-pick`: seleccionas solo lo que necesitas de los cambios de otra rama.

    #### Comando de Cherry-Pick
    ```bash
    git cherry-pick <id-del-commit>
    ```

    **Ejemplo Real:**
    Supón que descubriste un experimento increíble sobre la fotosíntesis en la rama `investigaciones`, y quieres llevarlo a `main`:
    ```bash
    git checkout main
    git cherry-pick a1b2c3d4
    ```

    **Explicación del Ejemplo:**
    - `git cherry-pick a1b2c3d4` te permite llevar esa valiosa información directamente a tu trabajo sin complicaciones.

    📌 **Tip:** Ideal para seleccionar solo las mejores ideas, como elegir la respuesta más brillante en un concurso. 💡
    """)

    st.markdown("### 🔄 Reset")
    st.markdown("""
    A veces, en mis aventuras, me doy cuenta de que necesito retroceder. `git reset` es como tener una máquina del tiempo que me permite volver a un punto anterior en mi camino. ⏳

    #### Comando de Reset
    ```bash
    git reset --hard <commit-id>
    ```

    **Ejemplo Real:**
    Imagina que decides que un experimento en el que trabajaste no salió como esperabas, y quieres volver a un punto anterior:
    ```bash
    git reset --hard a1b2c3d4
    ```

    **Explicación del Ejemplo:**
    - Con `git reset --hard`, vuelves a un estado donde todo estaba perfecto, pero cuidado: todos tus cambios no confirmados se perderán. ❌

    #### Reset Suave
    ```bash
    git reset --soft HEAD~1
    ```

    **Ejemplo Real:**
    Si decides que tu último experimento fue un error, pero no quieres perder la información:
    ```bash
    git reset --soft HEAD~1
    ```

    **Explicación del Ejemplo:**
    - `git reset --soft HEAD~1` te permite eliminar ese paso pero conservar todo lo que aprendiste, como volver a dibujar tu experimento en el pizarrón.

    📌 **Tip:** Usa `git reset --hard` con precaución; a veces es mejor aprender de los errores. ⚖️
    """)

    st.markdown("### 🔄 Diff y Reflog")
    st.markdown("""
    #### Diff
    Cuando estoy escribiendo mi artículo para la revista escolar, a menudo reviso lo que he cambiado. `git diff` es como mirar en un espejo que te muestra las diferencias entre tu borrador y el documento final. 🔍

    ```bash
    git diff
    ```

    **Ejemplo Real:**
    Para ver los cambios que has hecho en tu último ensayo de ciencias:
    ```bash
    git diff
    ```

    **Explicación del Ejemplo:**
    - `git diff` te muestra las modificaciones, como ver las anotaciones en tu trabajo antes de entregarlo.

    #### Reflog
    Y cuando necesito recordar todos los pasos que he dado en mis investigaciones, `git reflog` es como mi diario personal. 📖

    ```bash
    git reflog
    ```

    **Ejemplo Real:**
    Para revisar el historial de tus experimentos y saber qué ha funcionado y qué no:
    ```bash
    git reflog
    ```

    **Explicación del Ejemplo:**
    - `git reflog` te permite ver todos los cambios que has hecho en tu proyecto, como mirar atrás en tu diario de aventuras.

    📌 **Tip:** Usa `git diff` antes de hacer un commit para asegurarte de que todo esté en su lugar. ¡Es como revisar tu trabajo antes de entregarlo! ✨
    """)

    st.markdown("### 🏷️ Tag")
    st.markdown("""
    A veces, hay momentos en mis proyectos que merecen ser celebrados, como cuando gané el concurso de ciencias. `git tag` es la forma perfecta de marcar esos hitos. 🏅

    #### Comando de Tag
    ```bash
    git tag <nombre-del-tag>
    ```

    **Ejemplo Real:**
    Para marcar una versión de tu trabajo como `v1.0` después de un gran esfuerzo:
    ```bash
    git tag v1.0
    ```

    **Explicación del Ejemplo:**
    - `git tag v1.0` es como poner una medalla en tu proyecto para recordar ese gran momento de triunfo.

    📌 **Tip:** Usa etiquetas para marcar versiones clave en tus proyectos, ¡así siempre recordarás tus logros! 🏆
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
            "Mantiene tu grupo de estudio al día.",
            "Guarda tus ideas mientras resuelves problemas.",
            "Recupera tus ideas guardadas.",
            "Elige solo lo mejor de tus experimentos.",
            "Vuelve en el tiempo a un estado anterior.",
            "Deshazte de un paso pero conserva tus ideas.",
            "Revisa lo que ha cambiado en tu trabajo.",
            "Mira atrás y revisa tus pasos.",
            "Marca tus logros como versiones especiales."
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)












def integracion_github():
    st.title("Integración de GitHub con Ned Flanders")

    st.markdown("""
    ¡Hola, vecinito! Hoy vamos a aprender, con mucho cariñito y alegría, cómo conectar nuestro repositorio local con GitHub. Porque ya sabes, compartir es una bendición, y en este vecindario del código, siempre es bonito ayudar a los demás.

    ### Contenidito para nuestro caminito:
    1. 🌐 **Conectar el Repositorio Local a GitHub, vecinito**
    2. 🚀 **Solicitar una Pull Request con cariño y educadito**
    3. 🔍 **Consejitos útiles para trabajar en equipo con mucho amorcito**

    ### Conectar Repositorio Local a GitHub
    Empezamos por lo más sencillito, como cuando saludas a tu vecinito por la mañanita. Lo primero que necesitamos es conectar nuestro repositorio local a GitHub, el lugarcito donde guardaremos todo nuestro trabajito para que lo vean los demás y todos nos sintamos contentitos.

    #### Crear un Nuevito Repositorio en GitHub:
    1. Primero, ve a [GitHub](https://github.com) e inicia sesión, vecinito.
    2. Luego, dale un clic en "Nuevo repositorio", como cuando invitas a tu vecinito a tomar un cafecito.
    3. Rellena los campitos necesarios y haz clic en "Crear repositorio". ¡Qué alegría tan grandecita!

    #### Conectar tu Repositorio Local:
    ```bash
    git remote add origin <URL-del-repositorio>
    git branch -M main
    git push -u origin main
    ```

    **Ejemplo (más clarito que el agüita, vecinito):**
    ```bash
    git remote add origin https://github.com/usuario/repositorio.git
    git branch -M main
    git push -u origin main
    ```

    **Explicación (sencillita y bendecidita, vecinito):**
    - `git remote add origin <URL-del-repositorio>`: Conectas tu repositorio local con el remotito, como cuando das una llamadita a un amiguito.
    - `git branch -M main`: Cambias la rama principal a `main`, porque siempre es bueno tener todo bien ordenadito.
    - `git push -u origin main`: Subes la rama `main` al repositorio remotito, asegurando que todo está en armonía divina.

    📌 **Tip bendecidito:** Recuerda cambiar `<URL-del-repositorio>` por la URL de tu repositorio en GitHub, ¡y todo saldrá bien bonitito!

    """)

    st.markdown("### 🚀 Pull Requests (o como pedir ayudita a los vecinitos)")
    st.markdown("""
    Las pull requests son como esas veces que necesitas que tu vecinito te eche una manita antes de tomar una decisión importantita. ¡Qué bonito es colaborar entre buenos vecinitos!

    #### Crear una Pull Request con todo tu cariñito:
    1. Crea una nueva ramita y haz commits con mucho amorcito:
    ```bash
    git checkout -b <nombre-de-la-ramita>
    # realiza los cambiecitos y commits con fe
    git push origin <nombre-de-la-ramita>
    ```
    2. Luego, en GitHub, ve a tu repositorio y haz clic en "Compare & pull request". Es como cuando invitas a tus vecinitos a charlar sobre cómo mejorar las cosas.
    3. Rellena los detallitos, como cuando preparas algo rico para compartir, y haz clic en "Create pull request". ¡Es tan bonito como una tarde de juegos en el parquecito!

    **Ejemplo Real (hecho con mucho amorcito):**
    ```bash
    git checkout -b feature/nueva-funcionalidad
    # realizas los cambios con fe
    git add .
    git commit -m "Añadir nueva funcionalidad bendecidita"
    git push origin feature/nueva-funcionalidad
    ```

    **Explicación del Ejemplo (sencillito y lleno de amorcito, vecinito):**
    - `git checkout -b <nombre-de-la-ramita>`: Creas una nueva ramita, como cuando plantas una semillita que con amorcito crecerá.
    - `git push origin <nombre-de-la-ramita>`: Subes tu ramita a GitHub, porque el trabajito bien hecho siempre se comparte con cariño.
    - Luego en GitHub, abres una pull request para que tus vecinitos revisen tu trabajito y entre todos lo hagamos más bonito.

    📌 **Tip divinito:** Sé claro y preciso al describir tu pull request, vecinito, ¡así ayudarás a tus compañeros a entender mejor y todos seremos más felices!

    """)

    st.markdown("### 🔍 Consejitos útiles para vecinitos diligentes")
    st.markdown("""
    Aquí tienes algunos consejitos prácticos para que todo esté siempre en orden, vecinito, ¡porque un buen vecino siempre es precavido y organizado!

    #### Comprobar el estado de tu repositorio (como revisar tus tareas diarias, vecinito)
    ```bash
    git status
    ```

    **Ejemplo clarito y bendito:**
    ```bash
    git status
    ```

    **Explicación (para que todo esté ordenadito, vecinito):**
    - `git status`: Este comando te muestra el estado de tu repositorio. ¡Es como echarle un vistacito a las tareas del día para asegurarse de que todo está en su sitio!

    #### Mantener tu repositorio sincronizado (como mantener la paz en el vecindario, vecinito)
    ```bash
    git fetch origin
    git pull origin main
    ```

    **Ejemplo bendecidito:**
    ```bash
    git fetch origin
    git pull origin main
    ```

    **Explicación (para que siempre haya armonía, vecinito):**
    - `git fetch origin`: Este comando obtiene actualizaciones del repositorio remotito sin aplicarlas de inmediato, como escuchar con atención antes de actuar.
    - `git pull origin main`: Aquí aplicas los cambios, asegurando que todo esté actualizadito y en paz.

    #### Cambiar el nombre de una rama remotita (como renombrar algo para mayor claridad, vecinito)
    ```bash
    git push origin :<nombre-antiguo>
    git push origin <nombre-nuevo>
    ```

    **Ejemplo clarito y bonito:**
    ```bash
    git push origin :old-branch-name
    git push origin new-branch-name
    ```

    **Explicación (sencillita y efectiva, vecinito):**
    - `git push origin :<nombre-antiguo>`: Aquí eliminas una rama remota con el nombre antiguo, como cuando decides hacer espacio para algo nuevito.
    - `git push origin <nombre-nuevo>`: Subes una nueva rama con un nombrecito fresquito, asegurando que todo esté claro y bien organizadito.

    📌 **Tip celestial:** Mantén siempre tus ramitas ordenadas, vecinito, ¡así todo será más fácil y bendecidito para ti y los demás!

    """)

    # Resumen de Comandos (como un sermoncito dominical)
    st.markdown("### Resumen de Comandos de Integración en GitHub, vecinito")

    data = {
        "Comandito": [
            "`git remote add origin <URL-del-repositorio>`",
            "`git branch -M main`",
            "`git push -u origin main`",
            "`git push origin <nombre-de-la-ramita>`",
            "`git status`",
            "`git fetch origin`",
            "`git pull origin main`",
            "`git push origin :<nombre-antiguo>`",
            "`git push origin <nombre-nuevo>`"
        ],
        "Descripcióntita": [
            "Conectas el repositorio local con el remoto, como cuando haces amiguitos nuevos.",
            "Renombras tu rama principal a 'main', para tener todo bien ordenadito.",
            "Subes tu rama principal con amorcito y todo en su sitio.",
            "Subes tu ramita al repositorio remoto, para que los demás también puedan ver tu trabajito.",
            "Compruebas el estado de tu repositorio, como harías con tus tareas diarias.",
            "Obtienes actualizaciones del repositorio remoto para estar siempre al día.",
            "Actualizas tu rama local con los últimos cambios, manteniendo la paz en tu código.",
            "Eliminas una rama remota con el nombrecito antiguo para dejar espacio a nuevas oportunidades.",
            "Subes una nueva rama remota con un nombre más clarito y fresquito."
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
        "q2": "git add index.html",
        "q3": 'git commit -m "Añadida nueva función"',
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
        "q2": ["git add index.html", "git commit index.html", "git push index.html", "git remove index.html"],
        "q3": [ 'git commit -a -m "Añadida nueva función"', 'git commit --message "Añadida nueva función"','git commit -m "Añadida nueva función"', 'git commit m "Añadida nueva función"'],
        "q4": ["git status", "git log", "git history", "git log --goneline"],
        "q5": ["git tag", "git commit --amend", "git reset","git stash"],
        "q6": [ "git rebase feature-x", "git cherry-pick feature-x","git merge feature-x", "git merge main"],
        "q7": ["git delete deprecated_feature.py", "git remove deprecated_feature.py", "git drop deprecated_feature.py","git rm deprecated_feature.py"],
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
    
    st.title("Ejercicios de Git con Apu Nahasapeemapetilon")

    st.markdown("¡Bienvenidos al *Badulaque*! Como diría Apu: **Gracias, vuelva pronto... a hacer más commits!**")

    # Ejercicio 1
    st.header("Ejercicio 1: Clonar un Repositorio")
    st.markdown("""
    "Bienvenido, señor GitHub. ¿Cómo le puedo ayudar hoy?"
    
    Imagina que Apu ha recibido una URL de un repositorio y necesita clonar ese repositorio para actualizar el stock de su tienda. ¿Qué comando debería usar?"
    """)
    opciones1 = st.session_state.opciones["q1"]
    respuesta1 = st.radio("Selecciona la respuesta correcta:", opciones1, key="q1_respuesta")
    if st.button("Verificar Respuesta 1", key="q1_btn"):
        verificar_respuesta(respuesta1, "q1")

    # Ejercicio 2
    st.header("Ejercicio 2: Añadir Archivos al Área de Staging")
    st.markdown("""
    "¡Este código es mejor que un fresisuis recién servido!" 
    Apu ha hecho cambios en `index.html` para mejorar las ofertas del Badulaque y quiere prepararlo para el próximo commit. ¿Qué comando debe usar?"
    """)
    opciones1 = st.session_state.opciones["q2"]
    respuesta2 = st.radio("Selecciona la respuesta correcta:", opciones1, key="q2_respuesta")
    if st.button("Verificar Respuesta 2", key="q2_btn"):
        verificar_respuesta(respuesta2, "q2")

    # Ejercicio 3
    st.header("Ejercicio 3: Hacer un Commit con un Mensaje")
    st.markdown("""
    "Oh no, ¡he cometido un error en los precios de las rosquillas de Homer! Hora de hacer un commit con un mensaje apropiado: 'Añadida nueva función'. ¿Cuál es el comando correcto?"
    """)
    opciones3 = st.session_state.opciones["q3"]
    respuesta3 = st.radio("Selecciona la respuesta correcta:", opciones3, key="q3_respuesta")
    if st.button("Verificar Respuesta 3", key="q3_btn"):
        verificar_respuesta(respuesta3, "q3")

    # Ejercicio 4
    st.header("Ejercicio 4: Ver el Historial de Commits")
    st.markdown("""
    "Señor Git, déjeme revisar mis viejos errores y... ¡oh, aquí está el commit donde cambié los precios de los productos de Homer! ¿Qué comando uso para ver el historial de mis transacciones?"
    """)
    opciones4 = st.session_state.opciones["q4"]
    respuesta4 = st.radio("Selecciona la respuesta correcta:", opciones4, key="q4_respuesta")
    if st.button("Verificar Respuesta 4", key="q4_btn"):
        verificar_respuesta(respuesta4, "q4")

    # Ejercicio 5
    st.header("Ejercicio 5: Guardar Cambios Temporalmente")
    st.markdown("""
    "Apu ha recibido una llamada urgente de Homer sobre una oferta de fresisuis, pero primero necesita guardar sus cambios en el stock de Badulaque sin hacer un commit. ¿Qué comando usaría?"
    """)
    opciones5 = st.session_state.opciones["q5"]
    respuesta5 = st.radio("Selecciona la respuesta correcta:", opciones5, key="q5_respuesta")
    if st.button("Verificar Respuesta 5", key="q5_btn"):
        verificar_respuesta(respuesta5, "q5")

    # Ejercicio 6
    st.header("Ejercicio 6: Fusionar Cambios de una Rama")
    st.markdown("""
    "Apu ha terminado de trabajar en la rama `feature-x` donde añadió un nuevo tipo de fresisuis. Ahora quiere fusionar estos cambios con la rama `main`. ¿Qué comando debería usar?"
    """)
    opciones6 = st.session_state.opciones["q6"]
    respuesta6 = st.radio("Selecciona la respuesta correcta:", opciones6, key="q6_respuesta")
    if st.button("Verificar Respuesta 6", key="q6_btn"):
        verificar_respuesta(respuesta6, "q6")

    # Ejercicio 7
    st.header("Ejercicio 7: Eliminar un Archivo del Repositorio")
    st.markdown("""
    "Ese archivo `deprecated_feature.py` es como los precios antiguos del Badulaque: ¡ya no sirve! ¿Qué comando debería usar Apu para eliminar este archivo del repositorio?"
    """)
    opciones7 = st.session_state.opciones["q7"]
    respuesta7 = st.radio("Selecciona la respuesta correcta:", opciones7, key="q7_respuesta")
    if st.button("Verificar Respuesta 7", key="q7_btn"):
        verificar_respuesta(respuesta7, "q7")

    # Ejercicio 8
    st.header("Ejercicio 8: Ver Cambios entre Commits")
    st.markdown("""
    "Apu necesita comparar dos cambios importantes en los precios de sus fresisuis, entre los commits `abc123` y `def456`. ¿Qué comando usaría?"
    """)
    opciones8 = st.session_state.opciones["q8"]
    respuesta8 = st.radio("Selecciona la respuesta correcta:", opciones8, key="q8_respuesta")
    if st.button("Verificar Respuesta 8", key="q8_btn"):
        verificar_respuesta(respuesta8, "q8")

    # Ejercicio 9
    st.header("Ejercicio 9: Subir una nueva Rama al Repositorio Remoto")
    st.markdown("""
    "Apu ha creado una nueva rama local llamada `feature-y` con las ofertas especiales de la semana. Quiere subirla al repositorio remoto para que todos puedan verlas. ¿Qué comando usaría?"
    """)
    opciones9 = st.session_state.opciones["q9"]
    respuesta9 = st.radio("Selecciona la respuesta correcta:", opciones9, key="q9_respuesta")
    if st.button("Verificar Respuesta 9", key="q9_btn"):
        verificar_respuesta(respuesta9, "q9")

    # Ejercicio 10
    st.header("Ejercicio 10: Revertir el Último Commit")
    st.markdown("""
    "Apu cometió un error en el último commit y decide revertirlo, pero quiere conservar los cambios en el área de staging. ¿Qué comando usaría para deshacer el último commit?"
    """)
    opciones10 = st.session_state.opciones["q10"]
    respuesta10 = st.radio("Selecciona la respuesta correcta:", opciones10, key="q10_respuesta")
    if st.button("Verificar Respuesta 10", key="q10_btn"):
        verificar_respuesta(respuesta10, "q10")

    st.markdown("**¡Gracias, vuelva pronto y recuerde hacer siempre un `git pull` antes de trabajar!** - Apu")


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



def feedback():
    st.title("🍼 Feedback del Taller con Maggie")

    st.markdown("""
    **¡Pssst!** Maggie ha dejado caer su chupete para saber qué opinas del taller. Como no puede hablar, ella escucha atentamente lo que tienes que decir para seguir mejorando. ¡Déjanos tus impresiones y no olvides sonreír como lo harías con Maggie! 😊
    
    ### Preguntas de Feedback (Maggie promete que no habrá balbuceos... solo tus respuestas)
    """)

    # Pedimos el nombre del participante
    nombre = st.text_input("Por favor, introduce tu nombre para identificar tu feedback", key="nombre")

    # Pregunta 1
    st.subheader("1. ¿Qué te ha parecido el contenido del taller?")
    contenido = st.text_area("Tu respuesta:", key="contenido")

    # Pregunta 2
    st.subheader("2. ¿Hubo algún tema que te resultó tan interesante que hasta Maggie dejó de chuparse el dedo?")
    tema_util = st.text_area("Tu respuesta:", key="tema_util")

    # Pregunta 3
    st.subheader("3. ¿Hay algo que podamos mejorar? Maggie sabe que siempre hay algo que ajustar... como la posición del biberón.")
    mejoras = st.text_area("Tu respuesta:", key="mejoras")

    # Pregunta 4
    st.subheader("4. ¿Te gustaría participar en futuros talleres? Maggie quiere saber si seguirá escuchando tus ideas.")
    futuros_talleres = st.radio("Selecciona una opción:", ["Sí", "No"], key="futuros_talleres")

    # Espacio para otros comentarios
    st.subheader("Otros comentarios (Maggie está toda oídos, aunque no lo parezca...)")
    otros_comentarios = st.text_area("Tu respuesta:", key="otros_comentarios")

    # Botón para enviar feedback
    if st.button("Enviar Feedback", key="enviar_feedback"):
        if nombre:  # Nos aseguramos de que el usuario ha introducido un nombre
            # Creamos un diccionario con las respuestas
            feedback_data = {
                "Nombre": [nombre],
                "Contenido del Taller": [contenido],
                "Tema Útil": [tema_util],
                "Mejoras Sugeridas": [mejoras],
                "Participación en Futuros Talleres": [futuros_talleres],
                "Otros Comentarios": [otros_comentarios]
            }

            # Convertimos el diccionario en un DataFrame de pandas
            feedback_df = pd.DataFrame(feedback_data)

            # Definimos el nombre del archivo Excel
            file_path = "feedback_taller.xlsx"

            # Verificamos si el archivo ya existe
            if os.path.exists(file_path):
                # Si existe, cargamos el archivo y añadimos nuevas filas
                with pd.ExcelWriter(file_path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                    feedback_df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
            else:
                # Si no existe, lo creamos y añadimos el encabezado
                feedback_df.to_excel(file_path, index=False, header=True)

            st.success("¡Gracias por tu feedback! Maggie dice: ¡goo goo ga ga! (Lo que significa 'Gracias' en su idioma).")
        else:
            st.error("Por favor, introduce tu nombre antes de enviar el feedback.")

# Diccionario para la navegación
paginas = {
    "Home": pagina_principal,
    "Comandos Básicos el Ralph": comandos_basicos_terminal,
    "Configuración e Inicialización con Marge": configuracion_e_inicializacion_git,
    "Operaciones Básicas con Homer": operaciones_basicas,
    "Ramas y Colaboración con Bart": ramas_colaboracion,
    "Uso Avanzado de Git con Lisa": avanzado_git,
    "Integración de GitHub con Ned": integracion_github,
    "Resumen con Nelson": resumen_taller,
    "Ejercicios con Apu": ejercicios,
    "Feedback con Maggie": feedback
}

# Sidebar para la selección de página
st.sidebar.title("Contenido")
seleccion = st.sidebar.radio("Selecciona una sección", list(paginas.keys()))

# Ejecutar la función correspondiente a la selección de página
paginas[seleccion]()

