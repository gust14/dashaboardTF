import pandas as pd

#Função para processar e filtrar os dados que precisamos
def process_data(data):
    df = pd.DataFrame(data)
    orgaos_de_interesse = ['Ministério da Saúde', 'Ministério da Educação', 'Ministério da Defesa']
    df_filtrado = df[df['nomeOrgaoSuperior'].isin(orgaos_de_interesse)]

    # Inicializar valores totais
    saude_valor = 0
    educacao_valor = 0
    defesa_valor = 0

    # Somar valores para cada orgão de interesse
    for orgao in orgaos_de_interesse:
        valores_orgao = df_filtrado[df_filtrado['nomeOrgaoSuperior'] == orgao]['valor']
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
        'Orgão': ['Ministério da Saúde', 'Ministério da Educação', 'Ministério da Defesa'],
        'Valor': [saude_valor, educacao_valor, defesa_valor]
    }
    table_df = pd.DataFrame(table_data)
    return table_df
