import pandas as pd
import streamlit as st
#Função para exportar dados como CSV
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')
