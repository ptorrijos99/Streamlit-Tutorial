import streamlit as st
import pandas as pd
import numpy as np

st.header("Datos", divider=True)

"### `st.dataframe` Podemos incluso descargarla como .csv"
df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0))

"### `st.table`"
st.table(df)

"### `st.data_editor`"
df = pd.DataFrame([
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},])
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

"### `st.json`"
st.json({
    "foo": "bar",
        "stuff": [
            "stuff 1",
            "stuff 2",
            "stuff 3",
        ],
        "level1": {"level2": {"level3": {"a": "b"}}},
    },
    expanded=2,
)


"### `st.metric`"
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.metric(label="Active developers", value=123, delta=123, delta_color="off")


"### `st.column_config`"
from datetime import datetime, date
from streamlit.column_config import (
    TextColumn,
    NumberColumn,
    CheckboxColumn,
    SelectboxColumn,
    DatetimeColumn,
    DateColumn,
    AreaChartColumn,
    BarChartColumn,
    LineChartColumn,
)

data = {
    "Widgets": ["st.button", "st.slider", "st.selectbox"],
    "Price (in USD)": [10, 20, 30],
    "Your favorite?": [True, False, True],
    "App Category": ["🤖 LLM", "📈 Data Viz", "📊 Analytics"],
    "Appointment": [
        datetime(2023, 8, 1, 15, 0),
        datetime(2023, 9, 15, 10, 30),
        datetime(2023, 11, 22, 12, 0),
    ],
    "Birthday": [date(1990, 5, 21), date(1985, 8, 14), date(2000, 1, 1)],
    "Sales (last 6 months)": [
        [0, 4, 26, 80, 100, 40],
        [80, 20, 80, 35, 40, 100],
        [10, 20, 80, 80, 70, 0],
    ]
}
df = pd.DataFrame(data)

config = {
    "Widgets": TextColumn("Widgets", max_chars=50, validate="^st\.[a-z_]+$"),
    "Price (in USD)": NumberColumn("Price (in USD)", min_value=0, format="$%d"),
    "Your favorite?": CheckboxColumn("Your favorite?", help="Select your **favorite** widgets"),
    "App Category": SelectboxColumn("App Category", options=["🤖 LLM", "📈 Data Viz"]),
    "Appointment": DatetimeColumn("Appointment", min_value=datetime(2023, 6, 1), format="D MMM YYYY, h:mm a"),
    "Birthday": DateColumn("Birthday", max_value=date(2005, 1, 1), format="DD.MM.YYYY"),
    "Sales (last 6 months)": AreaChartColumn("Sales (last 6 months)", y_min=0, y_max=100),  # Gráfico de área
}

edited_data = st.data_editor(df, column_config=config)