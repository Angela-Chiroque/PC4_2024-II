# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.

# Primero, debes abrir el folder donde se encuentra tu archivo de Python en la terminal de tu computadora.
# Para hacerlo, debes escribir el siguiente comando en la terminal de tu computadora
# cd ruta_de_tu_carpeta
# o desde Visual Studio Code, seleccionas Open Folder y seleccionas la carpeta 
# donde se encuentra tu archivo de Python

# Segundo, debes instalar un entorno virtual en tu computadora.
# python -m venv .venv
# Este comando crea un entorno virtual en la carpeta actual con el nombre .venv.

# Para activar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# .venv\Scripts\activate
# Para desactivar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# deactivate

# Tercero, debes instalar Streamlit en tu entorno virtual.
# pip install Streamlit 

# Cuarto, puedes abrir el tutorial de Streamlit en tu navegador.
# streamlit hello o python -m streamlit hello

# Quinto, debes abrir el archivo de Python en la terminal de tu computadora.
# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py o python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Sumaq tusuy</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("foto perfil.jpeg", caption='Aquí puedes escribir una tiqueta debajo de la imagen', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
Mi nombre es Angela Chiroque Ruiz, tengo 20 años y estudio Comunicación Audiovisual en la Facultad de Ciencias y Artes de la Comunicación en la PUCP. Desde pequeña he estado inmersa en el mundo de la danza, comenzando con danzas afroperuanas a través de los talleres de extensión de la Universidad Nacional del Folklore José María Arguedas. Actualmente soy parte del conjunto de danza del Centro de Música y Danza de la PUCP, y en el futuro me gustaría formar parte de varios conjuntos y elencos nacionales, así como especializarme en Fotografía y obtener una maestría en Antropología audiovisual. 
Lo que más me apasiona de mi carrera es la capacidad de contar historias a través de los medios audiovisuales, y cómo la comunicación tiene el poder de conectar personas y culturas. Además de mi carrera, me encanta bailar otros géneros como el Jazz teatral, cantar diversos estilos musicales, el teatro musical, hacer impro y tocar el cajón. En mi tiempo libre, disfruto mucho de estas actividades, ya que son mi forma de expresión y de conectar con mi creatividad.
"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.

# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
Al principio, me sentía completamente ajena a la programación. No sabía nada sobre el tema, solo lo escuchaba de manera general, pero la idea de generar gráficos a partir de códigos y bases de datos me parecía interesante, aunque también intimidante. Sin embargo, a medida que fui aprendiendo, descubrí lo fascinante que puede ser poder crear algo desde cero y ver cómo cobra vida con solo escribir líneas de código.

La programación me ha enseñado a ser más paciente y meticulosa. A veces es fácil frustrarse cuando el código no funciona como esperas, pero aprender a resolver problemas y encontrar soluciones me ha ayudado a mejorar mis habilidades de análisis y lógica. Lo que más me gusta de programar es la capacidad de generar herramientas y recursos útiles, como redes de búsqueda o aplicaciones, que pueden hacer más accesible la información y facilitar la investigación sobre temas interesantes.

En el futuro, me gustaría aplicar lo aprendido en programación para crear páginas web y sistemas que faciliten la investigación en diversas áreas. Me gustaría seguir explorando el potencial de la programación y contribuir con soluciones que ayuden a resolver problemas reales. Aunque a veces la programación puede ser desafiante, el sentido de logro al lograr que todo funcione es increíblemente gratificante. 
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Ahora agregamos un video a mi blog donde explico algún tema de las clases
# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>", unsafe_allow_html=True)
# <h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>: Esta es una cadena de código HTML
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Explicación de un tema de las clases 📚") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.

# Agregamos un video a la aplicación web ( menor a 20 MB)

# st.video("ppc-2024-1.mp4"): Esta línea está agregando un video a la aplicación web.


