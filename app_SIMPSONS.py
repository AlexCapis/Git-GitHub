import streamlit as st
import os
import pandas as pd


# Configuración de la página
st.set_page_config(page_title="Taller de Git con Los Simpsons", page_icon="🍩", layout="wide")

# Función para verificar las respuestas
def verificar_respuesta(respuesta, correcta):
    if respuesta.strip() == correcta:
        st.success("¡Correcto!")
    else:
        st.error(f"Incorrecto. La respuesta correcta es `{correcta}`.")


def pagina_principal():
    # Título y bienvenida
    st.markdown("<h1 style='text-align: center;'>¡Bienvenidos al Taller de Git con Los Simpsons!</h1>", unsafe_allow_html=True)
    st.markdown("---")
    # Centrando la imagen de Maggie usando st.image() y con ancho ajustado
    col1, col2, col3 = st.columns([1, 2, 1])  # Tres columnas para centrar el contenido en el medio
    with col2:
        st.image("images/Portadas/SIMPSONS.jpeg", width=400)  # Imagen centrada en la columna del medio


    # Historia de introducción
    st.markdown("""
    ### ¡Bienvenidos a Springfield!

    En este taller aprender Git te resultará más fácil que beberse una Duff para Homer. En este taller, aprenderás a manejar el control de versiones como si fueras parte de la familia Simpson. ¿Te imaginas a Homer aprendiendo a hacer commits? ¡Eso es un espectáculo que no querrás perderte!

    Aquí, cada personaje tiene algo que enseñarte. Lisa, la cerebrito del grupo, se asegura de que todo sea ordenado y eficiente. Marge, con su infalible sentido del hogar, te guiará para que tu proyecto esté tan limpio como su casa. Bart, el rebelde, te mostrará cómo tomar riesgos y hacer cosas inesperadas con Git, mientras que Maggie, aunque no hable, siempre está lista para detectar mejoras que nadie más ve.
    """)


    # Configuración de columnas
    col1, col2 = st.columns(2)

    # Primera columna (izquierda)
    with col1:
        with st.container():
            st.markdown("### Ralph")
            st.image("images/ralph/ralph_presentacion.jpeg", width=300, caption="Git es como caramelos, ¡pero sin pegamento! A veces hago cosas y aparecen en otro lado... ¡Es como magia rara!")
            st.markdown("""
            **Comandos Básicos con Ralph**: ¡Hola! Soy Ralph y aquí te guiaré por los comandos básicos de terminal. ¡Nada de cebollas misteriosas en el parque, lo prometo!
            """)

        with st.container():
            st.markdown("### Homer")
            st.image("images/homer/homer_presentacion.jpeg", width=300, caption="¿Por qué programar cuando puedes comer?")
            st.markdown("""
            **Operaciones Básicas con Homer**: ¡Mmm, comandos básicos de Git! Tan buenos como una cerveza fría. Con **git add** y **git commit**, ¡verás que es tan bueno como abrir una Duff!
            """)

        with st.container():
            st.markdown("### Lisa")
            st.image("images/lisa/lisa_presentacion.jpeg", width=300, caption="Organizar código es como el jazz, ¡requiere práctica y ritmo!")
            st.markdown("""
            **Uso Avanzado de Git con Lisa**: Soy Lisa Simpson y aquí me toca poner orden. Aprenderemos técnicas avanzadas para que tu proyecto sea tan eficiente como mi saxofón en domingo.
            """)

        with st.container():
            st.markdown("### Nelson")
            st.image("images/nelson/nelson_presentacion_2.jpeg", width=300, caption="Ha-ha! ¡Si aprendes Git, te salvas de mis bromas!")
            st.markdown("""
            **Resumen del Taller con Nelson**: ¡Ha-ha! Soy Nelson y aquí no te escapas sin aprender Git. Repasaremos todo porque lo digo yo… ¡o sino verás!
            """)

        with st.container():
            st.markdown("### Maggie")
            st.image("images/maggie/maggie_presentacion.jpeg", width=300, caption="Maggie asiente en silencio... ¡Tu feedback es importante, así que cuéntanos!")
            st.markdown("""
            **Feedback con Maggie**: Incluso Maggie tiene algo que decir, ¿por qué no tú? ¡Tu feedback es valioso! Déjanos tus comentarios y sugerencias para que podamos mejorar y hacer que este taller sea todavía más increíble.
            """)

    # Segunda columna (derecha)
    with col2:
        with st.container():
            st.markdown("### Marge")
            st.image("images/marge/marge_presentacion.jpeg", width=300, caption="Organizar Git es como ordenar la cocina. ¡Todo en su sitio!")
            st.markdown("""
            **Configuración e Inicialización con Marge**: Hola, soy Marge. Configurar Git es como organizar la despensa: una vez que todo está en su sitio, la vida es mucho más fácil. ¡Vamos a evitar que Homer borre todo accidentalmente!
            """)

        with st.container():
            st.markdown("### Bart")
            st.image("images/bart/bart_presentacion.jpeg", width=300, caption="¡Soy el Barto! El caos de Git es mi especialidad.")
            st.markdown("""
            **Ramas y Colaboración con Bart**: ¡Yo soy el Barto! Vamos a liarla con unas cuantas ramas de Git, pero no te preocupes, ¡Lisa nos salvará antes de que se nos vaya todo de las manos!
            """)

        with st.container():
            st.markdown("### Ned Flanders")
            st.image("images/ned/ned_presentacion.jpeg", width=300, caption="Integrar con GitHub es como un saludito amistosito!")
            st.markdown("""
            **Integración con GitHub con Ned Flanders**: ¡Hola holita, vecinitos! Integrar Git con GitHub es más fácil que una limonada bien fresquita en una tarde de verano. ¡Nada complicado, lo prometo!
            """)

        with st.container():
            st.markdown("### Apu")
            st.image("images/apu/apu_presentacion.jpeg", width=300, caption="¡Gracias, vuelve pronto! Dominaremos Git como los precios del Badulaque.")
            st.markdown("""
            **Ejercicios Prácticos con Apu**: ¡Gracias, vuelve pronto! Soy Apu, y no te preocupes, te tengo preparado un surtido de ejercicios prácticos para que domines Git mejor que los precios en el Badulaque.
            """)

    st.markdown("")    
    st.markdown("")    
    st.markdown("")    
    st.markdown("¡Estamos emocionados de que te unas a nosotros en esta aventura Git al estilo de Springfield! Y recuerda, si Ralph ha podido aprender Git, tú también puedes, de todas maneras Nelson te ayudará a repasar ha-ha")


