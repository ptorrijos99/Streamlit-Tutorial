import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import time

st.header("Layouts", divider=True)

'### `st.columns()`'
left, middle, right = st.columns(3, vertical_alignment="bottom")

left.text_input("Write something")
middle.button("Click me", use_container_width=True)
right.checkbox("Check me")


'### `st.container()`'
container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")
container.write("This is inside too")


'### `st.columns()` + `st.container()`'
row1 = st.columns(3)
row2 = st.columns(3)
i = 0
for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon: " + str(i))
    i += 1


'### `st.expander()`'
left, right = st.columns(2, vertical_alignment="bottom")
num_tiradas = left.number_input("Número de tiradas", min_value=1, max_value=100000, value=10)
if right.button("Tirar dados"):
    data = [random.randint(1, 6) + random.randint(1, 6) for _ in range(num_tiradas)]
    st.write("Media de las tiradas:", sum(data) / len(data))

    with st.expander("Ver resultados"):
        st.write("Distribución de resultados de las tiradas de dos dados.")
        
        # Crear un histograma de las tiradas
        fig, ax = plt.subplots()
        ax.hist(data, bins=range(2, 14), edgecolor='black', align='left')
        ax.set_xticks(range(2, 13))
        ax.set_xlabel("Suma de los dados")
        ax.set_ylabel("Frecuencia")
        ax.set_title("Histograma de tiradas de dos dados")
        
        st.pyplot(fig)


'### `st.popover()`'
with st.popover("Configuración"):
    st.markdown("Configuración de la aplicación 👋")
    name = st.text_input("¿Cómo te llamas?")
    age = st.number_input("¿Cuántos años tienes?", min_value=0, max_value=150)

st.write("Tu nombre:", name)
st.write("Tu edad:", age)


'### `st.sidebar()`'
st.sidebar.write("Estamos añadiento texto a la barra lateral")
st.sidebar.button("¡Un botón lateral!")


'### `st.tabs()`'
tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)


'### `st.empty()`'
with st.empty():
    for seconds in range(5):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write(":material/check: 5 seconds over!")
st.button("Rerun")

#for seconds in range(5):
#    st.write(f"⏳ {seconds} seconds have passed")
#    time.sleep(1)
#st.write(":material/check: 5 seconds over!")
