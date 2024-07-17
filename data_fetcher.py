import aiohttp
import asyncio
import streamlit as st

# Função assíncrona para buscar todos os dados da API com barra de progresso e informação final
async def fetch_all_data(api_url, params, headers):
    #Cria uma sessão assíncrona usando aiohttp.ClientSession(). Essa sessão é usada 
    #para fazer requisições HTTP assíncronas.
    async with aiohttp.ClientSession() as session:
        #Inicializa uma lista vazia all_data que será usada para armazenar todos os dados obtidos da API.
        all_data = []
        current_page = 1
        #Essa variável será usada para contar quantas páginas foram consultadas com sucesso.
        total_pages = 0

        # Determinar um limite máximo de páginas para evitar loops infinitos
        max_pages = 2000

        # Criar a barra de progresso
        progress_bar = st.progress(0)
        # inicia um loop que continuará até current_page ser maior que max_pages.
        while current_page <= max_pages:
            params["pagina"] = current_page
            #requisição GET assíncrona à api_url, passando params como parâmetros da consulta e headers como cabeçalhos da requisição. O resultado da requisição é armazenado em response.
            async with session.get(api_url, params=params, headers=headers) as response:
                if response.status == 200:
                    #Converte o conteúdo da resposta para JSON de forma assíncrona usando await response.json() e armazena em data.
                    data = await response.json()
                    if data:
                        #Adiciona os dados obtidos (data) à lista all_data.
                        all_data.extend(data)
                        #Incrementa current_page para avançar para a próxima página na próxima iteração do loop.
                        current_page += 1
                        #Incrementa total_pages para contar mais uma página consultada com sucesso.
                        total_pages += 1
                        # Calcular a porcentagem de progresso
                        progress_percent = current_page / max_pages
                        # Limitar a porcentagem entre 0.0 e 1.0
                        progress_percent = min(progress_percent, 1.0)
                        progress_bar.progress(progress_percent)
                    else:
                        break #Caso data esteja vazio (sem dados), quebra o loop.
                else:
                    st.error(f"Erro ao consultar a API: {response.status}")
                    break

        # Atualizar a barra de progresso para 100% no final da consulta
        progress_bar.progress(1.0)

        # Exibir card com o total de páginas consultadas
        st.info(f"Total de páginas consultadas: {total_pages}")

        return all_data


#Essa função fetch_data configura um ambiente assíncrono para chamar uma função 
#(fetch_all_data) que faz uma consulta assíncrona a uma API. 
#Ela cria um loop de eventos assíncrono, executa a função assíncrona fetch_all_data #de forma síncrona dentro desse loop e retorna os dados obtidos da API. Isso é útil #em aplicações web ou outras situações onde a espera assíncrona por dados de uma API é necessária sem bloquear a thread principal.
def fetch_data(api_url, params, headers):
    # Cria um novo loop de eventos assíncrono
    loop = asyncio.new_event_loop()
    # Define o loop de eventos criado como o loop de eventos atual
    asyncio.set_event_loop(loop)
    # Executa a função fetch_all_data de forma síncrona dentro do loop de eventos
    data = loop.run_until_complete(fetch_all_data(api_url, params, headers))
    # Retorna os dados obtidos da API
    return data




"""
# Função assíncrona para buscar todos os dados da API com barra de progresso e debug
async def fetch_all_data(api_url, params, headers):
    async with aiohttp.ClientSession() as session:
        all_data = []
        current_page = 1
        max_pages = 32  # Definir um limite máximo para evitar loops infinitos

        with st.spinner("Aguarde, estamos processando sua solicitação..."):
            progress_bar = st.progress(0)
            while current_page <= max_pages:
                params["pagina"] = current_page
                async with session.get(api_url, params=params, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data:
                            all_data.extend(data)
                            current_page += 1
                            st.write(f"Consultando página {current_page - 1}...")  # Debug para exibir página atual
                            progress_bar.progress(current_page / max_pages)
                        else:
                            break
                    else:
                        st.error(f"Erro ao consultar a API: {response.status}")
                        break

        progress_bar.empty()  # Limpar barra de progresso ao finalizar
        return all_data

# Função para buscar dados usando um loop de evento assíncrono
def fetch_data(api_url, params, headers):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    data = loop.run_until_complete(fetch_all_data(api_url, params, headers))
    return data
"""