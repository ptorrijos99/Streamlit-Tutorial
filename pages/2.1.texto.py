import streamlit as st

st.header("Texto", divider=True)

# Markdown
st.markdown("*Streamlit* suppors **Markdown**. You can, for example, include [links](https://www.streamlit.io/).")

# Título
st.title("The app title: _Streamlit_ is :blue[cool] :sunglasses:")

# Encabezado
st.header("This is a header", divider=True)

# Subencabezado
st.subheader("This is a subheader", divider=True)

# Leyenda
st.caption("This is written small caption text")

# Bloque de Código
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

# Echo
with st.echo():
    a = 5
    b = 10
    st.write(f"La suma de {a} y {b} es {a + b}")
    
# Texto Preformateado
st.text("This is some text.")

# LaTeX
st.latex("\int a x^2 \,dx")

# Divisor
st.divider()
st.write("---")
"---"