import streamlit as st
import pandas as pd
import numpy as np

st.header("Botones", divider=True)

'### `st.button()`'
if st.button("Click me"):
    st.write("Button clicked!")

'### `st.download_button()`'
file_path = "figures/Streamlit-logo.png"
with open(file_path, "rb") as file:
    btn = st.download_button(
        label="Download Streamlit Logo",
        data=file,
        file_name="Streamlit-logo.png",
        mime="image/png"
    )
if btn:
    st.write("Download initiated!")

'### `st.feedback()`'
st.write("¿Cómo calificarías tu experiencia con nuestra aplicación?")
feedback = st.feedback("stars")
if feedback is not None:
    st.write(f"Gracias por tu calificación: {feedback+1} estrellas")

"---"

st.write("¿Cómo calificarías tu experiencia con nuestra aplicación?")
feedback = st.feedback("faces")
if feedback is not None:
    st.write(f"Gracias por tu calificación: {feedback+1}")

"---"

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
feedback = st.feedback("thumbs")
if feedback is not None:
    st.markdown(f"Has elegido: {sentiment_mapping[feedback]}")

'### `st.form_submit_button()`'
with st.form("my_form"):
    name = st.text_input("Name")
    submitted = st.form_submit_button("Sign up")
    if submitted:
        st.write(f"Welcome {name}!")

'### `st.link_button()`'
st.link_button("Go to Streamlit homepage", url="https://streamlit.io")

'### `st.page_link()`'
st.page_link("pages/2.1.texto.py", label="2.1. Texto", icon="📝")
st.page_link("pages/2.2.datos.py", label="2.2. Datos", icon="📊")
st.page_link("pages/2.3.graficas.py", label="2.3. Gráficas", icon="📈")
st.page_link("pages/2.4.input.py", label="2.4. Entradas", icon="📥")


st.header("Selectores", divider=True)

'### `st.checkbox()`'
selected = st.checkbox("I agree")
if selected:
    st.write("You agreed!")

'### `st.color_picker()`'
color = st.color_picker("Pick a color", "#00f900")
st.write(f"Selected color: {color}")

'### `st.multiselect()`'
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.write(f"You selected: {choices}")

'### `st.radio()`'
choice = st.radio("Pick one", ["cats", "dogs"])
st.write(f"You selected: {choice}")

'### `st.selectbox()`'
choice = st.selectbox("Pick one", ["cats", "dogs"])
st.write(f"You selected: {choice}")

'### `st.select_slider()`'
size = st.select_slider("Pick a size", ["XS", "S", "M", "L", "XL"])
st.write(f"Selected size: {size}")

startSize, endSize = st.select_slider("Pick a size", options=["XS", "S", "M", "L", "XL"], value=["S", "M"])
st.write(f"Selected size: between {startSize} and {endSize}")

'### `st.toggle()`'
activated = st.toggle("Activate")
if activated:
    st.write("Activated!")


st.header("Entradas numéricas", divider=True)

'### `st.number_input()`'
number = st.number_input("Pick a number between 0 and 100", 0, 100)
st.write(f"You picked: {number}") 

'### `st.slider()`'
number = st.slider("Pick a number between 0 and 100", 0, 100)
st.write(f"You picked: {number}")


st.header("Fecha y hora", divider=True)

'### `st.date_input()`'
date = st.date_input("Your birthday", pd.to_datetime("2000-01-01"))
st.write(f"Selected date: {date}")

'### `st.time_input()`'
time = st.time_input("Meeting time", value=None, step=60*10)
st.write(f"Selected time: {time}")


st.header("Entradas de texto", divider=True)


'### `st.text_area()`'
text = st.text_area("Text to translate")
if text:
    st.write(f"Text to translate: {text}")

'### `st.text_input()`'
name = st.text_input("First name")
st.write(f"Hello {name}!")


st.header("Media", divider=True)

'### `st.file_uploader()`'
st.write(pd.DataFrame({
    "Column A": np.random.rand(3),
    "Column B": np.random.rand(3),
    "Column C": np.random.rand(3),
}))

uploaded_file = st.file_uploader("Upload a CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)

'### `st.experimental_audio_input()`'
speech = st.experimental_audio_input("Record a voice message")
if speech:
    st.audio(speech)


'### `st.camera_input()`'
image = st.camera_input("Take a picture")
if image:
    st.image(image, caption="Captured Image", use_column_width=True)