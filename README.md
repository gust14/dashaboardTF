# Dashboard - Recursos Transferidos

Este projeto é um dashboard interativo para visualização de recursos transferidos, desenvolvido com Python e Streamlit. O objetivo é facilitar a visualização de dados financeiros recebidos por diferentes estados do Brasil com base no Orgão Superior.

Nesse momento estamos retornando o valor total tranferido para o Ministério da Saúde, Ministério da Educação e Ministério da Defesa. 

Também estamos organizando todos os dados refernete ao perido escolhido pelo usuario onde mesmo pode saber todos os dados retornados e caso for necessario exportar no formato CSV.

## API de Dados | Portal da Transparência do Governo Federal
Para consultar os dados precisamos criar um chave de API. Com ela, é possível ter um serviço de consulta direta aos dados do Portal da Transparência sem precisar navegar pelo site ou utilizar robôs para a obtenção das informações de forma automática. Os dados disponíveis são os mesmos apresentados em tela, com a flexibilidade característica das APIs.

Para fazer uso da API, deve-se realizar o cadastro de um e-mail em [API de dados - Cadastrar emial](http://portaldatransparencia.gov.br/api-de-dados/cadastrar-email) 

Através do e-mail cadastrado, você receberá um token, que deverá ser usado nas suas consultas via API.

## Funcionalidades

- Escolha de período de tempo (mês/ano de início e fim). 
- Seleção de Unidade Federativa (UF).
- Consulta de dados de recursos transferidos de diferentes ministérios.
- Exibição de tabela com os valores recebidos por cada ministério.
- Gráfico de pizza ilustrando a distribuição dos valores recebidos.
- Exportação dos dados em formato CSV.

## Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Matplotlib
- Requests
- Aiohttp (para requisições assíncronas)

## Estrutura do Projeto

O projeto está organizado nos seguintes arquivos:

- `main.py`: Arquivo principal que inicializa o dashboard e gerencia a interface do usuário. O usuario pode fazer a consulta utilizando os filtros. Ao clicar em buscar fazemos a consulta para coletar os dados.
- `config.py`: Configurações do projeto, incluindo layout do Streamlit. Essa função é mais para determinar um titulo e um icone do site. Mas é possível definir outras configurações.
- `data_fetcher.py`: Funções para buscar dados da API de forma assíncrona. Essa função faz a coleta dos dados.
- `data_processor.py`: Funções para processar e filtrar os dados. 
- `data_visualizer.py`: Funções para gerar gráficos baseados nos dados.
- `exporter.py`: Funções para exportar dados em formato CSV.

## Como Executar o Projeto

1. Clone este repositório:
    ```sh
    git clone https://github.com/gust14/dashaboardTF.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd dashaboardTF
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Execute o dashboard:
    ```sh
    streamlit run main.py
    ```

## Detalhes da Implementação

### `config.py`

Contém as configurações padrão para o layout do Streamlit e outras configurações globais.

### `data_fetcher.py`

Contém funções assíncronas para buscar dados da API, utilizando `aiohttp` para melhorar a performance das requisições. Inclui uma barra de progresso para informar o usuário sobre o status da consulta.

### `data_processor.py`

Processa e filtra os dados retornados da API, criando uma tabela com os valores recebidos por cada ministério. Além de retornar todos os dados em uma tabela, sendo possível exportar no formato CSV.

### `data_visualizer.py`

Gera gráficos de pizza para ilustrar a distribuição dos valores recebidos por cada ministério, utilizando `matplotlib`.

### `exporter.py`

Funções para exportar os dados processados em formato CSV.

## Exemplo de Uso

1. Execute o dashboard.
2. Escolha o período desejado (mês/ano de início e fim).
3. Selecione a UF de interesse.
4. Clique no botão "Buscar" para visualizar os dados.
5. Acompanhe o progresso da consulta na barra de progresso.
6. Veja os resultados na tabela e no gráfico de pizza.
7. Exporte os dados em formato CSV se necessário
8. Acessar site:[Site](https://dashaboardtf.streamlit.app/)


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT. 

## Contato

Para dúvidas ou sugestões, entre em contato:

- Nome: Ghu Solf
- Email: gusttavosolf@gmail.com
- GitHub: [gust14](https://github.com/gust14)

## Projeto

Esse projeto foi desenvolvido para disciplina de Fábrica de
Software da Universidade de Santa Cruz do Sul. Integrantes: Luis Gustavo, Matheus Barreto, Anna Santos


