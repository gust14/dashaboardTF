import matplotlib.pyplot as plt
import streamlit as st

#Função para criar gráficos e tabelas.
@st.cache_data
def gerar_grafico_pizza(table_df):
    fig, ax = plt.subplots()
    ax.pie(table_df['Valor'], labels=table_df['Orgão'], autopct=lambda p: 'R$ {:,.2f}'.format(p * sum(table_df['Valor']) / 100))
    ax.axis('equal')  
    plt.title('Distribuição de Valores por Ministério')
    return fig
