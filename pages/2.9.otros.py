import streamlit as st
import sqlite3
import pandas as pd
import requests

st.subheader("Execution flow", divider=True)


'### `st.stop()`'	

if st.button("Stop the script"):
    st.stop()

name = st.text_input("Name")
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success("Thank you for inputting a name.")


'### `st.rerun()`'	

if "value" not in st.session_state:
    st.session_state.value = "Title"

##### Option using st.rerun #####
st.subheader(st.session_state.value)
if st.button("Foo"):
    st.session_state.value = "Foo"
    st.rerun()

##### Option using a callback #####
st.subheader(st.session_state.value)
def update_value():
    st.session_state.value = "Bar"
st.button("Bar", on_click=update_value)



'### `st.fragment` - Ejemplo 1'	

if "clicks" not in st.session_state:
    st.session_state.clicks = 0

@st.fragment
def count_to_five():
    if st.button("Plus one!"):
        st.session_state.clicks += 1
        if st.session_state.clicks % 5 == 0:
            st.rerun()
    return

count_to_five()
st.subheader(f"Multiples of five clicks: {st.session_state.clicks // 5}")

if st.button("Check click count"):
    st.toast(f"## Total clicks: {st.session_state.clicks}")



'### `st.fragment` - Ejemplo 2'	

if "app_runs" not in st.session_state:
    st.session_state.app_runs = 0
    st.session_state.fragment_runs = 0

@st.fragment
def my_fragment():
    st.session_state.fragment_runs += 1
    st.button("Rerun fragment")
    st.write(f"Fragment says it ran {st.session_state.fragment_runs} times.")

st.session_state.app_runs += 1
my_fragment()
st.button("Rerun full app")
st.write(f"Full app says it ran {st.session_state.app_runs} times.")
st.write(f"Full app sees that fragment ran {st.session_state.fragment_runs} times.")



st.header("Caché", divider=True)


'### `st.session_state()`'
st.write("Click the button to increment the counter")
if "counter" not in st.session_state:
    st.session_state.counter = 0
if st.button("Increment"):
    st.session_state.counter += 1
st.write(f"Counter: {st.session_state.counter}")


'### `st.cache_data()` y `st.cache_resource()`'

st.image("https://docs.streamlit.io/images/caching-high-level-diagram.png", caption="Caching")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")


@st.cache_data
def get_coordinates(location):
    url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            return float(lat), float(lon)
        else:
            return None, None
    else:
        return None, None

st.write(get_coordinates("Albacete"))
st.write(get_coordinates("Albacete"))
st.write(get_coordinates("Cuenca"))


st.header("Diálogos y formularios", divider=True)

'### `st.dialog()`'

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"

if st.button("Reiniciar votación"):
    st.session_state.pop("vote", None)
    st.rerun()


'### `st.form()` y `st.form_submit_button()`'

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("slider", slider_val, "checkbox", checkbox_val)



st.header("Query params", divider=True)

'### `st.query_params()`'
# http://localhost:8501/.9.otros?name=Pablo

if "name" in st.query_params:
    st.write(f"Hola, {st.query_params['name']}!")
    

