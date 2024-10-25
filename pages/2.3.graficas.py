import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.figure_factory as ff
import pydeck as pdk
import graphviz

st.header("Gráficas", divider=True)


'### `st.area_chart()`'
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

'### `st.bar_chart()`'
bar_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["x", "y", "z"])
st.bar_chart(bar_chart_data)

bar_chart_data = pd.DataFrame({
    "x": ["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"],
    "y": [1.5, 2.1, 3.2, 4.0, 1.3, 2.8, 3.5, 4.5, 1.2, 2.6, 3.4, 4.2],
    "a": ["V", "X", "Y", "Z", "V", "X", "Y", "Z", "V", "X", "Y", "Z"]
})
st.bar_chart(bar_chart_data, x="x", y="y", color="a", horizontal=True)


'### `st.line_chart()`'
line_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["m", "n", "o"])
st.line_chart(line_chart_data)

'### `st.scatter_chart()`'
chart_data = pd.DataFrame(np.random.randn(20, 5), columns=["a", "b", "c", "d", "e"])
st.scatter_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
chart_data["col4"] = np.random.choice(["A", "B", "C"], 20)
st.scatter_chart(
    chart_data,
    x="col1",
    y="col2",
    size="col3",
    color="col4",
)

'### `st.map()` (usa `st.pydeck_chart()` por debajo)'
map_data = pd.DataFrame(
    np.random.randn(200, 2) / [50, 50] + [38.99, -1.856], columns=['lat', 'lon'])
st.map(map_data, size=50, color="#55CC55")


'### `st.pyplot()` - Matplotlib'
data = {'value': np.random.normal(loc=0, scale=1, size=300),
    'category': np.random.choice(['A', 'B', 'C'], size=300)}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['category'], df['value'], alpha=0.6)
st.pyplot(fig)

'### `st.pyplot()` - Seaborn (está usando Matplotlib por debajo)'
sns.set_theme(style="darkgrid")
fig, ax = plt.subplots(figsize=(10, 6))
sns.violinplot(x='category', y='value', hue='category', data=df, inner="quart", ax=ax)
st.pyplot(fig)


'### `st.altair_chart()`'
c = (alt.Chart(line_chart_data)
   .mark_circle()
   .encode(x="m", y="n", size="o", color="o", tooltip=["m", "n", "o"]))
st.altair_chart(c, use_container_width=True)


'### `st.vega_lite_chart()`'
st.vega_lite_chart(line_chart_data,
   {
       "mark": {"type": "circle", "tooltip": True},
       "encoding": {
           "x": {"field": "m", "type": "quantitative"},
           "y": {"field": "n", "type": "quantitative"},
           "size": {"field": "o", "type": "quantitative"},
           "color": {"field": "o", "type": "quantitative"},
       }
   })


'### `st.plotly_chart()`'
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']

fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])
st.plotly_chart(fig, use_container_width=True)


'### `st.pydeck_chart()`'
st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=38.99,
            longitude=-1.856,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=map_data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            )
        ],
    )
)

'### `st.graphviz_chart()`'
graph = graphviz.Digraph()
graph.node('A', 'Node A')
graph.node('B', 'Node B')
graph.node('C', 'Node C')
graph.node('D', 'Node D')
graph.edge('A', 'B', 'Edge1')
graph.edge('A', 'C', 'Edge2')
graph.edge('B', 'C', 'Edge3')
graph.edge('C', 'D', 'Edge4')
st.graphviz_chart(graph)
