import streamlit as st
import time

from config import set_config
from data_fetcher import fetch_data
from data_processor import process_data, create_table, create_full_table
from data_visualizer import gerar_grafico_pizza
from exporter import convert_df

# Configurações padrão
set_config()

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
                "pagina": 1  # página inicial
            }
            # Headers para a API
            headers = {
                "accept": "application/json",
                "chave-api-dados": "3cecdb8d3b0aac90c2a30386cfcb2c3c"
            }

            # Buscar todos os dados
            data = fetch_data(api_url, params, headers)

            # Verificar se há dados retornados
            if data:
                # Processar os dados
                saude_valor, educacao_valor, defesa_valor = process_data(data)

                table_df = create_table(saude_valor, educacao_valor, defesa_valor)

                # Exibir resultados
                with col2:
                    st.write(" ")
                    st.write(f"Estado de {uf} recebeu os seguintes valores:")

                    # Formatar valores como moeda para exibição
                    table_df_formatted = table_df.copy()
                    table_df_formatted['Valor'] = table_df_formatted['Valor'].apply(lambda x: f'R${x:,.2f}')

                    st.write(table_df_formatted.to_html(index=False, justify='center'), unsafe_allow_html=True)

                    # Botão para exportar tabela
                    csv = convert_df(table_df)

                    st.download_button(
                        "Exportar tabela",
                        csv,
                        "recursos_transferidos_{}.csv".format(uf),
                        "text/csv",
                        False
                    )


                    # Informativo
                    st.write(" ")  
                    st.write(f"Estado de {uf} recebeu o valor para Saúde de: <span style='color: #85EA2D'>R${saude_valor:,.2f}</span> 💸", unsafe_allow_html=True)
                    st.write(f"Estado de {uf} recebeu o valor para Educação de: <span style='color: #85EA2D'>R${educacao_valor:,.2f}</span> 📚", unsafe_allow_html=True)
                    st.write(f"Estado de {uf} recebeu o valor para Segurança de: <span style='color: #85EA2D'>R${defesa_valor:,.2f}</span> 💪", unsafe_allow_html=True)

                    # Mostrar gráficos
                    st.write("### Gráfico de Pizza")
                    st.pyplot(gerar_grafico_pizza(table_df))
                    
                    # Exibir tabela completa dos valores retornados
                    st.write("### Tabela Completa dos Valores Retornados")
                    create_full_table(data)


            else:
                st.error("Nenhum dado retornado para os parâmetros fornecidos.")
    else:
        # Exibir mensagem de instrução se o botão não foi clicado
        st.info("Selecione os parâmetros e clique em 'Buscar' para visualizar as informações de Recursos Transferidos para um estado")
