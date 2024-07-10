# 📑 Testes do backend realizados através do pytest

Este diretório contém testes automatizados para as APIs do projeto. Utilizamos `pytest` como framework de testes e `TestClient` do `FastAPI` para simular as requisições HTTP.

## 📘 Introdução

Os testes automatizados são essenciais para garantir a estabilidade e a qualidade da aplicação. Eles verificam se as APIs estão funcionando conforme o esperado e ajudam a identificar regressões e bugs.

## ⚙️ Requisitos

- Python 3.8+
- FastAPI
- pytest
- httpx (dependência do TestClient)

## 🛠️ Instalação

1. Clone o repositório para sua máquina local:
    ```bash
    git clone git@github.com:Inteli-College/2024-1B-T07-CC06-G04.git
    ```
   
2. Navegue até o diretório do projeto:
    ```bash
    cd codigo
    ```
3. Verifique se você tem `pip` e `venv` instalados e atualizados:
    ```bash
    python -m pip install --upgrade pip
    python -m pip install --upgrade virtualenv
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

## 🧪 Executando os testes

1. Rode o seguinte comando no seu terminal:
    ```bash
    pytest
    ```

2. Veja o resultado dos testes em seu terminal com uma saída como essa:
    ```bash
    backend\tests_pytest\test_aco_controller.py .      [ 16%]
    backend\tests_pytest\test_csv_controller.py ..     [ 50%]
    backend\tests_pytest\test_main.py .                [ 66%]
    backend\tests_pytest\test_results_controller.py .. [100%] 

    ------- Generated html report: file:///C:/Users/Inteli/Documents/2024-1B-T07-CC06-G04/codigo/test_report.html -------- 
    ================================================= 6 passed in 25.33s =================================================
    ```

3. Auxílio para interpretação:
    - Cada ponto `.` indica um teste bem sucedido.
    - Cada letra `F` indicaria uma falha. Revise o relatório gerado em caso de falhas para obter insights sobre os erros e direcionamento sobre como corrigí-los.

## 🧹 Limpeza Após os Testes

Alguns testes podem criar arquivos ou diretórios temporários (por exemplo, na pasta Services). Esses arquivos e diretórios são automaticamente removidos após a execução dos testes, conforme configurado nos fixtures do pytest.

## 🔍 Detalhamento dos Testes

Nesta seção, é fornecida uma descrição detalhada dos testes realizados em cada _controller_ do backend. Os testes são essenciais para garantir que as _APIs_ do projeto funcionem conforme o esperado e que qualquer alteração ou nova funcionalidade não introduza regressões ou _bugs_. 

Cada arquivo de teste contém múltiplos cenários que verificam o comportamento das rotas definidas em nossa aplicação _FastAPI_. Abaixo, você encontrará uma explicação sobre quais endpoints são testados, os parâmetros utilizados, e as asserções realizadas para garantir a validade das respostas.

### 🌐 test_main

- **Testa o endpoint root**:
    - **`test_read_root`**: Envia uma requisição GET para o endpoint root (`/`).
        - Verifica se o status da resposta é 200.
        - Verifica se a resposta contém a mensagem "Hello, Aegis".

### 🐜 test_aco_controller

- **Testa o endpoint do ACO (Ant Colony Optimization)**:
    - **`test_run_aco`**: Envia uma requisição POST para o endpoint `/run-aco` com parâmetros mínimos.
        - Verifica se o status da resposta é 200.
        - Verifica se a resposta contém um `task_id`.
        - Verifica se a resposta contém a mensagem "Optimization started. Check back later for results."

### 🗂️ test_clustering_controller

- **Setup e Cleanup**:
    - **`setup_environment`**: Configura o ambiente antes dos testes e limpa após os testes, criando e removendo diretórios temporários.

- **Testes de Clustering**:
    - **`test_cluster_csv_no_file_uploaded`**: Testa o endpoint de clustering sem nenhum arquivo CSV carregado.
        - Verifica se o status da resposta é 400.
        - Verifica se a resposta contém a mensagem "No CSV file uploaded yet."
        
    - **`test_cluster_csv_valid_file`**: Testa o endpoint de clustering com um arquivo CSV válido.
        - Faz o upload de um arquivo CSV.
        - Verifica se o status da resposta ao upload é 200.
        - Envia uma requisição para clusterizar o CSV.
        - Verifica se o status da resposta é 200.
        - Verifica se a resposta contém a localização do arquivo clusterizado e se ele existe.
        - Verifica se os dados processados do CSV são válidos.

    - **`test_upload_csv`**: Testa o endpoint de upload de CSV com um arquivo válido.
        - Faz o upload de um arquivo CSV.
        - Verifica se o status da resposta é 200.
        - Verifica se a resposta contém a localização do arquivo.
        - Verifica se os dados processados do CSV são válidos.

### 🗃️ test_csv_controller

- **Setup e Cleanup**:
    - **`clean_services_folder`**: Limpa a pasta de serviços após os testes.

- **Testes de Upload de CSV**:
    - **`test_upload_csv`**: Testa o endpoint de upload de CSV com um arquivo válido.
        - Verifica se o status da resposta é 200.
        - Verifica se a resposta contém a localização do arquivo.
        - Verifica se os dados processados do CSV são válidos.

    - **`test_upload_csv_invalid_format`**: Testa o endpoint de upload de CSV com um arquivo em formato inválido.
        - Verifica se o status da resposta é 400.
        - Verifica se a resposta contém a mensagem "Invalid file format. Please upload a CSV file."

### 📊 test_results_controller

- **Testa o endpoint de histórico de resultados**:
    - **`test_get_history`**: Envia uma requisição GET para o endpoint `/results`.
        - Verifica se o status da resposta é 200.
        - Verifica se a resposta é uma lista.

- **Testa o endpoint de resultados com um ID de tarefa inexistente**:
    - **`test_get_results_not_found`**: Envia uma requisição GET para o endpoint `/results/{task_id}` com um ID de tarefa inexistente.
        - Verifica se o status da resposta é 404.
        - Verifica se a resposta contém a mensagem "Results not found."