def comandos_basicos_terminal():
    st.markdown("<h1 style='text-align: center;'>¡Hazlo a lo Ralph! Guía Para No Derribar Todo en la Terminal🦖</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    Bienvenido a esta clase especial de comandos de terminal, ¡guiada por el mismísimo Ralph Wiggum! Si Ralph puede aprender esto (aunque piense que 'terminal' es un tipo de dinosaurio), tú también puedes. ¡Prepárate para aprender con los mejores ejemplos al estilo de Springfield!

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
    ls
    raptor.txt  tiranosaurio.jpg  velociraptor_cosas.txt  rosquillas
    ```
    Ralph se da cuenta de que no solo hay dinosaurios, ¡también hay rosquillas!, pero ¿qué es mejor buscar más dinosaurios o comerse una rosquilla? 🤷‍♂️
    
    #### Mostrar la Ruta del Directorio Actual (¡Para no Perderse!)
    Ralph suele perderse con facilidad, pero con este comando puede saber exactamente dónde está:
    ```bash
    pwd
    ```

    **Ejemplo:** Ralph quiere saber en qué carpeta está:
    ```bash
    pwd
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
    cd rosquillas
    pwd
    /home/springfield/dinosaurios/rosquillas
    ```
    Ralph ha llegado a la carpeta correcta y ahora puede disfrutar de sus rosquillas... hasta que Homer las descubra.

    📌 **Tip de Lisa:** Ralph, si alguna vez te pierdes de nuevo, recuerda que puedes "subir" a la carpeta anterior usando `cd ..`. Así es como funciona:
    
    **Ejemplo:** Si Ralph está en la carpeta `rosquillas` pero quiere volver a la carpeta `dinosaurios`:
    ```bash
    cd ..
    pwd
    /home/springfield/dinosaurios
    ```
    ¡Enhorabuena, Ralph! Has vuelto a la carpeta `dinosaurios` sano y salvo. Ahora puedes seguir buscando dinosaurios.
    """)

    st.image("images/ralph/ralph_carpetas_dinosaurios.jpeg", width=300, caption="¡Mira! Tengo carpetas de dinosaurios. Son muy fuertes y a veces tienen colas largas como... ¡mi papá!")

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
    mkdir habitacion_de_bart
    ls
    dinosaurios  chu-chu-chuly  habitacion_de_bart
    ```
    ¡Ralph ha creado una nueva habitación en la casa! Bart ahora tiene su espacio propio para hacer bromas sin molestar a Lisa... al menos por ahora.

    #### Crear Otras Habitaciones (¡La Casa Sigue Creciendo!)
    Ralph está en racha y decide que todos los Simpson necesitan su propia habitación. Ahora quiere construir una habitación para Lisa, otra para Homer y Marge (¡cerca de la nevera, claro!) y una para Maggie.

    **Ejemplo:** Ralph construye las demás habitaciones:
    ```bash
    mkdir habitacion_de_lisa
    mkdir habitacion_de_homer_marge
    mkdir habitacion_de_maggie
    ls
    dinosaurios  chu-chu-chuly  habitacion_de_bart  habitacion_de_lisa  habitacion_de_homer_marge_&_homer  habitacion_de_maggie
    ```
    La casa de los Simpson está tomando forma, y Ralph no podía estar más orgulloso.

    #### Eliminar un Directorio (¡Ups, Ralph Derriba una Habitación por Error!)
    Ralph, en su entusiasmo, construyó una habitación para el dinosaurio sin darse cuenta de que no era realmente necesaria. Ahora debe derribarla. Para eliminar un directorio (o "derribar una habitación", según Ralph), usa este comando:
    ```bash
    rm -r <nombre-del-directorio>
    ```

    **Ejemplo:** Ralph derriba la habitación del dinosaurio:
    ```bash
    rm -r dinosaurios
    ls
    chu-chu-chuly  habitacion_de_bart  habitacion_de_lisa  habitacion_de_homer_marge  habitacion_de_maggie
    ```
    La habitación del dinosaurio ya no está, pero Ralph sigue adelante con su proyecto.

    #### Advertencia de Marge: ¡Cuidado al Demoler Habitaciones!
    Marge se acerca a Ralph y le advierte que tenga cuidado al usar comandos para eliminar directorios. Es como cuando Homer entra a la cocina: si no tienes cuidado, todo podría desaparecer en un abrir y cerrar de ojos.

    📌 **Advertencia de Marge:** No uses `rm -rf` sin pensarlo dos veces, ya que podrías borrar toda la casa digital de los Simpsons (¡como cuando Homer se come una tarta entera en segundos!). Asegúrate de estar en el directorio correcto antes de borrar algo importante.

    #### Ejemplo de lo que NO debes hacer:
    Ralph está a punto de cometer un error. Intenta borrar la habitación de Homer, pero accidentalmente se encuentra en el directorio principal de la casa. Al usar `rm -rf *`, ¡podría borrar toda la casa de los Simpson!

    **Ejemplo Incorrecto:**
    ```bash
    rm -rf *
    ```

    Si Ralph ejecuta este comando desde el directorio principal, todos los archivos y directorios de la casa serán eliminados.

    **Resultado:**
    ```bash
    ls
    (nada...)
    ```
    ¡Oh no! Ralph ha borrado toda la casa de los Simpson por accidente. Marge se enfada, y Homer se queda sin su habitación y sin su preciada nevera.

    **Nota:** Asegúrate siempre de estar en el directorio correcto antes de eliminar algo. Un paso en falso puede tener consecuencias desastrosas.
    """)

    st.image("images/ralph/ralph_bart_constuctores.jpeg", width=300, caption="¡Construir es como jugar con espaguetis! ¡A veces se rompen, pero se ven tan ricos!")

    st.markdown("### 3. 📦 Gestión de Archivos con Bart y Sus Bromas: Ralph Aprende a Ser Travieso")
    st.markdown("""
    Ralph ha encontrado a su nuevo mejor amigo: ¡Bart Simpson! Bart es un experto en hacer bromas a la gente de Springfield, y ahora Ralph quiere aprender a hacer bromas usando la terminal. Vamos a enseñar a Ralph y Bart cómo gestionar archivos mientras preparan sus bromas.

#### Crear un Nuevo Archivo (¡Bart y Ralph Preparan una Broma!)
Bart le muestra a Ralph cómo crear archivos para sus bromas. Según el sistema operativo, el comando varía:

- **En Linux o macOS**: Puedes crear un archivo vacío con `touch`:
    ```bash
    touch <nombre-del-archivo>
    ```

    **Ejemplo:** Bart y Ralph crean un archivo llamado `broma_homer.txt`:
    ```bash
    touch broma_homer.txt
    ls
    broma_homer.txt travesuras_de_bart dinosaurios
    ```

- **En Windows**: Usan `New-Item` en PowerShell para hacer lo mismo:
    ```powershell
    New-Item -Path . -Name "broma_homer.txt" -ItemType "File"
    ```

    Ahora tienen un archivo listo para llenarlo de ideas graciosas. Ralph está emocionado porque Homer ni siquiera sospechará de la broma que están planeando.

    #### Copiar un Archivo (¡Bart y Ralph Multiplican Sus Bromas!)
    Bart le explica a Ralph cómo copiar un archivo para que las bromas puedan expandirse por todo Springfield. Usan este comando para copiar sus archivos de broma:
    ```bash
    cp <archivo_origen> <archivo_destino>
    ```

    **Ejemplo:** Bart y Ralph copian la broma de Homer para asegurarse de que llegue a todos los rincones de la casa:
    ```bash
    cp broma_homer.txt broma_homer_copia.txt
    ls
    broma_homer.txt  broma_homer_copia.txt  travesuras_de_bart  dinosaurios
    ```
    ¡Misión cumplida! Ahora tienen copias de su broma en varios directorios, por si alguna se pierde en el camino.

    #### Eliminar un Archivo (¡Bart y Ralph Borran las Evidencias!)
    Después de que una de sus bromas se sale de control (como suele pasar cuando Ralph está involucrado), necesitan borrar las pruebas rápidamente. Bart le enseña a Ralph cómo eliminar archivos para no ser atrapados:
    ```bash
    rm <nombre-del-archivo>
    ```

    **Ejemplo:** Bart y Ralph eliminan el archivo `broma_homer.txt` para que Homer no descubra su plan:
    ```bash
    rm broma_homer.txt
    ls
    broma_homer_copia.txt travesuras_de_bart  dinosaurios
    ```
    ¡Uf! El archivo ha sido eliminado justo a tiempo. Ralph suspira aliviado porque no quiere que Homer lo descubra.
                                
    #### Mover un Archivo (¡Bart y Ralph Ocultan las Bromas!)
    Ralph quiere esconder sus bromas y Bart le enseña a usar `mv` para mover los archivos a nuevos lugares, como cuando Bart esconde su tirachinas en la nevera:
    ```bash
    mv <archivo_origen> <destino>
    ```

    **Ejemplo:** Bart y Ralph mueven el archivo de broma de Homer a otro lugar en la casa para confundirlo aún más:
    ```bash
    mv broma_homer_copia.txt /casa_de_los_simpson/nevera/
    ls
    travesuras_de_bart  dinosaurios
    ```
    ¡Perfecto! El archivo ha sido movido a un lugar secreto. Ahora Homero jamás encontrará el archivo de la broma.

    📌 **Tip de Bart:** ¡Siempre es divertido mover los archivos! Solo asegúrate de recordar dónde los dejaste, o podrías perderlos para siempre...
                

     #### Leer el Contenido de un Archivo (¡Ralph Leyendo las Ideas de Bart!)
    Bart quiere mostrarle a Ralph sus ideas de bromas, así que usa el siguiente comando para leer el contenido del archivo:
    ```bash
    cat <nombre-del-archivo>
    ```

    **Ejemplo:** Bart lee el contenido de su archivo de brma_homer_copia.txt:
    ```bash
    cat broma_homer_copia.txt
    - Poner una bomba de ruido en la nevera de Homer.
    - Cambiar el shampoo de Lisa por pegamento.
    ```
    Ralph se ríe a carcajadas y ya está pensando en cómo llevar a cabo algunas de estas ideas locas como cambiar la pasta de dientes de Lisa por mayonesa: ¡Para que su boca tenga el mejor sabor a sándwich del mundo!""") 

    st.image("images/ralph/ralph_bart_bromas.jpeg", width=300, caption="¡Las bromas son como las galletas! ¡Siempre hay espacio para más, aunque me den un poco de tos!")

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
        {"Comando": "rm -r <directorio>", "Descripción": "Elimina un directorio (Ralph derriba la habitación del dinosario)."},
        {"Comando": "rm -rf *", "Descripción": "Elimina todo en el directorio actual (Ralph derriba todo como un tornado)."},
        {"Comando": "touch <archivo>", "Descripción": "Crea un nuevo archivo vacío en linux o macOs(Bart y Ralph preparan una broma)."},
        {"Comando": "New-Item -Path . -Name \"nombre-archivo\" -ItemType \"File\"", "Descripción": "Crea un nuevo archivo vacío en windows (Bart y Ralph preparan una broma)."},
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

    st.image("images/ralph/profe.jpeg", width=300, caption="¡Mira, una foto de mí siendo el mejor estudiante!")


    # Título de la conclusión
    st.markdown("""
    ## Terminamos ¡Chu-chu-chuly! 🚂""")
                    
    # Contenido de la conclusión
    st.markdown("""
    Acabamos de ver algunos comandos de terminal. Fue como un paseo en la montaña rusa, ¡pero sin la montaña! 

    Así que, cuando decimos `ls`, es como si estuviéramos buscando dinosaurios. Y cuando usamos `pwd`, es como decirle a mamá que no me perdí en el centro comercial. ¡Hola, mamá! 

    Y si alguien dice `rm -rf *`, ¡es como un monstruo que se come todos mis juguetes! ¡No, no! No dejeis que eso pase, es malo. 

    Y si quereis hacer un nuevo archivo, solo teneis que usar `touch`. Es como si Bart y yo estuviéramos haciendo una broma y tratando de hacer que desaparezca, pero... ¡no quiero que mis dibujos desaparezcan! 

    Pero no os preocupeis, porque la próxima vez Marge nos va a enseñar a configurar Git. ¡Espero que no sea un gato! ¡Hasta la próxima!
    """)


def configuracion_e_inicializacion_git():
    st.markdown("<h1 style='text-align: center;'>Cocinando Código: ¡Sazona tu Proyecto de Git con Marge!🍰</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    ¡Hola! Soy Marge Simpson, y hoy te llevaré a un viaje en el tiempo y el espacio, a través de las complejidades del mundo de Git. Piensa en esto como una de esas aventuras locas que la familia Simpson suele tener, pero esta vez, no se trata de evitar que Bart le haga una broma a Skinner en el colegio, sino de asegurarnos de que tus proyectos digitales estén perfectamente organizados.

    ### ¿Qué es Git?
    Imagina que estás en la cocina, donde cada receta es un proyecto. A veces, la cocina se convierte en un verdadero campo de batalla, con ingredientes volando y mi famoso pastel de manzana en riesgo de quemarse. ¡Ah, la vida en Springfield! Git es como ese viejo y buen libro de recetas que utilizo, que guarda cada pequeño cambio que hago. Cada vez que modifico un pastel, puedo volver y ver exactamente qué hice, evitando que todo se convierta en un desastre, como cuando Bart trató de hacer un pastel para mi cumpleaños y terminó usando kétchup como decoración.

    **Beneficios de Git:**
    - **Distribución**: Cada desarrollador tiene su propia copia del proyecto, ¡lo que significa que pueden trabajar sin preocuparse de que Lisa les interrumpa con preguntas sobre sus tareas!
    - **Velocidad**: Git es más rápido que Homer comiendo una krusty burguer; además, maneja proyectos grandes sin despeinarse.
    - **Colaboración**: Permite que todos trabajen juntos sin estorbarse, como en una cena familiar bien organizada. Cada uno tiene su rol, ¡y juntos logramos una comida espectacular… o una catástrofe!
    """)
    st.image("images/marge/marge_recetas_git.jpeg", width=300, caption="Las recetas de Git son como las mías: siempre hay un secreto para que queden perfectas!")


    st.markdown("""
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
    git config --global user.name "Marge Simpson"
    ```

    #### Configurar el Correo Electrónico
    Ahora, configuremos tu correo electrónico global, como poner tu dirección en una carta que enviarías a tus amigos para invitarlos a cenar:
    ```bash
    git config --global user.email "tuemail@example.com"
    ```

    **Ejemplo:** Asegúrate de que tus amigos puedan contactarte fácilmente, especialmente si alguna vez me piden la receta de mis galletas de chocolate:
    ```bash
    git config --global user.email "marge.simpson@example.com"
    ```

    #### Verificar la Configuración Actual
    Para asegurarte de que todo esté en orden, puedes usar el siguiente comando:
    ```bash
    git config --list
    ```

    **Ejemplo:** Verifica si tu firma está bien puesta, como cuando reviso la lista de ingredientes antes de hacer mis galletas:
    ```bash
    git config --list
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
    git config user.name "Marge Proyectos Especiales"
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
        {"Comando": "git config  user.name 'Tu Nombre'", "Descripción": "Configura el nombre de usuario local en Git."},
        {"Comando": "git config user.email 'tuemail@example.com'", "Descripción": "Configura el correo electrónico local en Git."},
    ]

    df_comandos_git = pd.DataFrame(comandos)
    st.dataframe(df_comandos_git, use_container_width=True)

    st.image("images/marge/marge_enseñando.jpeg", width=300, caption="La clave para aprender Git es practicar y no rendirse. ¡Como hacer una buena lasaña!")

    st.markdown("### 2. 🚀 Inicialización de Repositorios en GitHub")
    st.markdown("""
    Ahora que tienes todo configurado, ¡es hora de comenzar tu proyecto! Imagina que estás haciendo una nueva receta para una cena especial. Estoy aquí para guiarte en cada paso del camino.

    #### Paso 1: Crea el Repositorio en GitHub
    Primero, dirígete a [GitHub](https://github.com/) y crea un nuevo repositorio. Copia la URL del repositorio, como si estuvieras guardando una receta especial en tu libro de cocina. ¡Asegúrate de que la URL sea más sólida que la casa de los Simpson!

    #### Paso 2: Crea la Carpeta y Archivos Necesarios para tu Proyecto
    En tu terminal, navega hasta el lugar donde quieres comenzar tu proyecto y crea una nueva carpeta. Es como preparar el área de trabajo antes de empezar a cocinar mi famosa lasaña:
    ```bash
    mkdir mi_proyecto
    cd mi_proyecto
    ```

    #### Paso 3: Inicializa el Repositorio Git
    Ahora es el momento de dar el primer paso y preparar tu cocina:
    ```bash
    git init
    Initialized empty Git repository in /home/usuario/mi_proyecto/.git/
    ```

    #### Paso 4: Añade los Archivos al Índice
    Añade todos los archivos de tu proyecto, como agregar los ingredientes a tu mezcla de lasaña:
    ```bash
    git add .
    ```

    #### Paso 5: Realiza un Commit Inicial
    Realiza un commit inicial, como hacer la primera prueba de tu pastel. Asegúrate de que todo esté bien mezclado:
    ```bash
    git commit -m "versión 1 del proyecto"
    ```

    #### Paso 6: Renombra la Rama Principal a 'main'
    Renombra la rama principal para que suene más formal, como un menú especial en nuestra mesa. Esto es como asegurarme de que la decoración de la mesa esté a la altura:
    ```bash
    git branch -M main
    ```

    #### Paso 7: Vincula el Repositorio Local con GitHub
    Ahora añade la URL del repositorio que copiaste antes. Es como enviar tu receta a la familia para que la prueben:
    ```bash
    git remote add origin https://github.com/usuario/mi_proyecto.git
    ```

    #### Paso 8: Envía los Cambios al Repositorio Remoto
    Finalmente, envía tus cambios al repositorio remoto. Asegúrate de que todo esté en orden, como cuando verifico que todos los ingredientes estén listos para la cena:
    ```bash
    git push -u origin main
    ```

    📌 **Tip:** Asegúrate de tener permisos de escritura en el repositorio remoto. ¡No querrás tener problemas como cuando Bart y Lisa discuten por el control remoto!

    """)

    st.markdown("""
    ## Resumen de Comandos
    Aquí tienes un resumen de los comandos básicos para inicializar tu repositorio, como un recetario bien organizado que siempre debes tener a mano:
    """)

    comandos_inicializacion = [
        {"Comando": "git init", "Descripción": "Inicializa un nuevo repositorio Git en el directorio actual."},
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

    st.image("images/marge/marge_profe.jpeg", width=300, caption="Marge enseñando lo esencial de Git, ¡siempre con amor y paciencia!")

    st.markdown("""
    ### Conclusión al Estilo Marge: ¡Todo en su Lugar!
    ¡Y ahí lo tienes! Desde la configuración inicial hasta la creación de tu primer repositorio, ahora estás listo para sumergirte en el mundo de Git. Recuerda que, como en la cocina, la práctica es clave. Cada pequeño paso que tomas te acerca a convertirte en un maestro en este arte.

    Si tienes preguntas, ¡no dudes en preguntar! Estoy aquí para ayudarte, al igual que cuando ayudo a Bart y Lisa a hacer sus deberes (aunque eso a veces puede ser todo un desafío).

    ¡Feliz codificación y que disfrutes de tus proyectos tanto como disfruto yo de mis galletas de chocolate! 🍪
    """)


def operaciones_basicas():
    st.markdown("<h1 style='text-align: center;'>🍻Operaciones Básicas de Git con Homer🍩 </h1>", unsafe_allow_html=True)
    st.markdown("---")

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

    st.markdown("""
    ### 1. Clonar Repositorios
                
    Mmm… ¡software libre! Lo bueno de Git es que, si lo rompes, solo tú te das cuenta… ¡nadie te castiga! Ahora vamos a hablar de clonar repositorios. ¿Qué es eso? Bueno, imagina que tienes todas las rosquillas del mundo, y puedes hacer copias de ellas, ¡una para cada Homer del universo! O como diría yo, ¡mmmm... rosquillas!

    Clonar es como cuando veo una rosquilla en la tele y quiero otra en la mano. Es tener el mismo proyecto que está en internet, ¡pero ahora en tu ordenador! Así puedes hacer con él lo que quieras, sin que nadie te mire mal si metes la pata.

    #### ¿Por Qué Clonar un Repositorio?
    - **Colaboración**: Como en la planta nuclear, si todos tenemos el mismo clon, ¡podemos hacer nuestras "tareas" sin que se entere el Señor Burns!
    - **Acceso Completo**: Cuando Marge me hace la lista de las cosas que he roto, el historial de un repositorio te deja ver todo lo que ha pasado en el proyecto. Es como mirar cuántas duffs me he bebido sin que Marge enterarse.
    - **Desarrollo Local**: Puedes hacer lo que te dé la gana sin que nadie te diga nada. Y si te sale mal, solo le echas la culpa a Bart.

    #### Pasos para Clonar un Repositorio
    1. **Obtén la URL del Repositorio**: Es como cuando vas al bar de Moe y apuntas dónde está para que no se te olvide. Copia la URL del proyecto que quieres clonar.
    2. **Ejecuta el Comando para Clonar**: Abre esa cosa de la terminal (¡tranqui! No es tan difícil… si yo puedo, cualquiera puede) y pon esto:
        ```bash
        git clone <URL-del-repositorio>
        ```
        
        **Ejemplo:** Si quiero clonar un repositorio llamado `Git` desde GitHub, hago:
        ```bash
        git clone https://github.com/AlexCapis/Git.git
        ```
        
        📌 **Tip:** Si el repositorio es privado, necesitarás tu cuenta y acceso, como cuando Moe te deja a deber una cerveza en su bar ¡eso no es para todos, amigo!

    Y ya lo tienes, ¡eres todo un clonador! ¿Ves? Con este método puedes trastear con el código tanto como quieras, y si la cosa explota… nadie sabrá que fuiste tú, porque tienes tu propio clon. ¡D'oh!

    """)

    st.image("images/homer/clonar.jpeg", caption="¡Clones de Homers por todas partes! Las rosquillas del mundo tiemblan.", width=300)


    # Sección de Añadir y Eliminar Archivos
    st.markdown("""
    ### 2. Añadir y Eliminar Archivos
    *Mmm... ¡añadir archivos es como añadir más rosquillas a mi colección! Siempre hay espacio para más... y si necesito quitar alguno, es solo porque quiero espacio para algo aún mejor.*

    Con Git, puedo **añadir archivos** al área de staging, y cuando ya no quiero más (aunque eso nunca pasa con las rosquillas), también puedo **eliminarlos**. Así mantengo mi repositorio limpio y organizado... o al menos lo intento.

    #### Añadir Archivos al Repositorio
    Para añadir nuevos archivos al área de staging (o, como yo diría, ¡a mi stash de rosquillas!), usa este comando:
    """)

    st.code("git add <archivo>", language='bash')

    st.markdown("""
    **Ejemplo:** Creé un archivo de receta de rosquillas llamado `Receta_Rosquilla.txt`. ¡Lo quiero en mi repositorio para consultarlo cuando quiera! Entonces escribo:
    """)

    st.code("git add Receta_Rosquilla.txt", language='bash')

    st.markdown("""
    #### Eliminar Archivos del Repositorio
    Pero si algún día decido que ya tengo suficientes recetas y necesito espacio para más (¡como si eso pasara!), puedo **eliminar un archivo** que ya no necesite. Para eso, uso `git rm`:
    """)

    st.code("git rm <archivo>", language='bash')

    st.markdown("""
    **Ejemplo:** Digamos que tengo una receta de pizza en el archivo `Receta_Pizza.txt`... pero la verdad es que prefiero enfocarme en las rosquillas. Así que para eliminarlo, escribo:
    """)

    st.code("git rm Receta_Pizza.txt", language='bash')

    st.markdown("""
    📌 **Tip de Chef Homer:** Si solo quiero quitar el archivo del área de staging, pero aún conservarlo en mi pc (por si decido que realmente lo quiero), uso `git reset HEAD <archivo>` en lugar de `git rm`.

    **Ejemplo:** Me arrepiento un poco de añadir `Receta_Rosquilla.txt` al área de staging porque quiero revisarla un poco más. Así que, para sacarlo del staging y seguir trabajándolo, hago esto:
    """)

    st.code("git reset HEAD Receta_Rosquilla.txt", language='bash')

    st.markdown("""
    Esto mantiene el archivo en mi directorio de trabajo, pero lo elimina del área de staging, como si nada hubiera pasado. ¡Nadie me quita mis rosquillas!
    """)

    # Imagen asociada a Añadir y Eliminar Archivos
    st.image("images/homer/homer_comiendo_rosquillas.jpeg", caption="Añadir archivos es como tener más rosquillas... ¡nunca es suficiente!", width=300)

    # Sección de Hacer Commits y Ver Historial
    st.markdown("""
    ### 3. Hacer Commits y Ver Historial
    *Mmm... hacer commits es como guardar mis mejores momentos en un álbum de recuerdos. Cada cambio es como una nueva página en mi historia, ¡y puedo ver cómo ha crecido mi colección con el tiempo!*

    Con Git, cada commit es una oportunidad de **guardar el estado de tu proyecto** en un momento específico, como si estuvieras haciendo una captura de pantalla de tus avances. Y cuando quieras revivir esos momentos, puedes ver el historial de commits para ver cada cambio guardado.

    #### Hacer un Commit
    Para capturar esos momentos importantes en el repositorio, usa el comando `git commit` junto con un mensaje que explique el cambio.
    """)

    st.code("git commit -m \"Mensaje del commit\"", language='bash')

    st.markdown("""
    **Ejemplo:** Digamos que acabo de añadir una receta súper secreta de rosquillas... ¡definitivamente merece ser parte de mi historia! Para guardar este momento, escribiría:
    """)

    st.code("git commit -m \"Añadida nueva receta de rosquilla\"", language='bash')

    st.markdown("""
    #### Ver el Historial de Commits
    Ahora, ¿qué pasa si quiero ver todos los momentos que he guardado? Para eso está el comando `git log`. Con él, puedo revisar cada paso que he dado.
    """)

    st.code("git log", language='bash')

    st.markdown("""
    **Ejemplo:** Quiero ver todas mis hazañas y recetas guardadas, así que uso:
    """)

    st.code("git log", language='bash')

    st.markdown("""
    📌 **Tip Rápido:** Para ver un historial más compacto, como si fuera un resumen de mis aventuras, usa `git log --oneline`. Esto te mostrará solo los mensajes de cada commit, ¡perfecto para una vista rápida de tu historia de cambios!

    **Ejemplo:** Digamos que quiero ver un resumen sin entrar en detalles, entonces puedo escribir:
    """)

    st.code("git log --oneline", language='bash')

    st.markdown("""
    Esto me dará un resumen más breve y directo, ideal para cuando quiero recordar mis mejores momentos sin revisar cada detalle.
    """)

    # Imagen asociada a Hacer Commits y Ver Historial
    st.image("images/homer/recuerdos.jpeg", caption="Revisar el historial de commits es como recordar mis mejores aventuras... ¡me encanta!", width=300)

    # Sección de Actualizar y Sincronizar Repositorios
    st.markdown("""
    ### 4. Actualizar y Sincronizar Repositorios
    *¿Sabes? Actualizar mi repositorio es como recibir una nueva temporada de mi serie favorita... ¡Siempre quiero estar al día con lo que pasa en Springfield! Así que cuando alguien agrega algo nuevo, necesito actualizar mi colección.*

    Para trabajar en equipo con Git, es esencial que tu repositorio local esté sincronizado con el remoto. Aquí vamos a ver cómo hacerlo:

    #### Actualizar el Repositorio Local
    Cuando alguien en tu equipo, como Bart, añade algo nuevo, puedes descargar y fusionar esos cambios a tu repositorio local usando el comando `git pull`como por ejemplo cuando me enteré de que Bart añadió nuevas recetas a nuestra colección y quiero traerlas a mi repositorio para probarlas yo también.
    """)

    st.code("git pull", language='bash')

    st.markdown("""
    #### Enviar Cambios al Repositorio Remoto
    Por supuesto, si yo quiero compartir una de mis recetas (como la de mi famosa rosquilla doble), uso `git push` para enviar mis cambios al repositorio remoto y que todos puedan disfrutarlo como por ejemplo si quiero que Bart y el resto de Springfield puedan ver y probar mi receta, ¡envío mis cambios con:
    """)

    st.code("git push", language='bash')

    st.markdown("""
    #### Verificar el Estado del Repositorio
    Y antes de enviar cualquier cambio, siempre verifico que todo esté en orden con `git status` y me permite ver si hay algo pendiente o sin guardar. Como siempre soy un poco curioso (y a veces un poco despistado), reviso mi estado actual usando: 
    """)

    st.code("git status", language='bash')

    st.markdown("""
    #### Estado Compacto del Repositorio
    Si quiero ver el estado en un formato más corto, uso `git status -s`, que es como ver solo el resumen.
    """)

    st.code("git status -s", language='bash')

    st.markdown("""
    📌 **Recuerda:** Usa `git status` sin la opción `-s` si necesitas un estado más detallado y  `git status -s` si quieres un resumen.
    """)

    # Imagen asociada a Actualizar y Sincronizar Repositorios
    st.image("images/homer/tele.jpeg", caption="Mantenerme al día con los cambios es como descubrir una nueva temporada en mi amada tele", width=300)

    # Sección de Crear Alias para Comandos
    st.markdown("""
    ### 5. Crear Alias para Comandos
    *A veces me canso de escribir tanto, como cuando me canso de esperar a que cocinen mis rosquillas. Crear alias es como tener atajos directos a las cosas importantes... ¡así no pierdo tiempo y puedo volver a lo que realmente me interesa!*

    Con los alias, puedo reducir los comandos largos a algo breve y directo. ¡Ahora soy más rápido con Git y sigo siendo Homer!

    #### Cómo Crear un Alias
    Para hacer un alias, usa el comando `git config` y asígnale un nombre fácil de recordar al comando de Git que quieras abreviar.
    """)

    st.code("git config --global alias.<alias> '<comando>'", language='bash')

    st.markdown("""
    **Ejemplo:** 
    Imaginemos que quiero ver el estado de mi repositorio sin escribir `git status` cada vez. Puedo abreviarlo con el alias `s` de la siguiente forma:
    """)

    st.code("git config --global alias.s 'status'", language='bash')

    st.markdown("""
    Ahora, cada vez que quiera ver el estado, solo tengo que escribir `git s`. ¡Es como tener un botón directo para la rosquilla perfecta!

    #### Alias Útiles
    Aquí tienes algunos alias que podrían gustarte:
    - `git config --global alias.che 'checkout'`: Usa `git che` en lugar de `git checkout`.
    - `git config --global alias.br 'branch'`: Usa `git br` para ver tus ramas.
    - `git config --global alias.co 'commit'`: Usa `git co` para hacer un commit rápido.

    ¡Estos atajos hacen que usar Git sea casi tan fácil como alcanzar una rosquilla!
    """)

    # Imagen de Homer riéndose delante del ordenador
    st.image("images/homer/homer_riendose_ordenador.jpeg", caption="¡Los alias me facilitan la vida!", width=300)

    # Título de la aplicación
    st.title("¡D'oh! Resumen de Comandos de Git")

    # Introducción
    st.write("""
        Bienvenidos a mi increíble guía de comandos de Git. Aquí aprenderás los comandos iniciales del control de versiones 
        con la misma destreza que yo domino el sofá. ¡Vamos a sumergirnos en el delicioso mundo de Git, 
        donde cada commit es como una rosquilla que no quieres perder!
    """)


    # Datos de los comandos
    data = {
        "Comando": [
            "git clone [url]",
            "git add [archivo]",
            "git rm [archivo]",
            "git reset HEAD [archivo]",
            "git commit -m 'mensaje'",
            "git log",
            "git log --oneline",
            "git pull",
            "git push",
            "git status",
            "git status -s",
            "git config --global alias.[alias] [comando]",
        ],
        "Descripción": [
            "Crea una copia local de un repositorio remoto. ¡Es como tener una nevera llena de donas en casa!",
            "Agrega cambios específicos de un archivo al área de preparación. ¡Como poner tu sabor de dona favorito en la lista de compras!",
            "Elimina un archivo del directorio de trabajo y del área de preparación. ¡Adiós, archivo, nunca serás olvidado... o tal vez sí!",
            "Deshace el último 'git add'. Es como arrepentirte de comer esa última dona y decidir que no era una buena idea.",
            "Crea un nuevo commit con los cambios en el área de preparación. ¡Es como contarle a todos lo genial que eres cada vez que comes una dona!",
            "Muestra el historial de commits del repositorio. ¡Es como ver el álbum familiar, pero sin las fotos embarazosas!",
            "Muestra un resumen conciso del historial de commits. ¡Rápido y directo, como yo cuando veo una caja de donas!",
            "Actualiza la rama local con los cambios del repositorio remoto. ¡Recibe las novedades como si fueran las últimas noticias sobre donas!",
            "Envía los cambios de la rama local al repositorio remoto. ¡Como lanzar una dona al aire y esperar que caiga justo en tu boca!",
            "Muestra el estado actual del repositorio. ¡Te dice si estás en el camino correcto o si necesitas más donas para seguir!",
            "Proporciona una salida abreviada del estado del repositorio. ¡Es como un '¿todo bien?' pero sin el compromiso de preguntar!",
            "Crea un alias global para un comando de Git. ¡Es como apodar a tu mejor amigo, pero en lugar de eso, le pones un nombre a tu comando!",
        ],
    }

    # Crear un DataFrame
    df = pd.DataFrame(data)

    # Mostrar los comandos en formato de tabla
    st.subheader("Tabla de Comandos de Git")
    st.dataframe(df)

    # Imagen de Homer riéndose delante del ordenador
    st.image("images/homer/profe.jpeg", caption="¡El maestro del control de versiones!", width=300)


    # Sección de conclusión
    st.markdown("### 🍩 ¡Cierre Rosquilloso! 🍩")
    st.write("""
        ¡Woo-hoo! Hemos llegado al final de nuestra sección sobre los comandos de Git. Recuerda, cada vez que haces un commit, es como guardar una rosquilla para más tarde (¡mmm, rosquillas!). ¡Siempre es bueno tener una a mano para esos días en los que todo se vuelve un lío!

        Pero espera, ¡no te vayas todavía! Ahora le toca a Bart para hablarte sobre las ramas de Git. ¡Es como cuando intenté encontrar el camino de regreso a casa después de un mal día en el trabajo, pero con menos enredos y más diversión! 

        Así que ponte cómodo, relájate y prepárate para aprender algo nuevo. ¡No te preocupes! Bart no lanzará un libro, solo algunas ramas de Git que son más interesantes que los discursos de Lisa. ¡D'oh!
    """)

def ramas_colaboracion():
    # Título y estilo
    # st.markdown("<h1 style='text-align: center; color: #FFA500;'>🌿 Ramas y Colaboración con Bart y El Barto 🛹</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>🤣Ramas y Colaboración con Bart Simpson 🛹</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Introducción de Bart
    st.markdown("""
    ¡Qué pasa, troncos! Soy Bart Simpson y hoy os voy a enseñar a usar Git, ¡a lo Bart! Vais a crear ramas y colaborar como auténticos pros... o al menos lo bastante bien como para que hasta el señor Skinner alucine. Si seguís mis pasos, ¡seréis los reyes de Git en menos de lo que se tarda en decir “Ay, caramba!”.
    """)

    # Contenido
    st.markdown("""
    ### Contenido
    1. 🌿 **Crear y Gestionar Ramas**
    2. 🔀 **Hacer Merges y Resolver Conflictos (como cuando la lio en la escuela)**
    3. 🤝 **Estrategias para Trabajar en Equipo sin Volverse Loco**
    """)

    # Sección de Crear y Gestionar Ramas
    st.markdown("### 1. 🌿 Crear y Gestionar Ramas")
    st.markdown("""
    Imaginad que tengo varios proyectos secretos en marcha, y necesito que cada uno esté bien separado para que no se mezclen entre ellos. Por ejemplo, tengo:

    - Un proyecto para fastidiar al señor Skinner (ya sabéis, lo típico).
    - Otro para hacerle bromas a Lisa sin que se dé cuenta.
    - Y un tercero para pasar el rato con Milhouse haciendo locuras.

    Cada misión necesita su propia **rama** para que no se líe nada y pueda ser el maestro de cada plan. Así no mezclo las cosas y evito que mamá o Homer descubran alguno de mis planes. 😎
    """)

    # Crear una Nueva Rama
    st.markdown("#### Crear una Nueva Rama")
    st.markdown("Si tengo una nueva idea, ¡necesito su propia rama! Así, puedo hacer de las mías sin estropear los otros planes. Míralo así:")
    st.code("git branch plan-skate", language="bash")
    st.markdown("""
    Con `git branch plan-skate`, me hago una rama solo para mis aventuras de skate, ¡así no se mezclan con mis bromas para Skinner, Lisa o para pasar tiempo con Milhouse!
    """)

    # Cambiar a una Rama Diferente
    st.markdown("#### Cambiar a una Rama Diferente")
    st.markdown("Ahora que tengo mi nueva rama, ¡vamos a ella! Para meterme de lleno en esa rama y empezar con el lío, solo uso:")
    st.code("git checkout plan-skate", language="bash")
    st.markdown("""
    Con `git checkout plan-skate`, me meto en la nueva rama y puedo planear mis trucos de skate sin liarla con mis otros planes. Es como ponerme un nuevo disfraz para cada broma que tengo en mente. 🛹
    """)

    # Crear y Cambiar a una Nueva Rama en un Solo Paso
    st.markdown("#### Crear y Cambiar a una Nueva Rama en un Solo Paso")
    st.markdown("Si quiero ahorrar tiempo y ser más rápido que Marin escapandose de Nelson, hago todo en un solo paso:")
    st.code("git checkout -b broma-nueva", language="bash")
    st.markdown("""
    Con `git checkout -b broma-nueva`, creo y entro en la nueva rama `broma-nueva` al mismo tiempo. ¡Rápido y sencillo, como las mejores bromas!
    """)

    # Ver todas las Ramas
    st.markdown("#### Ver todas las Ramas")
    st.markdown("Para asegurarme de que no he perdido ni una sola broma (ni rama), hago un repaso general:")
    st.code("git branch", language="bash")
    st.markdown("""
    Con `git branch`, veo todas las ramas que he creado. Así, puedo recordar cuál es cuál y no mezclo las cosas... ni mis ideas más locas.
    """)

    # Tips
    st.markdown("📌 **Tip de Bart:** Dale nombres divertidos a tus ramas, algo como `broma_lisa_super_pegajosa`, ¡así siempre sabes de qué va cada una!")
    st.markdown("📌 **Tip extra:** Si alguna broma ya pasó de moda (o está más quemada que una rosquilla en la fritura de Homer), la elimino así:")
    st.code("git branch -d idea_vieja", language="bash")
    st.markdown("¡Así mis planes siempre están frescos y listos para usarse!")

    # Imagen de Bart haciendo skate
    st.image("images/bart/ramas.jpeg", caption="Bart en una de sus locas aventuras", width=300)



    # Sección de Merges y Conflictos
    st.markdown("### 2. 🔀 Realizar Merges y Resolver Conflictos")
    st.markdown("""
    Imaginad esto: llevo todo el día currándomelo en mi proyecto de skate, añadiendo trucos nuevos, mejorando los saltos, y ahora quiero que todos vean mis avances. Pero antes de enseñarlo al mundo (o sea, a mis colegas y a Lisa, para que flipe), necesito combinar mi proyecto de skate (`aventura-skate`) con el proyecto principal (`main`). ¡Es hora de hacer un **merge** y mezclarlo todo!
    """)

    # Realizar un Merge
    st.markdown("#### Realizar un Merge")
    st.markdown("""
    Para hacer que el merge funcione y que mis mejoras de skate pasen al equipo principal, primero tengo que asegurarme de estar en la **rama principal** (`main`). Esto es como cuando estás en casa y te preparas para salir a lo grande:
    """)
    st.code("git checkout main", language="bash")
    st.markdown("""
    Ahora que estoy en `main`, listo para la acción, hago el merge. Con este comando, uno mi `aventura-skate` con la rama principal, como si juntara todas mis ideas de skate en un solo gran truco:
    """)
    st.code("git merge aventura-skate", language="bash")
    st.markdown("""
    Con `git merge aventura-skate`, mezclo mis increíbles trucos de skate con el proyecto principal. Esto es como si estuviera mostrando a todos en Springfield lo genial que soy. 
    Lisa no volverá a decir que soy un pringado. ¡Va a flipar! 
    """)

    # Resolver Conflictos (Opcional)
    st.markdown("#### Resolver Conflictos (si es que los hay)")
    st.markdown("""
    A veces, cuando uno se pasa el día añadiendo trucos nuevos, puede que la cosa se complique y Git no sepa qué cambios son los buenos. Esto se llama **conflicto** (sí, como cuando Homer se cabrea porque he gastado demasiado llamando al bar de Moe para hacer bromas).

    Si hay un conflicto, Git me lo dirá, y tendré que elegir cuál versión es la mejor: ¿mi versión loca de Bart o una versión más suave para que todos estén contentos? Para resolverlo, abro el archivo en conflicto, reviso y decido qué cambios se quedan y cuáles se van. Luego, cuando esté satisfecho, hago:
    """)
    st.code("git add archivo_conflicto", language="bash")
    st.code("git commit -m 'Conflicto resuelto, todos felices'", language="bash")
    st.markdown("""
    Y listo, los conflictos se van y todo vuelve a estar bajo control. ¡Ahora sí, mis trucos de skate están listos para ser vistos por el mundo!
    """)

    # Imagen de Bart 
    st.image("images/bart/conflicto_ramas.jpeg", caption="¡Ay, caramba! ¡Pelea de ramas, LISAAA!", width=300)


    # Sección de Estrategias de Colaboración
    st.markdown("### 3. 🤝 Estrategias de Colaboración en Proyectos")
    st.markdown("""
    Trabajar solo mola, pero hacerlo con amigos... ¡es lo máximo! Para que nuestras aventuras sean aún más épicas, os enseño cómo colaborar sin que acabemos en una pelea estilo “Bart vs. Lisa”. ¡Vamos a currar en equipo como auténticos cracks! 
    """)

    # Uso de Pull Requests
    st.markdown("#### Uso de Pull Requests")
    st.markdown("""
    Antes de unir mis trucos locos a la rama principal, pido a mis colegas que los revisen. **Pull Request (PR)** es como decir: “Eh, Milhouse, ¿qué opinas de este salto?”  
    Con un PR explico mis movidas, escucho sugerencias y evito meter la pata. ¡Cero drama, cien por cien flow!  
    """)

    # Revisión de Código
    st.markdown("#### Revisión de Código")
    st.markdown("""
    Aquí hacemos sesiones de **revisión de código**. Es como reunirnos en la tienda de cómics: cada quien aporta algo, y al final tenemos los mejores trucos para enseñar en el parque.  
    Mis amigos pueden decir: "Bart, esta pirueta necesita más giro". ¡Y yo lo acepto porque... bueno, puede que tengan razón!  
    Las revisiones evitan que acabemos con un código peor que las notas de Ralph en matemáticas (1 + 1 = Unicornio)
    """)

    # Integración Continua
    st.markdown("#### Integración Continua")
    st.markdown("""
    Si no quieres que tu proyecto acabe más destrozado que la bici de Milhouse después de una bajada, necesitas **CI/CD**.  
    Con herramientas como **Jenkins**, automatizo pruebas y me aseguro de que todo funcione. Así, cada cambio pasa el control de calidad y no nos llevamos sustos. ¡Control máximo sin perder el flow!
    """)

    # Consejos y Tip
    st.markdown("""📌 **Tip Bartiano:** Crea **nombres guays para los commits** y usa un flujo como **GitFlow**. Por ejemplo, en lugar de “update files”, di:  
    “¡Nuevo salto 360º en skate, listo para el parque!”  
    Así todo queda claro, ordenado y, lo mejor de todo... ¡mola un montón!""")

    # Imagen de Bart revisando código con sus amigos
    st.image("images/bart/revisar_codigo.jpeg", caption="Bart y sus colegas mejorando sus trucos... y su código. ¡Más épico que un triple kickflip!", width=300)

    # Título de la sección
    st.markdown("### Resumen de Comandos: ¡Git al Estilo Bart!")

    # Introducción
    st.markdown("""
    ¡Ey, troncos! Después de un día de bromas, skate y, claro, unas cuantas líneas de código, os dejo un buen resumen. Con estos comandos, podréis crear ramas para vuestras locuras, resolver líos y colaborar como auténticos cracks. Apunta esto, porque así nadie os podrá decir: “¡Ay, caramba! ¿Qué hiciste en el código?”
    """)

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
            "🔧 Crea una nueva rama para tus bromas (o trucos épicos).",
            "🏄 Cambia de rama como quien cambia de pista en el parque.",
            "🚀 Crea y cambia a una rama nueva de una sola vez, ¡sin frenos!",
            "🗺️ Mira todas las ramas disponibles, como si planearas tu próxima ruta de bromas.",
            "🔀 Mezcla dos ramas en una, ¡como si fusionaras dos megasaltos en el skate!",
            "🛠️ Marca los archivos que resolviste para que todo esté listo para la acción.",
            "💾 Guarda tus cambios y deja claro que el lío está resuelto. ¡Pro en todo sentido!",
            "🗑️ Borra ramas que ya no necesitas, como trucos que ya no te impresionan."
        ]
    }

    df = pd.DataFrame(data)

    # Mostrar la tabla usando Streamlit
    st.table(df)

    # Imagen de Bart revisando código con sus amigos
    st.image("images/bart/profe.jpeg", caption="Bart enseñando Git: '¡Ya podéis decir que sois expertos en ramas y bromas!'", width=300)


    # Sección de conclusión
    st.markdown("### 🏁 ¡Hasta la Vista, Ramas!")
    st.markdown("""
    ¡Ey, troncos! Después de todas estas locuras con Git, me siento como el rey del parque. Ahora sé cómo crear ramas, resolver líos y trabajar en equipo sin romper nada (bueno, *casi* nada). Pero esto no es el final... ¡es solo el principio!  

    Como buen rebelde, sé que todavía hay mucho por aprender. Y, aunque yo sea el más molón, Lisa dice que vienen **comandos avanzados** que son como trucos ninja. Así que prepárate, porque en la próxima aventura vamos a deslizarnos por el lado pro de Git.  

    ¡Nos vemos en la siguiente rama, cracks! 🤘😜
    """)

