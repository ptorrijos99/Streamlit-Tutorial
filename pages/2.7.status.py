import streamlit as st
import time

st.header("Información", divider=True)

'### `st.success()`'
st.success("¡Todo está bien!", icon="✅")

'### `st.info()`'
st.info("Aquí va información importante.", icon="ℹ️")

'### `st.warning()`'
st.warning("¡Cuidado!", icon="⚠️")

'### `st.error()`'
st.error("¡Algo salió mal!", icon="🚨")

'### `st.exception()`'
try:
    1 / 0
except Exception as e:
    st.exception(e)


st.header("Barras de progreso y otros", divider=True)

'### `st.progress()`'
if st.button("Haz clic para iniciar un proceso"):
    progress_bar = st.progress(0)

    for i in range(100):
        time.sleep(0.02)  
        progress_bar.progress(i)

    st.success("¡Proceso completado!")


'### `st.spinner()`'
if st.button("Haz clic para cargar algo"):
    with st.spinner("Cargando, por favor espera..."):
        time.sleep(2)  
    st.success("¡Carga completa!")


'### `st.status()`'
if st.button("Haz clic para ejecutar una tarea"):
    with st.status("Ejecutando tarea..."):
        time.sleep(2)  
    st.success("¡Tarea completada!")


'### `st.toast()`'
if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')

if st.button('Cook breakfast'):
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")


'### `st.balloons()`'
if st.button("Haz clic para celebrar"):
    st.balloons()


'### `st.snow()`'
if st.button("Haz clic para ver copos de nieve"):
    st.snow()
