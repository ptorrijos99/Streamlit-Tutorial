import streamlit as st

pg = st.navigation([
    st.Page("pages/2.1.texto.py", title="2.1. Texto", icon="📝"),
    st.Page("pages/2.2.datos.py", title="2.2. Datos", icon="📊"),
    st.Page("pages/2.3.graficas.py", title="2.3. Gráficas", icon="📈"),
    st.Page("pages/2.4.input.py", title="2.4. Input", icon="🧩"),
    st.Page("pages/2.5.media.py", title="2.5. Media", icon="🎥"),
    st.Page("pages/2.6.layouts.py", title="2.6. Layouts", icon="🔲"),
    st.Page("pages/2.7.status.py", title="2.7. Status", icon="🛠️"),
    st.Page("pages/2.8.chat.py", title="2.8. Chat", icon="💬"),
    st.Page("pages/2.9.otros.py", title="2.9. Otros", icon="🔧")
])
pg.run()