def avanzado_git():
    st.markdown("<h1 style='text-align: center;'>🔬 Las Aventuras de Lisa en el Mundo Avanzado de Git 🔬</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("""
    ¡Hola, mentes brillantes del código! Soy Lisa Simpson y voy a guiarte por las partes más avanzadas de Git, esas herramientas mágicas que hacen que todo funcione como un saxofón bien afinado. 🎷  
    ¿Listo para llevar tu flujo de trabajo a otro nivel? Aquí vas a descubrir cómo mantener todo en orden, resolver problemas y hasta impresionar a tus compañeros de equipo. ¡Vamos allá!  

    ### Contenido
    1. 🔄 **Rebase**
    2. 🗂️ **Stash**
    3. 🍒 **Cherry-Pick**
    4. 🚨 **Reset**
    5. 📜 **Diff y Reflog**
    6. 🏷️ **Tag**
    """)

    st.markdown("### 🔄 Rebase")
    st.markdown("""
    Recordáis esa vez en que intenté que la familia Simpsons participara en un día educativo de ciencias, pero Homer acabó interrumpiendo con su versión de 'Música para Dormir'? 🎶 Bueno, usar rebase es como lograr que todos sigan al ritmo de tu proyecto, sin interrupciones y manteniendo un flujo de trabajo ordenado.

    ```bash
    git rebase <rama-base>
    ```
 
    Imagina que estás trabajando en un proyecto de ciencias, y tu maestro, el Sr. Skinner, ha añadido algunos cambios importantes en main. Lo primero es asegurarte de estar en tu rama de trabajo (por ejemplo, feature) con: 
    1. Cambia a tu rama de trabajo:  
       ```bash
       git checkout feature
       ```  
    2. Actualiza tu rama con los cambios de `main`:  
       ```bash
       git rebase main
       ```  

    Después, al aplicar `git rebase main`, tomas todos los cambios recientes en `main` y los integras en tu rama actual, como si pidieras prestadas las últimas notas del Sr. Skinner para que tu proyecto esté actualizado.

    📌 **Tip de Lisa:** Mantén tu historial de trabajo tan claro y organizado como un buen cuaderno de apuntes. ¡Recuerda que un rebase bien hecho es como una página sin borrones!   
    """)
    st.image("images/lisa/informacion.jpeg", caption="Compartir información es clave. Recuerda, el conocimiento se multiplica cuando lo compartes con los demás!", width=300)

    st.markdown("### 🗂️ Stash")
    st.markdown("""
    Imagina que estás trabajando en un emocionante proyecto de investigación sobre el medio ambiente y tomando notas súper importantes, cuando de repente Bart entra pidiendo ayuda porque tiene un problema.

    Así que, ¿qué haces? Bueno, `git stash` es como una caja especial donde puedes guardar todo lo que estabas haciendo, para dejarlo en pausa sin perder nada, como cuando guardo mi saxofón para concentrarme en un examen complicado.

    #### Paso 1: Guardar los Cambios con `git stash`
    Primero, usamos el comando `git stash` para guardar tus cambios en un lugar temporal:
    ```bash
    git stash
    ```
    Ahora tus cambios están seguros, como si los hubieras puesto en una caja con tu nombre. ¡Puedes ir a ayudar a Bart sin preocuparte por perder nada!

    #### Paso 2: Cambiar a la Rama Principal con `git checkout main`
    ```bash
    git checkout main
    ```
    Este comando es como si estuvieras cambiando de clase: necesitas ir a la rama `main`, o "clase principal", antes de empezar cualquier otra cosa. Cambiar a `main` es importante si quieres trabajar en otra cosa sin mezclar lo que ya tienes en tu rama actual.

    #### Paso 3: Recuperar Cambios Guardados con `git stash apply` y `git stash pop`
    Después de ayudar a Bart, vuelves a tu proyecto de investigación. ¡Es momento de recuperar tus notas! Para ello, tienes dos opciones:

    - **`git stash apply`**: Este comando saca tus cambios de la caja y los coloca en tu trabajo actual sin eliminarlos del "cajón de stashes", por si quieres volver a usarlos.
    - **`git stash pop`**: Este comando es como sacar los cambios de la caja y borrar la caja. Úsalo si estás seguro de que ya no necesitas guardar una copia de esos cambios.

    ```bash
    git stash apply
    git stash pop
    ```

    #### Paso 4: Volver a la Rama de Trabajo con `git checkout feature`
    Una vez que tienes tus cambios, asegúrate de estar en la rama donde trabajabas originalmente, en este caso, `feature`:
    ```bash
    git checkout feature
    ```
    Este paso es crucial para retomar el trabajo donde lo dejaste. Así, es como regresar al mismo escritorio en la biblioteca después de ayudar a Bart.

    📌 **Tip de Lisa:** Usa `git stash list` para ver todos los cambios que guardaste con `stash`. ¡Es como revisar tus notas para saber qué proyectos tienes pendientes!
    """)
    st.image("images/lisa/saxo.jpeg", caption="La programación y la música tienen algo en común: ¡hay que encontrar el ritmo!", width=300)


    # Título de la sección
    st.markdown("### 🍒 Cherry-Pick con Lisa Simpson")

    # Introducción al comando cherry-pick
    st.markdown("""
    A continuación, te enseñaré cómo usar `cherry-pick`, un comando especial de Git.  Es como cuando elijo las mejores cerezas del árbol 🍒, o las respuestas más brillantes en clase. `Cherry-pick` te permite traer solo esos cambios clave de otra rama, sin tener que arrastrar todo.  
    """)

    # Comando de cherry-pick
    st.markdown("#### Comando de Cherry-Pick")
    st.code("""
    git cherry-pick <id-del-commit>
    """, language="bash")

    # Ejemplo de cherry-pick contextualizado
    st.markdown("""
    Supón que encontré un descubrimiento genial sobre la fotosíntesis en la rama `investigaciones`. Quiero llevar ese hallazgo a la rama principal (`main`) de mi proyecto, ¡pero sin traer otros cambios extra!  
    """)
    st.code("""
    git checkout main
    git cherry-pick a1b2c3d4
    """, language="bash")

    # Explicación detallada
    st.markdown(""" 
    - Primero, uso `git checkout main` para asegurarme de que estoy en la rama `main`, que es donde quiero añadir este cambio especial.  
    - Después, con `git cherry-pick a1b2c3d4`, recojo solo ese commit importante, como si tomara la mejor cereza del árbol.  
   
     Así, llevo mi descubrimiento sobre la fotosíntesis directo a `main` sin mezclar nada más.  

    📌 **Tip:** ¡Es perfecto para elegir justo lo que necesitas, como cuando escojo los datos más interesantes en mis proyectos de ciencias! 💡  
    """)

    # Imagen contextual
    st.image("images/lisa/lisa_cherry.jpeg", caption="Las ideas brillantes son como cerezas, ¡se disfrutan mejor en grupo!", width=300)

    # Título e introducción de Lisa para el comando Reset
    st.markdown("### 🔄 Reset")

    st.markdown("""
    Esta vez quiero mostrarte cómo `git reset` es como tener una máquina del tiempo ⏳. Es una herramienta perfecta para volver a un momento anterior en tu proyecto.  A veces, cuando estamos experimentando, nos damos cuenta de que necesitamos retroceder a un punto seguro en nuestro camino.  `git reset` nos lleva atrás en el tiempo, como si viajáramos al pasado para arreglar algo sin que nadie lo note.  
    """)

    # Comando de Reset con explicación del uso "hard"
    st.markdown("#### Comando de Reset con `--hard`")
    st.code("""
    git reset --hard <commit-id>
    """, language="bash")

    st.markdown(""" 
    Supón que estuviste trabajando en un proyecto de ciencias, pero el último experimento no salió como esperabas. Decides que lo mejor es regresar a un estado donde todo estaba bien:  
    """)
    st.code("""
    git reset --hard a1b2c3d4
    """, language="bash")

    # Explicación del ejemplo
    st.markdown(""" 
    - Usando `git reset --hard`, retrocedes a un momento en el tiempo, donde todo estaba como lo querías.  
    - **¡Advertencia!** ❌ Con `--hard`, todos los cambios no confirmados que hayas hecho desaparecerán, ¡así que úsalo con cuidado!  

    #### Comando de Reset Suave con `--soft`  
    Si quieres volver en el tiempo pero conservar tu información:  
    """)
    st.code("""

    git reset --soft HEAD~1
    """, language="bash")

    st.markdown(""" 
    Si el último paso en tu experimento fue un error, pero aún quieres conservar los datos que anotaste, puedes usar `git reset --soft` para retroceder sin perder nada:  
    """)
    st.code("""
    git reset --soft HEAD~1
    """, language="bash")

    # Explicación del reset suave
    st.markdown("""
    - Con `git reset --soft HEAD~1`, eliminas el último cambio pero mantienes tus notas y datos.  
    
    Es como si pudieras borrar solo una pizarra sin perder la información, lista para escribir de nuevo en limpio.  

    📌 **Tip:** Usa `git reset --hard` solo si estás seguro de que quieres eliminar esos cambios, igual que si viajaras al pasado y estuvieras listo para empezar de cero. ⚖️  
    """)

    # Imagen de Lisa con la máquina del tiempo
    st.image("images/lisa/lisa_maquina_tiempo.jpeg", caption="Si tuviéramos una máquina del tiempo para deshacer esos errores...", width=300)

    # Título y separación de secciones
    st.markdown("### 🔍 Diff y 📖 Reflog")

    # Explicación de Diff
    st.markdown("#### Comando de Diff")
    st.markdown("""
    A veces, cuando estoy revisando un ensayo para la revista escolar, me detengo a analizar lo que he cambiado para asegurar que quede perfecto antes de enviarlo. ¡Eso es exactamente lo que hace `git diff`! Es como un espejo que muestra cada ajuste que has hecho, línea por línea. Ideal para perfeccionistas como yo. 
    """)

    # Ejemplo real de Diff
    st.markdown("""
    Imagina que estás editando tu proyecto de ciencias y quieres ver todos los cambios que has hecho antes de confirmar tus avances:
    """)

    st.code("git diff", language="bash")

    # Explicación del ejemplo Diff
    st.markdown("""
    Con `git diff`, puedes analizar cada modificación realizada. Es como darle una última revisión a tu ensayo antes de entregarlo a la profesora.

    📌 **Tip:** Usa siempre `git diff` antes de hacer un commit, así te aseguras de que todo está perfecto, como yo lo hago con mis experimentos escolares. 
    """)

    # Explicación de Reflog
    st.markdown("#### Comando de Reflog")
    st.markdown("""
    Ahora, imagina que necesitas consultar todas las decisiones que tomaste en tu proyecto. Aquí es donde entra `git reflog`: ¡es como un diario personal donde anotas todo lo que hiciste, incluso esos pasos que parecían irrelevantes pero resultaron importantes!
    """)

    # Ejemplo real de Reflog
    st.markdown("""
    ¿Alguna vez te has preguntado qué experimentos intentaste la semana pasada? Con `git reflog`, puedes consultar tu historial completo de acciones:
    """)

    st.code("git reflog", language="bash")

    # Explicación del ejemplo Reflog
    st.markdown("""
    `git reflog` guarda el registro completo de tus movimientos, incluso si hiciste un reset o te perdiste en la historia. Es como una máquina del tiempo donde todo queda anotado, lista para ser consultada.

    📌 **Tip:** Si alguna vez te pierdes en tu trabajo, `git reflog` es tu mejor aliado para regresar a ese punto brillante de inspiración. 
    """)

    # Imagen de Lisa levantando un trofeo
    st.image("images/lisa/ver_cambios.jpeg", caption="Revisar cambios es como leer un buen libro: ¡no te saltes ni una línea!", width=300)


    # Sección de Tag
    st.markdown("### 🏷️ Tag")

    # Introducción al concepto de Tag
    st.markdown("""
    En cada proyecto, siempre hay hitos que merecen ser celebrados, como cuando gané el concurso de ciencias en la escuela. `git tag` es perfecto para marcar esos momentos especiales y recordarlos para siempre. 🏅
    """)

    # Comando de Tag
    st.markdown("#### Comando de Tag")
    st.code("git tag <nombre-del-tag>", language="bash")

    # Ejemplo real del uso de Tag
    st.markdown("""
    **Ejemplo Real:**
    Imagina que acabas de completar una versión importante de tu proyecto y quieres etiquetarla como `v1.0`:
    """)
    st.code("git tag v1.0", language="bash")

    # Explicación del ejemplo de Tag
    st.markdown("""
    **Explicación del Ejemplo:**
    Usar `git tag v1.0` es como colocar una medalla en tu trabajo, recordando un momento de triunfo y logros alcanzados en el proyecto.

    📌 **Tip:** Usa etiquetas para señalar esas versiones clave que merecen ser recordadas. ¡Así siempre tendrás presente cada logro en tu camino! 🏆
    """)

    # Imagen de Lisa levantando un trofeo
    st.image("images/lisa/triunfo.jpeg", caption="Cada triunfo es un pequeño paso hacia un gran avance.", width=300)


    # Título y breve introducción de Lisa
    st.markdown("### 🎓 Resumen de Comandos Avanzados")

    # Introducción de Lisa
    st.markdown("""
    Este es nuestro resumen de los comandos avanzados que hemos aprendido en esta aventura. Aquí tienes una guía rápida para recordar cada herramienta, como tener todas las fórmulas antes de un examen. ¡Vamos a repasarlas para que nunca te pierdas en el mundo de Git!
    """)

    # Datos para el DataFrame con descripciones al estilo de Lisa
    data = {
        "Comando": [
            "`git rebase <rama-base>`",
            "`git stash`",
            "`git stash apply`",
            "`git stash pop`",
            "`git cherry-pick <id-del-commit>`",
            "`git reset --hard <commit-id>`",
            "`git reset --soft HEAD~1`",
            "`git diff`",
            "`git reflog`",
            "`git tag <nombre-del-tag>`"
        ],
        "Descripción": [
            "Mantiene tu grupo de estudio al día con los últimos cambios.",
            "Guarda tus ideas en pausa mientras resuelves otros problemas.",
            "Recupera tus ideas guardadas y sigue desde donde lo dejaste.",
            "Recupera tus ideas guardadas y elimínalas del stash, ¡como sacar tus notas justo a tiempo para usarlas!",
            "Elige solo lo mejor de tus experimentos y aplica el cambio.",
            "Viaja en el tiempo a un estado anterior, perfecto para empezar de nuevo.",
            "Deshaz un paso, pero guarda tus ideas para retomarlas después.",
            "Revisa lo que ha cambiado en tu trabajo, como repasar las anotaciones antes de entregarlo.",
            "Mira atrás y revisa todos tus pasos en el proyecto.",
            "Marca tus logros como versiones especiales, como una medalla para celebrar un hito."
        ]
    }

    # Crear el DataFrame
    df = pd.DataFrame(data)

    # Mostrar el DataFrame en Streamlit
    st.dataframe(df)

        # Imagen de Bart revisando código con sus amigos
    st.image("images/lisa/profe.jpeg", caption="El código es como una buena canción, ¡debe tener ritmo y siempre ser comprensible!.", width=300)


    # Conclusión de la lección de Lisa y transición hacia la lección con Ned
    st.markdown("### Ciencia y Código: Una Conclusión con el Estilo de Lisa")

    st.markdown("""
    ¡Genial! Hemos recorrido juntos los comandos avanzados de Git, como auténticos exploradores del conocimiento. Ahora tienes las herramientas esenciales para mantener el control de tus proyectos, navegar entre cambios, elegir tus mejores ideas, y marcar esos hitos clave como si fueran trofeos de ciencia. 🏅

    Ahora bien, hemos hablado mucho sobre cómo organizar tu trabajo en Git, ¡pero el siguiente paso es compartirlo con el mundo! 🌎 Aquí es donde entra **GitHub**: un lugar donde podrás llevar tu código en línea, colaborar con otros, y aprender aún más. 

    Pero, ¿quién mejor para guiarnos en esta misión que nuestro vecino favorito? Te dejo en las excelentes manos de **Ned Flanders**, quien te ayudará a integrar Git y GitHub y a compartir tu progreso. Ned te enseñará a subir repositorios, hacer pull requests, y aprovechar la comunidad de desarrolladores al máximo.

    ¡Nos vemos en el siguiente desafío! Hasta pronto, y recuerda que el aprendizaje es aún mejor cuando lo compartimos. 👋
    """)


def integracion_github():
    st.markdown("<h1 style='text-align: center;'>😇De Vecinito a Vecinito: Conectando con GitHub🙏</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("""
    ¡Hola holita, programadillo! 👋  
                
    Hoy traigo un sermoncito  sobre los comandos de integración en GitHub. Cada línea de código es como un versículo de la buena escritura: debe ser claro, preciso y, sobre todo, compartido con amor. 

    Con estos comandos, harás que tu repositorio local y remoto sean amiguitos, como cuando compartes una tarta de manzana con tus vecinos.  

    ### Contenidito para nuestro caminito:
    1. 🌐 **Conectar el Repositorio Local a GitHub, vecinito**
    2. 🚀 **Solicitar una Pull Request con cariño y educadito**
    3. 🔍 **Consejitos útiles para trabajar en equipo con mucho amorcito**

    ### 1. 🌐 Conectar Repositorio Local a GitHub
    Empezamos por lo más sencillito, como cuando saludas a tu vecinito por la mañanita. Lo primero que necesitamos es conectar nuestro repositorio local a GitHub, el lugarcito donde guardaremos todo nuestro trabajito para que lo vean los demás y todos nos sintamos contentitos.

    #### Crear un Nuevito Repositorio en GitHub:
    1. Primero, ve a [GitHub](https://github.com) e inicia sesión, vecinito.
    2. Luego, dale un clic en **"Nuevo repositorio"**, como cuando invitas a tu vecinito a tomar un cafecito.
    3. Rellena los campitos necesarios y haz clic en **"Crear repositorio"**. ¡Qué alegría tan grandecita!

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
    st.image("images/ned/conectar_gitHub.jpeg", width=300, caption="Conectar Git con GitHub es como abrirle la puertita a los vecinitos para que todos disfruten del trabajito.")

    st.markdown("###   2. 🚀  Pull Requests (o como pedir ayudita a los vecinitos)")
    st.markdown("""
    Las pull requests son como esas veces que necesitas que tu vecinito te eche una manita antes de tomar una decisión importantita. ¡Qué bonito es colaborar entre buenos vecinitos!

    #### Crear una Pull Request con todo tu cariñito:
    1. Crea una nueva ramita y haz commits con mucho amorcito:
    ```bash
    git checkout -b <nombre-de-la-ramita>
    # realiza los cambiecitos y commits con fe
    git push origin <nombre-de-la-ramita>
    ```
    2. Luego, en GitHub, ve a tu repositorio y haz clic en **"Pull request"**. Es como cuando invitas a tus vecinitos a charlar sobre cómo mejorar las cosas.
    3. Rellena los detallitos, como cuando preparas algo rico para compartir, y haz clic en **"Create pull request"**. ¡Es tan bonito como una tarde de juegos en el parquecito!

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
    st.image("images/ned/pull_request.jpeg", width=300, caption="Ay, hacer un pull request es como pedir un favorcito: siempre con mucho respeto y amabilidad.")

    st.markdown("### 3. 🔍 Consejitos útiles para vecinitos")
    st.markdown("""
    Aquí tienes algunos consejitos prácticos para que todo esté siempre en orden, vecinito, ¡porque un buen vecino siempre es precavido y organizado!

    #### Comprobar el estado de tu repositorio (como revisar tus tareas diarias, vecinito)
    ```bash
    git status
    ```

    **Ejemplo clarito y bendito:** Para que la salida esté más ordenadita.
    ```bash
    git status -s
    ```

    **Explicación (para que todo esté ordenadito, vecinito):**
    - `git status`: Este comando te muestra el estado de tu repositorio. ¡Es como echarle un vistacito a las tareas del día para asegurarse de que todo está en su sitio!
    - `git status`: Este comando te muestra el estado de tu repositorio de forma más odenadita y clarita.
                
    #### Mantener tu repositorio sincronizado (como mantener la paz en el vecindario, vecinito)
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
    git push origin :adios_ramita
    git push origin hola_nueva_ramita
    ```

    **Explicación (sencillita y efectiva, vecinito):**
    - `git push origin :<nombre-antiguo>`: Aquí eliminas una rama remota con el nombre antiguo, como cuando decides hacer espacio para algo nuevito.
    - `git push origin <nombre-nuevo>`: Subes una nueva rama con un nombrecito fresquito, asegurando que todo esté claro y bien organizadito.

    📌 **Tip celestial:** Mantén siempre tus ramitas ordenadas, vecinito, ¡así todo será más fácil y bendecidito para ti y los demás!

    """)
    st.image("images/ned/amigos.jpeg", width=300, caption="¡Nada más bonito que trabajar en equipo, vecinito! Juntos en el código y en el corazón.")


    # Resumen de Comandos (como un sermoncito dominical)
    st.markdown("### Resumen de Comandos de Integración en GitHub, vecinito")

    # Introducción al estilo Ned Flanders
    st.markdown("""
    ¡Hola holita, programadillo! 👋
    
    Terminamos el sermón y por ello te dejo con el resumen para que tu caminito de integración esté siempre derechito y bien guiado. ¡Amén, vecinillo!
    """)


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

    st.image("images/ned/jesucristo.jpeg", width=300, caption="Oh, querido Jesucristo, siempre nos muestras el caminito correcto. ¡Paciencia y humildad en cada línea de código!")

    # Resumen de Comandos (como un sermoncito dominical)
    st.markdown("### Resumen de Comandos de Integración en GitHub, vecinillo")

    # Introducción al estilo Ned Flanders
    st.markdown("""
    ¡Hola holita,  vecinito! 👋  
                
    ¿Listo para enderezar tu caminito en el universo del GitHub? Aquí te traigo un resumen más claro que el sermón del domingo, para que integres tu repositorio como buen cristianillo.

    Cada comando es como una obrita de caridad: bien hecho, beneficia a todo el equipo. ¡Así que prepárate para empujar (o hacer `push`) tu código al cielo del remoto!  
    """)

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
            "Conectas el repositorio local con el remoto, como hacer nuevos amiguitos.",
            "Renombras tu rama principal a 'main', para tener todo bien ordenadito, ¡nada de caos, vecinillo!",
            "Subes tu rama principal al repositorio remoto con amorcito y dedicación.",
            "Subes tu ramita específica al remoto, para que todos puedan verla y disfrutarla.",
            "Revisas el estado de tu repositorio, como quien revisa que la casita esté impecable.",
            "Traes actualizaciones del remoto, porque estar al día es importante, ¡dilly-dally no más!",
            "Sincronizas tu rama local con los cambios más recientes, ¡manteniendo la paz y la armonía!",
            "Eliminas una rama remota antigua, dejando espacio para nuevas oportunidades.",
            "Creas una nueva rama remota con un nombre fresco, ¡como un nuevo comienzo en primavera!"
        ]
    }

    # Mostrar la tabla con los comandos y sus descripciones
    df = pd.DataFrame(data)
    st.table(df)

    # Imagen final con una bendición de Flanders
    st.image("images/ned/jesucristo.jpeg", width=300, caption="Oh, querido Jesucristo, ¡guíanos en este caminito del código! Paciencia y humildad en cada línea, vecinillo.")


    st.markdown("### ⛪Conclusión Bendecidita de Ned Flanders")

    st.markdown("""
    ¡Pues vaya, vecinitos! Hemos llegado al final de este maravilloso paseo por el vecindario de GitHub. Ahora, con mucho amorcito y alegría, sabes cómo conectar tu repositorio local, hacer pull requests, y mantener todo bien organizadito, ¡como si fuera un jardín florido!

    Trabajar en equipo y compartir nuestros avances es tan bonito como un día soleado, y GitHub es el lugar perfecto para que nuestro código esté siempre accesible y a la vista de todos nuestros vecinitos. ¡Qué alegría tan grandecita es poder colaborar y mejorar juntos!

    Te dejo en las manitas de nuestro querido Nelson, quien, con un poquito más de energía, te ayudará a revisar todo lo que hemos aprendido. ¡Así reforzaremos conocimientos y terminaremos esta lección como buenos vecinitos que somos!

    ¡Nos vemos en el vecindario, y recuerda, compartir es bendecir! 🙏
    """)


def resumen_taller():
    # Título principal
    st.markdown("<h1 style='text-align: center;'>💥¿Recuerdas el Taller de Git? Con Nelson si lo harás,  ja, ja😂</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Introducción al estilo de Nelson
    st.write("¡Bienvenido al resumen rápido de Git al estilo de Nelson!")
    st.write("Vas a repasar todo lo aprendido sobre Git sin hacer el ridículo.¡Prepárate para pulir tus habilidades o te espera un buen **Ja, ja!**")
    st.write("Así que ponte cómodo, coge papel y boli y prepárate para dominar Git. ¡Vamos allá!")

    # Comandos Básicos
    st.header("⚙️ Comandos Básicos: Como cuando le robas el almuerzo a Milhouse")
    st.write("Empieza con lo básico, porque si no sabes esto, mejor ni te acerques a Git.")

    st.write("""
    - **`ls`**: Lista los archivos y directorios. Para saber dónde estás metido.
    - **`pwd`**: Muestra el directorio actual. Así evitas perderte, como el tonto de Milhouse.
    - **`cd <nombre_del_directorio>`**: Cambia de directorio. Imagínate que es como entrar a una nueva zona de la escuela.
    - **`mkdir <nombre_del_directorio>`**: Crea un directorio nuevo. No te pongas sentimental, son solo carpetas.
    - **`rm -r <nombre_del_directorio>`**: Borra un directorio con todos sus archivos. Como borrar los recuerdos de Ralph.
    - **`rm -rf <nombre_del_directorio>`**: Elimina sin preguntar. Esto es solo para valientes… ¡o locos!
    - **`touch <nombre_del_archivo>`**: Crea un archivo vacío. Algo que ni necesita usar Milhouse.
    - **`New-Item -Path . -Name "broma_homer.txt" -ItemType "File"`**: En Windows, crea un archivo. ¡Para dejarle notitas a Homero!
    - **`cp <origen> <destino>`**: Copia archivos. ¿Tramposo? Sí, pero se vale.
    - **`mv <origen> <destino>`**: Mueve o renombra archivos. Cambia las cosas de sitio como cuando Bart quiere esconder pruebas.
    - **`cat <archivo>`**: Muestra el contenido de un archivo. No te pongas a leer mi diario, ja, ja!
    """)

    st.write("Si llegaste hasta aquí y no te confundiste con los comandos básicos de Ralph... ¡entonces ya es un logro! Que no se te olvide el **`rm -rf *`**... ¡no queremos que borres todo el sistema como Ralph!")

    st.image("images/nelson/construir_casa.jpeg", width=300, caption="Construyendo la casa... de los pipelines, ¡que no se cae con el viento!")



    # Configuración e Inicialización de Git
    st.header("🔧 Configuración e Inicialización de Git: Para que sepan quién eres (y te vigilen)")
    st.write("Configura tu identidad en Git. Si no lo haces bien, podrías acabar siendo **Usuario Desconocido**. ¡Ja, ja!")

    st.write("""
    - **`git config --global user.name "Tu Nombre"`**: Configura tu nombre. Si la riegas, te van a recordar.
    - **`git config --global user.email "tuemail@example.com"`**: Configura tu correo. Sin esto, te vas a ver como un bot.
    - **`git config --list`**: Muestra la configuración actual. Es como un espejo: no miente.
    - **`git config user.name "Nombre Local"`**: Cambia el nombre solo para este proyecto. Pa' que nadie sospeche.
    """)

    st.image("images/nelson/firma.jpeg", width=300, caption="Firmando el commit, porque estilo siempre hay que poner.")


    # Operaciones Básicas
    st.header("📂 Operaciones Básicas de Git: Para que no te quedes como Ralph cuando algo sale mal")
    st.write("Aquí tienes lo esencial para guardar, enviar y gestionar cambios en Git. ¡Hazlo bien o prepárate para el **Ja, ja!**")

    st.write("""
    - **`git clone <URL-del-repositorio>`**: Clona un repositorio de GitHub. Como copiarle la tarea al listo.
    - **`git add <archivo>`**: Añade archivos al índice. ¡Todo bajo control!
    - **`git rm <archivo>`**: Elimina un archivo del repositorio. Sin dejar rastro.
    - **`git reset HEAD Receta_Rosquilla.txt`**: Revierte un archivo al último commit. No más recetas de Homero.
    - **`git commit -m "Mensaje del commit"`**: Guarda cambios con un mensaje. Sé claro, como un buen maestro.
    - **`git log`**: Muestra el historial de commits. Toda la historia sucia.
    - **`git log --oneline`**: Muestra el historial en una línea. Sencillo y directo.
    - **`git pull`**: Trae los últimos cambios del repositorio remoto. Que no te tomen por sorpresa.
    - **`git push`**: Sube tus cambios al repositorio remoto. Presume lo que hiciste.
    - **`git status`**: Muestra el estado de los archivos. Como tu bitácora.
    - **`git status -s`**: Muestra el estado en formato corto. Con esto ni Bart se perdería.
    - **`git config --global alias.<alias> '<comando>'`**: Crea un alias para un comando. ¡Más rápido!
    """)


    st.write("Después tenemos a Homer, quien te enseñó las operaciones básicas… espero que hayas seguido las instrucciones y no hayas hecho un `git add cerveza.jpg` por accidente. ¡Ja, ja! No te preocupes, Homer también lo hace a veces.")

    st.image("images/nelson/elimina_archivo.jpeg", width=300, caption="Eliminando archivos… y rezando para que no sea el importante.")


    # Ramas y Colaboración
    st.header("🌱 Ramas y Colaboración: No dejes que te saquen de tu propia historia")
    st.write("Con estas instrucciones, podrás trabajar en paralelo sin hacer un lío (o algo peor).")

    st.write("""
    - **`git branch aventura-skate`**: Crea una nueva rama. Como empezar una nueva historia.
    - **`git checkout aventura-skate`**: Cambia a la rama 'aventura-skate'. Listo para explorar.
    - **`git checkout -b aventura-nueva`**: Crea y cambia a una nueva rama. No más excusas para no innovar.
    - **`git branch`**: Lista las ramas. Para que sepas de dónde vienes.
    - **`git branch -d aventura_olvidada`**: Elimina una rama. Como un recuerdo amargo.
    - **`git checkout main`**: Vuelve a la rama principal. Porque no hay lugar como casa.
    - **`git merge aventura-skate`**: Une cambios de otra rama en la actual. ¡Todo en un solo lugar!
    """)

    st.write("Luego vino Bart con las ramas y colaboración. ¡Claro, porque quién más para enseñarnos a meternos en problemas y luego intentar `mergearlos`! Solo recuerda: si la lías con un `merge`, ¡culpa a Milhouse! O... haz un `rebase`, que nadie se entere.")
    st.image("images/nelson/cambia_estilo.png", width=300, caption="Cambiando el estilo como si fuera un día casual.")



    # Uso Avanzado de Git
    st.header("🔥 Uso Avanzado de Git: Aquí es donde separas a los fuertes de los débiles")
    st.write("Si has llegado hasta aquí, ya deberías saber lo básico. ¡Hora de jugar en las grandes ligas!")

    st.write("""
    - **`git rebase <rama-base>`**: Reorganiza commits de una rama sobre otra. Un baile de cambios.
    - **`git checkout feature`** / **`git rebase main`**: Aplica los commits de 'main' en 'feature'. Para no quedar desactualizado.
    - **`git stash`**: Guarda cambios sin hacer commit. Un truco bajo la manga.
    - **`git checkout main`** / **`git stash apply`**: Aplica el último stash. Como sacarlo del cajón.
    - **`git stash pop`**: Aplica y elimina el último stash. Un movimiento rápido.
    - **`git cherry-pick <id-del-commit>`**: Toma un commit específico y aplícalo en la rama actual. Para lo mejor de lo mejor.
    - **`git reset --hard <commit-id>`**: Revierte todos los cambios hasta el commit especificado. Para empezar de cero.
    - **`git reset --soft HEAD~1`**: Revierte el último commit. Si te arrepentiste, no pasa nada.
    - **`git diff`**: Muestra diferencias entre cambios no confirmados. Para detectar al culpable.
    - **`git reflog`**: Muestra el historial de operaciones recientes. Como la caja negra de un avión.
    - **`git tag <nombre-del-tag>`**: Crea un marcador en el historial. Como una firma de Nelson.
    """)
    st.write("Y ahí va Lisa, con el uso avanzado de Git, que seguro te dejó pensando. Con tanto `rebase` y `cherry-pick`, casi parece que ella está buscando la verdad del universo y no solo los commits. ¡Ja, ja! Espero que hayas sobrevivido a su parte sin quedarte con dolor de cabeza.")
    st.image("images/nelson/pasado_maquina_tiempo.jpeg", width=300, caption="Viajando al pasado en la máquina del tiempo para corregir un ‘push’ equivocado.")


    # Integración de GitHub
    st.header("🌐 Integración de GitHub: Lleva tu grandeza al mundo digital")
    st.write("Si quieres presumir tus cambios, GitHub es el lugar. No subas cualquier cosa… ¡Nelson te vigila!")

    st.write("""
    - **`git remote add origin <URL-del-repositorio>`**: Conecta el repositorio local con GitHub. ¡Como un grito en el vacío!
    - **`git branch -M main`**: Renombra la rama principal a 'main'. Porque los tiempos cambian.
    - **`git push -u origin main`**: Sube la rama principal a GitHub. Hora de compartir.
    - **`git checkout -b <nombre-de-la-ramita>`**: Crea y cambia a una nueva rama para trabajo en GitHub. ¡Aventúrate!
    - **`git push origin <nombre-de-la-ramita>`**: Sube una rama específica a GitHub. Pa' que todos vean.
    - **`git push origin :<nombre-antiguo>`** / **`git push origin <nombre-nuevo>`**: Cambia el nombre de una rama en GitHub. ¡Actualízate o queda en el pasado!
    """)
    st.write("Por último, Ned Flanders, tan amiguito como siempre, te enseñó la integración con GitHub. Si alguien tiene todo bajo control en **La Nube**, ese es Ned. Solo recuerda, cuando empujes tus cambios (`push`), hazlo con una sonrisa y un **hola vecinito!** como él.")
    st.image("images/nelson/vigilando.jpeg", width=300, caption="¡Vigilando el código como un halcón en busca de bugs!")

    # Encabezado de Documentación y Recursos
    st.header("¡Documentación y Recursos Adicionales!")

    # Introducción al estilo Nelson
    st.markdown("""
    ¡Ey, novato del código! Si creías que podías andar por Git sin leer nada, ¡adivina qué! **Ja, ja**, aquí tienes unos recursos para que no la fastidies en tus commits.

    ¡Toma nota y deja de ser un desorganizado! Estos enlaces son lo único que te separa del caos.
    """)

    # Recursos adicionales
    st.markdown("""
    - **[Libro Pro Git Gratuito](https://git-scm.com/book/en/v2)**: Para los cerebritos que quieren aprenderlo TODO sobre Git (y gratis, porque no somos millonarios).

    - **[Cheat Sheet Git](https://training.github.com/downloads/es_ES/github-git-cheat-sheet/)**: El resumen de comandos perfecto por si la memoria no es lo tuyo.

    - **[Git Official Documentation](https://git-scm.com/doc)**: Documentación oficial con videos cortos para que aprendas lo básico sin quedarte dormido.

    - **[Juego Interactivo de Git](https://learngitbranching.js.org/?locale=es_ES)**: Aprende jugando y demuestra que eres más listo que Ralph. ¡Es interactivo, así que no te aburras!
    """)

    # Imagen graciosa de Nelson
    st.image("images/nelson/leer_libro_git.jpeg", width=300, caption="¡Ja, ja! Leyendo el manual porque los commits no se arreglan solos.")

    # Conclusión 
    st.header("🎉 ¡Y con eso hemos terminado, ja, ja! 🎉")
    st.write("Si llegaste hasta aquí y no te perdiste en el camino, ya eres casi tan bueno en Git como yo en hacerle bromas a Milhouse. Ahora, cuando alguien más esté peleando con Git, podrás aparecer y decir: ‘¿En serio no sabes eso? ¡Ja, ja!’")
    st.write("Git ya no será un misterio, sino tu carta secreta para verte como un genio. Y no olvides, ¡cuando surjan dudas, responde como un campeón en la siguiente sección de repaso! ¡Vamos a ver si has aprendido algo o solo estabas de turista!")
    st.write("Si has practicado cada comando y no has terminado hecho un lío, ¡entonces Git ya no será un misterio, sino tu herramienta secreta! ¡Cuando alguien necesite ayuda con Git, podrás decirles 'Ja, ja!' como yo, tu buen amigo Nelson!")
    st.write("¡Ahora, vamos con las preguntas de repaso, y a ver si no haces como Bart y te lo copias todo, ja, ja!")


    st.markdown("**Recuerda**: el que **ja-ja**  último, **ja-ja** mejor…" )

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
        "q8": ["git diff donut314 duff17", "git log donut314 duff17", "git status donut314 duff17", "git show donut314 duff17"],
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
    
    st.markdown("<h1 style='text-align: center;'>Ejercicios de Git con Apu Nahasapeemapetilon</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("¡Bienvenidos al *Badulaque*! Como diría Apu: **Gracias, vuelva pronto... a hacer más commits!**")

    # Ejercicio 1
    st.header("Ejercicio 1: Clonar un Repositorio")
    st.markdown("""
    Bienvenido, señor GitHub. ¿Cómo le puedo ayudar hoy?
    
    Imagina que Apu ha recibido una URL de un repositorio y necesita clonar ese repositorio para actualizar el stock de su tienda. ¿Qué comando debería usar?
    """)
    opciones1 = st.session_state.opciones["q1"]
    respuesta1 = st.radio("Selecciona la respuesta correcta:", opciones1, key="q1_respuesta")
    if st.button("Verificar Respuesta 1", key="q1_btn"):
        verificar_respuesta(respuesta1, "q1")
    st.image("images/apu/apu_clonar.jpeg", width=200)

    # Ejercicio 2
    st.header("Ejercicio 2: Añadir Archivos al Área de Staging")
    st.markdown("""
    ¡Este código es mejor que un fresisuis recién servido! 
    Apu ha hecho cambios en `index.html` para mejorar las ofertas del Badulaque y quiere prepararlo para el próximo commit. ¿Qué comando debe usar?
    """)
    opciones1 = st.session_state.opciones["q2"]
    respuesta2 = st.radio("Selecciona la respuesta correcta:", opciones1, key="q2_respuesta")
    if st.button("Verificar Respuesta 2", key="q2_btn"):
        verificar_respuesta(respuesta2, "q2")
    st.image("images/apu/apu_cambios.jpeg", width=200)

    # Ejercicio 3
    st.header("Ejercicio 3: Hacer un Commit con un Mensaje")
    st.markdown("""
    Oh no, ¡he cometido un error en los precios de las rosquillas de Homer! Hora de hacer un commit con un mensaje apropiado: `Añadida nueva función`. ¿Cuál es el comando correcto?
    """)
    opciones3 = st.session_state.opciones["q3"]
    respuesta3 = st.radio("Selecciona la respuesta correcta:", opciones3, key="q3_respuesta")
    if st.button("Verificar Respuesta 3", key="q3_btn"):
        verificar_respuesta(respuesta3, "q3")
    st.image("images/apu/precios.jpeg", width=200)

    # Ejercicio 4
    st.header("Ejercicio 4: Ver el Historial de Commits")
    st.markdown("""
    Señor Git, déjeme revisar mis viejos errores y... ¡oh, aquí está el commit donde cambié los precios de los productos de Homer! ¿Qué comando uso para ver el historial de mis transacciones?
    """)
    opciones4 = st.session_state.opciones["q4"]
    respuesta4 = st.radio("Selecciona la respuesta correcta:", opciones4, key="q4_respuesta")
    if st.button("Verificar Respuesta 4", key="q4_btn"):
        verificar_respuesta(respuesta4, "q4")
    st.image("images/apu/donuts_apu.jpeg", width=200)

    # Ejercicio 5
    st.header("Ejercicio 5: Guardar Cambios Temporalmente")
    st.markdown("""
    Apu ha recibido una llamada urgente de Homer sobre una oferta de fresisuis, pero primero necesita guardar sus cambios en el stock de Badulaque sin hacer un commit. ¿Qué comando usaría?
    """)
    opciones5 = st.session_state.opciones["q5"]
    respuesta5 = st.radio("Selecciona la respuesta correcta:", opciones5, key="q5_respuesta")
    if st.button("Verificar Respuesta 5", key="q5_btn"):
        verificar_respuesta(respuesta5, "q5")
    st.image("images/apu/llamada.jpeg", width=200)

    # Ejercicio 6
    st.header("Ejercicio 6: Fusionar Cambios de una Rama")
    st.markdown("""
    Apu ha terminado de trabajar en la rama `feature-x` donde añadió un nuevo tipo de fresisuis. Ahora quiere fusionar estos cambios con la rama `main`. ¿Qué comando debería usar?
    """)
    opciones6 = st.session_state.opciones["q6"]
    respuesta6 = st.radio("Selecciona la respuesta correcta:", opciones6, key="q6_respuesta")
    if st.button("Verificar Respuesta 6", key="q6_btn"):
        verificar_respuesta(respuesta6, "q6")
    st.image("images/apu/cambios_rama.jpeg", width=200)

    # Ejercicio 7
    st.header("Ejercicio 7: Eliminar un Archivo del Repositorio")
    st.markdown("""
    Ese archivo `deprecated_feature.py` es como los precios antiguos del Badulaque: ¡ya no sirve! ¿Qué comando debería usar Apu para eliminar este archivo del repositorio?
    """)
    opciones7 = st.session_state.opciones["q7"]
    respuesta7 = st.radio("Selecciona la respuesta correcta:", opciones7, key="q7_respuesta")
    if st.button("Verificar Respuesta 7", key="q7_btn"):
        verificar_respuesta(respuesta7, "q7")
    st.image("images/apu/no_sirve.jpeg", width=200)

    # Ejercicio 8
    st.header("Ejercicio 8: Ver Cambios entre Commits")
    st.markdown("""
    Apu necesita comparar dos cambios importantes en los precios de sus fresisuis, entre los commits `donut314` y `duff17`. ¿Qué comando usaría?
    """)
    opciones8 = st.session_state.opciones["q8"]
    respuesta8 = st.radio("Selecciona la respuesta correcta:", opciones8, key="q8_respuesta")
    if st.button("Verificar Respuesta 8", key="q8_btn"):
        verificar_respuesta(respuesta8, "q8")
    st.image("images/apu/precios_lucha.jpeg", width=200)

    # Ejercicio 9
    st.header("Ejercicio 9: Subir una nueva Rama al Repositorio Remoto")
    st.markdown("""
    Apu ha creado una nueva rama local llamada `feature-y` con las ofertas especiales de la semana. Quiere subirla al repositorio remoto para que todos puedan verlas. ¿Qué comando usaría?
    """)
    opciones9 = st.session_state.opciones["q9"]
    respuesta9 = st.radio("Selecciona la respuesta correcta:", opciones9, key="q9_respuesta")
    if st.button("Verificar Respuesta 9", key="q9_btn"):
        verificar_respuesta(respuesta9, "q9")
    st.image("images/apu/oferta_especial.jpeg", width=200)

    # Ejercicio 10
    st.header("Ejercicio 10: Revertir el Último Commit")
    st.markdown("""
    Apu cometió un error en el último commit y decide revertirlo, pero quiere conservar los cambios en el área de staging. ¿Qué comando usaría para deshacer el último commit?
    """)
    opciones10 = st.session_state.opciones["q10"]
    respuesta10 = st.radio("Selecciona la respuesta correcta:", opciones10, key="q10_respuesta")
    if st.button("Verificar Respuesta 10", key="q10_btn"):
        verificar_respuesta(respuesta10, "q10")
    st.image("images/apu/error.jpeg", width=200)

    st.markdown("**¡Gracias, vuelva pronto y recuerde hacer siempre un `git pull` antes de trabajar!**")


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
    st.markdown("<h1 style='text-align: center;'>Tss... silencio Maggie sólo quiere escucharte 🍼</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("""
    **¡Pssst!** Maggie ha dejado caer su chupete para saber qué opinas del taller. Como no puede hablar, ella escucha atentamente lo que tienes que decir para seguir mejorando. ¡Déjanos tus impresiones y no olvides sonreír como lo harías con Maggie! 😊
    
    ### Preguntas de Feedback (Maggie promete que no habrá balbuceos... solo tus respuestas)
    """)

    # Pedimos el nombre del participante
    nombre = st.text_input("Por favor, introduce tu nombre para identificar tu feedback", key="nombre")
    st.image("images/maggie/atenta.jpeg", width=200)

    # Pregunta 1
    st.subheader("1. ¿Qué te ha parecido el contenido del taller? (¿Valió cada chupetón de Maggie?)")
    contenido = st.text_area("Tu respuesta:", key="contenido")
    st.image("images/maggie/divertida.jpeg", width=200)

    # Pregunta 2
    st.subheader("2. ¿Hubo algún tema que te resultó tan interesante que hasta Maggie dejó de chuparse el dedo?")
    tema_util = st.text_area("Tu respuesta:", key="tema_util")
    st.image("images/maggie/no_chuparse.jpeg", width=200)

    # Pregunta 3
    st.subheader("3. ¿Hay algo que podamos mejorar? Maggie sabe que siempre hay algo que mejorar... como la posición del biberón.")
    mejoras = st.text_area("Tu respuesta:", key="mejoras")
    st.image("images/maggie/posicion_biberon.jpeg", width=200)

    # Pregunta 4
    st.subheader("4. ¿Te gustaría participar en futuros talleres? Maggie quiere saber si seguirá escuchando tus ideas.")
    futuros_talleres = st.radio("Selecciona una opción:", ["Sí", "No"], key="futuros_talleres")
    st.image("images/maggie/ideas.jpeg", width=200)

    # Espacio para otros comentarios
    st.subheader("Otros comentarios (Maggie es toda oídos, aunque no lo parezca...)")
    otros_comentarios = st.text_area("Tu respuesta:", key="otros_comentarios")
    st.image("images/maggie/oidos.jpeg", width=200)


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

    st.markdown("---")

    # Mensaje final del taller
    st.markdown("<h2 style='text-align: center;'>🎉 ¡Felicidades por completar el taller de Git! 🎉</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Espero que te haya sido útil y que te lleves una sonrisa junto con el conocimiento. ¡Recuerda que siempre hay espacio para mejorar!</p>", unsafe_allow_html=True)

    # Agradecimiento y firma
    st.markdown(
        """
        <p style='text-align: center; font-size: 20px;'>
            Realizado con 💻 y con mucha dedicación por 
            <span style='color: #8D99AE; font-weight: bold;'>Alex Marzá</span>
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("<p style='text-align: center;'>Si quieres conectar, tienes alguna duda o quiere ayudar a mejorar el taller, no dudes en visitar mi perfil en LinkedIn:</p>", unsafe_allow_html=True)

    # Enlace a LinkedIn
    st.markdown(
        """
        <div style='text-align: center;'>
            <a href='https://www.linkedin.com/in/alex-marza-data-science/' target='_blank' style='font-size: 20px; color: #0073b1; text-decoration: none;'>
                👤 Alex Marzá Manuel
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Mensaje de despedida
    st.markdown("<p style='text-align: center;'>¡Gracias por participar y por el feedback proporcionado! 👋</p>", unsafe_allow_html=True)

# Diccionario para la navegación
paginas = {
    "Home": pagina_principal,
    "Comandos Básicos con Ralph": comandos_basicos_terminal,
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
