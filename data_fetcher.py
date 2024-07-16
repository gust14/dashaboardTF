import aiohttp
import asyncio
import streamlit as st

# Função assíncrona para buscar todos os dados da API com barra de progresso e informação final
async def fetch_all_data(api_url, params, headers):
    async with aiohttp.ClientSession() as session:
        all_data = []
        current_page = 1
        total_pages = 0

        # Determinar um limite máximo de páginas para evitar loops infinitos
        max_pages = 2000

        # Criar a barra de progresso
        progress_bar = st.progress(0)

        while current_page <= max_pages:
            params["pagina"] = current_page
            async with session.get(api_url, params=params, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    if data:
                        all_data.extend(data)
                        current_page += 1
                        total_pages += 1
                        # Calcular a porcentagem de progresso
                        progress_percent = current_page / max_pages
                        # Limitar a porcentagem entre 0.0 e 1.0
                        progress_percent = min(progress_percent, 1.0)
                        progress_bar.progress(progress_percent)
                    else:
                        break
                else:
                    st.error(f"Erro ao consultar a API: {response.status}")
                    break

        # Atualizar a barra de progresso para 100% no final da consulta
        progress_bar.progress(1.0)

        # Exibir card com o total de páginas consultadas
        st.info(f"Total de páginas consultadas: {total_pages}")

        return all_data

def fetch_data(api_url, params, headers):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    data = loop.run_until_complete(fetch_all_data(api_url, params, headers))
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