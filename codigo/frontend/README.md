# Frontend Aegis

## Descrição

Este diretório inclui a entrega para a sprint 03 do grupo Aegis. É importante destacar que este trabalho ainda está em progresso e será melhorado para as próximas entregas. Atualmente, ele se encontra "mockado", isto é, não possui qualquer integração com o frontend. Isso foi feito para que a navegação pela aplicação consiga ser validada.

## Pré-requisitos

Para executar este projeto, você precisará das seguintes ferramentas instaladas no seu sistema:

- **Node.js**: Versão 14.0.0 ou superior
- **npm**: Versão 6.0.0 ou superior (npm é geralmente instalado junto com o Node.js)

## Instruções de Instalação

Siga as etapas abaixo para configurar e executar o projeto localmente.

### 1. Clonar o Repositório

Primeiro, clone este repositório para o seu ambiente local usando o comando:

```bash
git clone https://github.com/Inteli-College/2024-1B-T07-CC06-G04.git
```

### 2. Navegar até o Diretório do Projeto

Entre no diretório do projeto:

```bash
cd codigo/frontend
```

### 3. Instalar Dependências

Instale todas as dependências necessárias executando o comando:

Entre no diretório do projeto clonado:

```bash
npm install
```

### 4. Executar o Projeto

Depois de instalar as dependências, inicie o servidor de desenvolvimento:

```bash
npm start
```

## Telas disponíveis

As telas disponíveis para validação neste momento são:

- ```/``` **Tela de início:** Esta é a tela na qual o usuário poderá fazer o upload do arquivo CSV contendo todos os pontos que deverão ser visitados.

- ```/main``` **Tela principal:** Esta tela contém o _core_ da aplicação. É aqui que o usuário irá executar o algoritmo e/ou simulações e poder obter os resultados gerados. Essa visualização poderá ser obtida tanto no mapa quanto no arquivo CSV disponibilizado para download.

- ```/history``` **Histórico de execução:** Nesta tela é possível observar o histórico de execução dos algoritmos, incluindo data, hora, tipo do algoritmo e status de execução. Ao clicar em visualizar, o usuário é direcionado para a tela principal com os resultados (se já estiverem disponíveis).