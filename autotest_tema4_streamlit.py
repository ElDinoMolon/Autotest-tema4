
import streamlit as st
import pandas as pd

# Cargar las preguntas del tema 4
data = {
    "Pregunta": [
        "¿Cuál es el objetivo principal de la compresión de audio digital?",
        "¿Qué es el umbral de cuantificación en compresión de audio?",
        "¿Qué técnica es utilizada para reducir la redundancia temporal en una señal de audio?",
        "¿Qué caracteriza a la codificación de audio perceptual?",
        "¿Cómo afecta el algoritmo de Huffman en la compresión de audio?"
    ],
    "Opciones": [
        ["Aumentar el ancho de banda necesario para la transmisión.",
         "Reducir el tamaño de los datos eliminando redundancia.",
         "Eliminar información esencial de la señal.",
         "Duplicar la señal para mejorar la calidad."],
        ["El nivel máximo de amplitud antes de la distorsión.",
         "El nivel mínimo de energía que se puede representar.",
         "La diferencia entre el nivel de entrada y salida.",
         "El nivel de ruido aceptable en la señal."],
        ["Transformada de Fourier rápida (FFT).",
         "Codificación predictiva lineal (LPC).",
         "Atenuación de la señal no utilizada.",
         "Filtrado adaptativo de datos."],
        ["El uso de transformadas temporales para la compresión.",
         "Aprovecha las limitaciones del oído humano.",
         "Introduce redundancia en los datos para asegurar calidad.",
         "Se basa en la teoría de muestreo uniforme."],
        ["Reduce la calidad del audio eliminando componentes importantes.",
         "Permite codificar datos de manera eficiente usando longitudes variables.",
         "Incrementa la redundancia de los datos para evitar errores.",
         "Aumenta la complejidad de la decodificación sin beneficios reales."]
    ],
    "Respuestas Correctas": ["B", "B", "B", "B", "B"],
    "Justificaciones": [
        "La compresión de audio digital tiene como propósito principal minimizar el tamaño de los datos eliminando redundancia y preservando la calidad percibida.",
        "El umbral de cuantificación representa el nivel más bajo de energía que se puede codificar, siendo crucial para determinar la precisión de la señal cuantificada.",
        "La codificación predictiva lineal reduce la redundancia temporal prediciendo la siguiente muestra a partir de las anteriores.",
        "La codificación perceptual utiliza modelos psicoacústicos para eliminar datos que el oído humano no puede percibir, optimizando el tamaño de los datos.",
        "El algoritmo de Huffman crea códigos de longitud variable para representar datos más frecuentes con códigos más cortos, aumentando la eficiencia."
    ]
}

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Título de la aplicación
st.title("Autotest Interactivo: Tema 4 - Tratamiento Digital de Audio")

# Instrucciones
st.write("Selecciona las respuestas correctas para cada pregunta y verifica tus resultados.")

# Crear un puntaje inicial
puntaje = 0

# Iterar sobre las preguntas
for index, row in df.iterrows():
    st.subheader(f"Pregunta {index + 1}")
    st.write(row["Pregunta"])
    # Opciones
    respuesta = st.radio("Selecciona una respuesta:", row["Opciones"], key=index)
    # Comprobar respuesta
    if respuesta.startswith(row["Respuestas Correctas"]):
        st.success("¡Correcto!")
        puntaje += 1
    else:
        st.error("Incorrecto.")
        st.write(f"Justificación: {row['Justificaciones']}")

# Mostrar puntaje final
st.write(f"Tu puntaje final es: {puntaje} / {len(df)}")

