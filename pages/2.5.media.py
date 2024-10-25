import streamlit as st
import numpy as np

st.header("Elementos multimedia", divider=True)

'### `st.image()`'
logoUCLM = "https://www.uclm.es/-/media/MediosUCLM/IdentidadVisualCorporativa/LOGOMARCA_UCLM_2021-scaled"
st.image(logoUCLM, caption="Logo Universidad de Castilla-La Mancha", width=400)

image_array = np.random.rand(300, 300, 3)  # Imagen aleatoria
st.image(image_array, caption="Imagen aleatoria")
 

'### `st.video()`'
st.video("https://www.youtube.com/watch?v=6TkjFktg6I8", start_time=2, format="video/mp4")

'### `st.audio()`'
st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg", 
         format="audio/ogg", start_time=10)


'### `st.logo()`'
st.logo(logoUCLM, link="https://www.uclm.es/", size='large')
