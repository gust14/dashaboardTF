import streamlit as st
import requests
import pandas as pd
import time

# Título do dashboard
st.title("Dashboard - Recursos Transferidos")

# Cabeçalho para os parâmetros de busca
st.header("Parâmetros de busca")

# Criar duas colunas para os filtros e o gráfico
col1, col2 = st.columns((1, 3))

# Filtros de busca
with col1:
    # Input para escolher o mês e ano de início
    mes_ano_inicio = st.text_input("Escolha Mês/Ano Inicio (MM/AAAA)")

    # Input para escolher o mês e ano de fim
    mes_ano_fim = st.text_input("Escolha Mês/Ano Fim (MM/AAAA)")

    # Selectbox para escolher a UF
    uf = st.selectbox("Sigla UF", ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"])

    # Botão para buscar os dados
    if st.button("Buscar"):
        # Exibir mensagem de espera com spinner
        with st.spinner("Aguarde, estamos processando sua solicitação..."):
            # Delay de 2 segundos para simular o processamento
            time.sleep(2)

            # Parâmetros para a API
            api_url = "https://api.portaldatransparencia.gov.br/api-de-dados/despesas/recursos-recebidos"
            params = {
                "mesAnoInicio": mes_ano_inicio,
                "mesAnoFim": mes_ano_fim,
                "uf": uf,
                "pagina": 1  # página sempre como 1
            }

            # Headers para a API
            headers = {
                "accept": "*/*",
                "chave-api-dados": "3cecdb8d3b0aac90c2a30386cfcb2c3c"
            }

            # Requisição GET para a API
            response = requests.get(api_url, params=params, headers=headers)

            # Verificar se a resposta foi bem-sucedida
            if response.status_code == 200:
                # Converter a resposta em JSON
                data = response.json()

                # Processar os dados
                df = pd.DataFrame(data)

                # Filtrar e agrupar os dados
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

                # Exibir resultados
                col2.write(" ")  
                col2.write(f"Estado de {uf} recebeu o valor para Saúde de: <span style='color: #85EA2D'>R${saude_valor:,.2f}</span> 💸", unsafe_allow_html=True)
                col2.write(f"Estado de {uf} recebeu o valor para Educação de: <span style='color: #85EA2D'>R${educacao_valor:,.2f}</span> 📚", unsafe_allow_html=True)
                col2.write(f"Estado de {uf} recebeu o valor para Segurança de: <span style='color: #85EA2D'>R${defesa_valor:,.2f}</span> 💪", unsafe_allow_html=True)
            else:
                # Exibir erro se a resposta não foi bem-sucedida
                st.error("Erro ao consultar a API")
    else:
        # Exibir mensagem de instrução se o botão não foi clicado
        st.info("Selecione os parâmetros e clique em 'Buscar' para visualizar as informações de Recursos Transferidos")