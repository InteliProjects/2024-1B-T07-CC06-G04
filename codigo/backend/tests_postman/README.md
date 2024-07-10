# Testes do backend realizados através do postman

&emsp;&emsp;O _Postman_ é uma ferramenta popular utilizada para desenvolver, testar e documentar APIs. Ele permite que os desenvolvedores enviem solicitações HTTP a um servidor e visualizem as respostas. A ferramenta é especialmente útil para testar endpoints de APIs RESTful, como os criados com FastAPI.

&emsp;&emsp;Neste projeto, o Postman foi usado para testar as rotas do backend, garantindo que todas as funcionalidades da API estejam operando conforme o esperado. Através do _Postman_, é possível simular diferentes cenários de uso e verificar as respostas do servidor, além de documentar cada um dos endpoints testados.

&emsp;&emsp;A coleção dos testes e requisições realizadas pode ser encontrada através do arquivo Json "Aegis.postman_collections.json" com o seguinte caminho dentro do repositório (essa mesma pasta): `codigo\backend\tests_postman\Aegis.postman_collection.json`

&emsp;&emsp;Para rodar a coleção é só abrir o seu aplicativo do _Postman_ no desktop ou navegador, clicar em "import" e subir o arquivo json da collection.

## GET http://127.0.0.1:8000/

&emsp;&emsp;Esta rota é a rota raiz da aplicação, usada para verificar se o servidor está funcionando corretamente. Quando acessada, ela retorna uma mensagem simples.

**Resposta:**
```json
{
    "message": "Hello, Aegis"
}
```

## POST http://127.0.0.1:8000/upload-csv

&emsp;&emsp;Esta rota é usada para fazer o upload de um arquivo CSV. O arquivo CSV é processado e armazenado no sistema, e um arquivo CSV clusterizado é gerado e armazenado.

Arquivo usado: amostra_total.csv (Localizado nessa mesma pasta)

**Resposta:**
```json
{
    "file_location": "./Services/uploaded_files/uploaded_file.csv",
}
```

## POST http://127.0.0.1:8000/cluster-csv

&emsp;&emsp;Esta rota é usada para clusterizar um arquivo CSV previamente carregado. Os parâmetros necessários para clusterização devem ser fornecidos na URL.

**Parâmetros usados no teste:**
- n_clusters_primary: 50
- n_clusters_secondary: 22

**Resposta:**
```json
{
    "clustered_file_location": "./Services/clusters/clustered_file.csv",
}
```

## POST http://127.0.0.1:8000/run-aco

&emsp;&emsp;Esta rota é usada para iniciar o algoritmo de Otimização por Colônia de Formigas (ACO). Os parâmetros necessários para rodar o algoritmo devem ser fornecidos no corpo da solicitação.

**Parâmetros necessários para rodar:**
- num_ants: Número de formigas
- alpha: Parâmetro alfa
- beta: Parâmetro beta
- evaporation_rate: Taxa de evaporação
- iterations: Número de iterações

**Parâmetros usados no teste:**
- num_ants: 5
- alpha: 1.0
- beta: 1.0
- evaporation_rate: 0.5
- iterations: 10

**Resposta:**
```json
{
    "task_id": "81a8fe40-9a67-4ca7-9473-fd27edb5f961",
    "message": "Optimization started. Check back later for results."
}
```

## POST http://127.0.0.1:8000/api/run-ortools

&emsp;&emsp;Esta rota é usada para iniciar o algoritmo de otimização utilizando uma ferramente do Google chamada OR Tools. Não é necessário fornecer nenhum parâmetro para que ela seja executada.

**Resposta:**
```json
{
    "task_id": "83aa9696-f0a8-4fa8-94dd-c81ebd46d50f",
    "message": "Optimization started. Check back later for results."
}
```

## GET http://127.0.0.1:8000/results/{task_id}

&emsp;&emsp;Esta rota é usada para obter os resultados da otimização para um determinado task_id. O task_id é fornecido quando a otimização é iniciada.

ID usado no teste: `dda2fed7-995a-4e14-959e-bf860ac87829`

**Resposta:**
O arquivo contendo a resposta da requisição foi apagado para manter a segurança dos dados da aplicação.

## GET http://127.0.0.1:8000/results

&emsp;&emsp;Esta rota é usada para obter os resultados de todas as otimizações realizadas, retornando um array de objetos com todas as otimizações já realizadas pelo algoritmo.

**Resposta:**
O arquivo contendo a resposta da requisição foi apagado para manter a segurança dos dados da aplicação.