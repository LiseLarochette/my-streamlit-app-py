import streamlit as st
import pandas as pd
from datetime import datetime

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)

your-repository/
├── .streamlit/
│   └── config.toml
├── pages/
│   ├── admin.py
│   ├── super-admin.py
│   └── user.py
├── menu.py
└── app.py

import streamlit as st

st.https://wilder.streamlit.app/("my_streamlit_app.py", label="Home", icon="🏠")
st.https://wilder.streamlit.app/("pages/page_1.py", label="Page 1", icon="1️⃣")
st.https://wilder.streamlit.app/("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.https://wilder.streamlit.app/("http://www.google.com", label="Google", icon="🌎")

# Here we use "magic commands":
df_weather

#afficher le graphique de la température maximale
st.line_chart(df_weather['MAX_TEMPERATURE_C'])




import seaborn as sns
df_weather = df_weather.drop(["DATE", "OPINION"], axis=1)

viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

import streamlit as st

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")
