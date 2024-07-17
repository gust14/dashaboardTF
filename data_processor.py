import pandas as pd
import streamlit as st


#Função para processar e filtrar os dados que precisamos
def process_data(data): 
    #Cria um DataFrame do pandas a partir dos dados passados como argumento.
    df = pd.DataFrame(data)
    orgaos_de_interesse = [
        'Ministério da Saúde', 'Ministério da Educação', 'Ministério da Defesa'
    ]
    #Filtra o DataFrame para incluir apenas linhas onde a coluna nomeOrgaoSuperior contenha valores presentes na lista orgaos_de_interesse.
    df_filtrado = df[df['nomeOrgaoSuperior'].isin(orgaos_de_interesse)]

    # Inicializar valores totais
    saude_valor = 0
    educacao_valor = 0
    defesa_valor = 0

    # Somar valores para cada orgão de interesse
    for orgao in orgaos_de_interesse:
        #Seleciona os valores da coluna valor para o ministério atual.
        valores_orgao = df_filtrado[df_filtrado['nomeOrgaoSuperior'] == orgao]['valor']
        #Verifica se há valores para o ministério atual.
        if not valores_orgao.empty:
            if orgao == 'Ministério da Saúde':
                saude_valor = valores_orgao.sum()
            elif orgao == 'Ministério da Educação':
                educacao_valor = valores_orgao.sum()
            elif orgao == 'Ministério da Defesa':
                defesa_valor = valores_orgao.sum()
                
    #Retorna os valores totais calculados para cada ministério.
    return saude_valor, educacao_valor, defesa_valor


def create_table(saude_valor, educacao_valor, defesa_valor):
    table_data = {
        'Orgão': [
            'Ministério da Saúde', 'Ministério da Educação',
            'Ministério da Defesa'
        ],
        'Valor': [saude_valor, educacao_valor, defesa_valor]
    }
    table_df = pd.DataFrame(table_data) #Converte table_data em um DataFrame 
    return table_df #nomes dos ministérios e os valores associados a eles.


# Retorna todos os dados da API
def create_full_table(data):
    df = pd.DataFrame(data) #DataFrame do pandas a partir dos dados passados como argumento.


    # Formatar a coluna 'anoMes' para exibir como 'MM/YYYY'
    df['anoMes'] = pd.to_datetime(df['anoMes'], format='%Y%m').dt.strftime('%m/%Y')

    # Formatar a coluna 'valor' para exibir como 'R$ X.XX'
    df['valor'] = df['valor'].apply(lambda x: f'R$ {x:,.2f}')

    # Adicionar um link na barra lateral para a tabela completa
    st.sidebar.markdown(f"### [Valores retornados](#valores-retornados)")
    st.sidebar.info(
        "Tabela com todos os campos retornados pela consulta da API.")

    # Criar âncora para a tabela completa
    st.markdown('<a name="valores-retornados"></a>', unsafe_allow_html=True)

    # Mostrar a tabela completa
    st.dataframe(df)

    return df