# Agregamos un enlace a la página web donde está el video.
enlace = f'<a href="https://drive.google.com/file/d/1Cm-AwULrQqt4gCUyZ9Mo_NXPm5SMG31S/view?usp=sharing" target="_blank"><button>Diferencias entre las declaraciones condicionales if-elif-else</button></a>'
st.markdown(enlace, unsafe_allow_html=True)
# f'<a href="URL" target="_blank"><button>Nombre</button></a>':
# La etiqueta <a> se utiliza para crear un enlace en HTML.
# El atributo href se utiliza para especificar la URL de destino del enlace.
# El atributo target="_blank" se utiliza para abrir el enlace en una nueva pestaña del navegador.
# La etiqueta <button> se utiliza para crear un botón en HTML.
# El texto dentro de las etiquetas <button> ("Nombre creativo para el botón") es el contenido del botón.
# La variable enlace contiene la cadena de código HTML para el enlace y el botón.


# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Gráficos creados durante el ciclo</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['Gráfico 1 - Juventus Local', 'Gráfico 2 - Juventus visitante', 'Gráfico 3 - Milan e Inter']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == 'Gráfico 1 - Juventus Local':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    sidebar.image("grafico 1 juventus local.png", caption='El gráfico es un histograma que representa la frecuencia de goles anotados por la Juventus como local en distintos partidos. Eje horizontal (Goles): Indica la cantidad de goles anotados en un partido (desde 0 hasta 8). Eje vertical (# de partidos): Muestra la cantidad de partidos en los que se anotó esa cantidad de goles. Distribución de los goles: La frecuencia más alta está en la categoría de 2 goles, lo que sugiere que este es el número más común de goles que la Juventus anota como local. Hay un patrón de distribución casi simétrica: las frecuencias disminuyen gradualmente a medida que los goles anotados son más bajos (0, 1) o más altos (4). Rendimiento ofensivo en casa:La Juventus anota con mayor regularidad entre 1 y 3 goles en casa.Es poco frecuente que marque 0 goles (aunque esto ocurre), y los partidos con más de 4 goles son excepcionales.Comparación visual:A diferencia de los goles como visitante (donde había una fuerte asimetría hacia pocos goles), el rendimiento en casa parece más balanceado, con un desempeño ligeramente mejor al anotar frecuentemente 2 o 3 goles.', width=500)
    pass
elif grafico_seleccionado == 'Gráfico 2 - Juventus visitante':
    sidebar.markdown("<div style='text-align: justify'>Texto para la opción 2.</div>", unsafe_allow_html=True)
    sidebar.image("grafico 2 juventus visitante.png", caption='El gráfico es un histograma que muestra la frecuencia de goles anotados por la Juventus como visitante en diferentes partidos. Eje horizontal (Goles): Representa la cantidad de goles anotados en un partido (desde 0 hasta 8). Eje vertical (# de partidos): Indica el número de partidos en los que la Juventus anotó una cantidad específica de goles. Distribución de los goles: La mayor parte de los partidos como visitante terminan con 1 o 2 goles anotados, ya que el grupo más alto (frecuencia máxima) está en la categoría de 2 goles. Hay pocos partidos donde la Juventus no anota goles (frecuencia más baja, aunque todavía significativa). Rendimiento extremo: Es poco común que la Juventus anote más de 3 goles como visitante, ya que las frecuencias disminuyen notablemente a partir de 3 goles. Asimetría:La distribución está sesgada a la derecha: la mayoría de los partidos tienen un número bajo de goles, mientras que los partidos con un número alto de goles (como 4 o más) son raros.', width=500)
    pass
elif grafico_seleccionado == 'Gráfico 3 - Milan e Inter':
    sidebar.markdown("<div style='text-align: justify'>Texto para la opción 3.</div>", unsafe_allow_html=True)
    sidebar.image("pie chart visitante milan inter.png", caption='El gráfico es un diagrama de pastel que muestra la distribución porcentual del promedio de goles como visitante entre dos equipos: Inter y Milan. Inter (59.6%): Representa la mayoría de los goles promedio anotados como visitante en comparación con el Milan. Es decir, el Inter tiene un desempeño superior en términos de goles anotados fuera de casa en esta comparación específica. Milan (40.4%): Aunque es menor, sigue siendo una proporción significativa, indicando que el Milan también tiene una contribución importante a los goles promedio como visitante, pero es inferior en comparación con el Inter.', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas': Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
