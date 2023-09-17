import streamlit as st
import cv2
import numpy as np

# Configuración de la página
st.title("Aplicación de Desenfoque de Imágenes")
st.sidebar.header("Ajustes")

# Cargar una imagen desde el usuario
uploaded_image = st.sidebar.file_uploader("Cargar una imagen", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Leer la imagen original
    original_image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
    
    # Mostrar la imagen original
    st.image(original_image, caption="Imagen Original", use_column_width=True)
    
    # Aplicar el desenfoque
    blur_radius = st.sidebar.slider("Radio de Desenfoque", 1, 20, 5)
    blurred_image = cv2.GaussianBlur(original_image, (blur_radius, blur_radius), 0)
    
    # Mostrar la imagen desenfocada
    st.image(blurred_image, caption="Imagen Desenfocada", use_column_width=True)
else:
    st.sidebar.text("Sube una imagen para empezar.")
