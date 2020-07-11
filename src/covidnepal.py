## Python application that gives visual of covid infection in Nepal. 
## Disclaimer: This is based on fake data. 
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

DATE_TIME = "date/time"
DATA_URL = (
    "covidnepal.csv"
)

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    # data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data(1000)

##Raw Data
'This is based on Imaginary Data', data



'This is based on imaginary data. Made just for the purpose of demo', st.map(data)
