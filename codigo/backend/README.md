# Backend Aegis

Esse projeto foi desenvolvido utilizando o framework FastAPI. Ele inclui as funcionalidades para o processamento de arquivos CSV e otimização de rotas usando diversos algoritmos de otimização. Abaixo, são exibidas duas formas de utilizar o backend desenvolvido por este grupo, sendo uma delas a inicialização de um servidor que estará ouvindo quaisquer requisições feitas, bem como a implementação de uma Command Line Interface (CLI) para que não haja a necessidade de utilizar ferramentas como Postman ou mesmo uma aplicação web para verificar os endpoints.

## Requisitos

- Python 3.7 ou superior

## Instalação

1. Clone o repositório para sua máquina local:
    ```bash
    git clone git@github.com:Inteli-College/2024-1B-T07-CC06-G04.git
    ```
   
2. Navegue até o diretório do projeto:
    ```bash
    cd codigo
    ```

3. Crie um ambiente virtual (recomendado) e ative-o:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

4. Instale as dependências necessárias listadas no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Executando o Projeto - Servidor para utilização em páginas web

1. Navegue até o diretório do backend:
    ```bash
    cd backend
    ```

2. Execute o aplicativo FastAPI utilizando o Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```

3. Acesse a aplicação no seu navegador em `http://127.0.0.1:8000`.

4. Acesse a documentação da API `http://127.0.0.1:8000/docs`.

## Endpoints Disponíveis

### Raiz

- **GET /**
    - **Descrição**: Endpoint raiz que retorna uma mensagem de boas-vindas.
    - **Retorno**: `{"message": "Hello, Aegis"}`

### CSV

- **POST /upload-csv**
    - **Descrição**: Faz o upload de um arquivo CSV, processa e aplica clustering nos dados.
    - **Parâmetros**:
        - `file`: Arquivo CSV a ser enviado.
    - **Retorno**: Localização do arquivo original e do arquivo clusterizado.

### Ant Colony Optimization

- **POST /run-aco**
    - **Descrição**: Inicia a otimização por colônia de formigas em segundo plano.
    - **Parâmetros**:
        - `num_ants`: Número de formigas.
        - `alpha`: Influência dos feromônios na direção.
        - `beta`: Influência da distância na direção.
        - `evaporation_rate`: Taxa de evaporação dos feromônios.
        - `iterations`: Número de iterações.
    - **Retorno**: ID da tarefa e mensagem de confirmação.

- **GET /results/{task_id}**
    - **Descrição**: Obtém os resultados da otimização com base no ID da tarefa.
    - **Parâmetros**:
        - `task_id`: ID da tarefa gerado na chamada do endpoint `/run-aco`.
    - **Retorno**: Resultados da otimização.

### OR Tools

- **POST /api/run-ortools**
    - **Descrição**: Inicia a otimização utilizando a bibilioteca OR-Tools em segundo plano.
    - **Parâmetros**: Nenhuma parâmetro é necessário.
    - **Retorno**: ID da tarefa e mensagem de confirmação.

- **GET /results/{task_id}**
    - **Descrição**: Obtém os resultados da otimização com base no ID da tarefa.
    - **Parâmetros**:
        - `task_id`: ID da tarefa gerado na chamada do endpoint `/api/run-ortools`.
    - **Retorno**: Resultados da otimização.


## Executando o Projeto - Command Line Interface

1. Navegue até o diretório do backend:
    ```bash
    cd backend
    ```

2. Execute o arquivo python referente à CLI:
    ```bash
    python cli.py
    ```

3. Será exibido um menu semelhante a este. Selecione a opção que mais se adequa ao que você gostaria de fazer.
    ```bash
     █████  ███████  ██████  ██ ███████
    ██   ██ ██      ██       ██ ██
    ███████ █████   ██   ███ ██ ███████
    ██   ██ ██      ██    ██ ██      ██
    ██   ██ ███████  ██████  ██ ███████


     ██████ ██      ██
    ██      ██      ██
    ██      ██      ██
    ██      ██      ██
     ██████ ███████ ██



    Bem vindo!

    Escolha um endpoint para rodar:
    1: Healthy Check
    2: Upload CSV
    3: Rodar Ant Colony Optimization
    4: Pegar Tarefa Ant Colony Optimization
    0: Sair
    Digite o número do endpoint que você deseja visitar ou 'S' para sair:
    ```

### 1. Healthy Check

- **Descrição**: Retorna uma mensagem de boas vindas se tudo estiver correndo bem na aplicação e ela conseguir ser inicializada com êxito.
- **Retorno**: `{"message": "Hello, Aegis"}`

### 2. Upload CSV

- **Descrição**: Faz o upload de um arquivo CSV, processa e aplica clustering nos dados.
- **Parâmetros**:
    - `file`: Arquivo CSV a ser enviado. Será solicitado que você informe o caminho para algum arquivo .CSV. Informe o **caminho absoluto** até um csv na sua máquina.
- **Retorno**: Localização do arquivo original e do arquivo clusterizado.

### 3. Ant Colony Optimization

- **Descrição**: Inicia a otimização por colônia de formigas em segundo plano.
- **Parâmetros**: Estes parâmetros serão solicitados um a um quando solicitada a opção de executar o algoritmo ACO.
    - `num_ants`: Número de formigas.
    - `alpha`: Influência dos feromônios na direção.
    - `beta`: Influência da distância na direção.
    - `evaporation_rate`: Taxa de evaporação dos feromônios.
    - `iterations`: Número de iterações.
- **Retorno**: ID da tarefa e mensagem de confirmação.

### 4. Ant Colony Optimization
- **Descrição**: Obtém os resultados da otimização com base no ID da tarefa.
- **Parâmetros**:
    - `task_id`: ID da tarefa gerado na chamada do endpoint `/run-aco`. erá solicitado que você informe o id no terminal.
- **Retorno**: Resultados da otimização.

### S. Sair
- **Descrição**: Encerra a CLI.