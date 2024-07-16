import pandas as pd
import streamlit as st


#Função para processar e filtrar os dados que precisamos
def process_data(data):
    df = pd.DataFrame(data)
    orgaos_de_interesse = [
        'Ministério da Saúde', 'Ministério da Educação', 'Ministério da Defesa'
    ]
    df_filtrado = df[df['nomeOrgaoSuperior'].isin(orgaos_de_interesse)]

    # Inicializar valores totais
    saude_valor = 0
    educacao_valor = 0
    defesa_valor = 0

    # Somar valores para cada orgão de interesse
    for orgao in orgaos_de_interesse:
        valores_orgao = df_filtrado[df_filtrado['nomeOrgaoSuperior'] ==
                                    orgao]['valor']
        if not valores_orgao.empty:
            if orgao == 'Ministério da Saúde':
                saude_valor = valores_orgao.sum()
            elif orgao == 'Ministério da Educação':
                educacao_valor = valores_orgao.sum()
            elif orgao == 'Ministério da Defesa':
                defesa_valor = valores_orgao.sum()

    return saude_valor, educacao_valor, defesa_valor


def create_table(saude_valor, educacao_valor, defesa_valor):
    table_data = {
        'Orgão': [
            'Ministério da Saúde', 'Ministério da Educação',
            'Ministério da Defesa'
        ],
        'Valor': [saude_valor, educacao_valor, defesa_valor]
    }
    table_df = pd.DataFrame(table_data)
    return table_df


# Retorna todos os dados da API
def create_full_table(data):
    df = pd.DataFrame(data)

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