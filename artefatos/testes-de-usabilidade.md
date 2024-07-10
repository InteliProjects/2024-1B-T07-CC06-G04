# Documentação dos Testes de Usabilidade

## Introdução

&emsp;&emsp;Os testes de usabilidade são um componente vital no ciclo de desenvolvimento de qualquer solução tecnológica. Eles garantem que o produto final seja intuitivo, eficiente e alinhado com as necessidades dos usuários finais. No contexto do nosso projeto, focado na otimização de rotas de leitura de hidrômetros para a Aegea Saneamento, a realização desses testes é essencial para validar e aprimorar a solução proposta. Este documento visa registrar os procedimentos, objetivos, resultados esperados e a importância dos testes de usabilidade, proporcionando uma visão clara de como esses testes contribuem para o sucesso do projeto.

&emsp;&emsp;A otimização das rotas de leitura de hidrômetros é um desafio complexo que exige uma interface de usuário amigável e eficiente para ser plenamente eficaz. Através dos testes de usabilidade, buscamos garantir que os leituristas e gerentes possam utilizar a solução de maneira intuitiva, sem enfrentar barreiras que comprometam sua produtividade. Além disso, a coleta de feedback direto dos usuários é uma ferramenta poderosa para identificar pontos de melhoria que podem não ser evidentes durante a fase de desenvolvimento.

&emsp;&emsp;Realizar testes de usabilidade nos ajuda a identificar problemas de interface, e também validar se as funcionalidades desenvolvidas realmente atendem às expectativas dos usuários. No contexto deste projeto, é essencial que a solução permita a otimização das rotas de leitura, reduzindo o tempo e a distância percorrida pelos leituristas. Essa eficiência operacional reflete diretamente na redução de custos e na melhoria do serviço prestado aos clientes.

## Objetivos dos Testes de Usabilidade

&emsp;&emsp;Os principais objetivos dos testes de usabilidade são:

1. **Identificar Problemas de Usabilidade**: Detectar dificuldades que os usuários possam encontrar ao utilizar a solução, como interface complexa, funcionalidades confusas ou qualquer outro obstáculo que possa comprometer a eficiência do sistema.

2. **Validar Funcionalidades**: Garantir que as principais funcionalidades, como a otimização de rotas e o registro de anomalias, funcionem conforme o esperado, proporcionando uma experiência de usuário fluida e sem interrupções.

3. **Melhorar a Experiência do Usuário**: Coletar feedback dos usuários para realizar melhorias na interface e nos processos, assegurando que a solução seja fácil de usar e atenda às expectativas dos usuários finais.

4. **Aumentar a Eficiência Operacional**: Assegurar que a solução otimize as rotas de leitura, reduzindo o tempo e a distância percorridos pelos leituristas, contribuindo para uma operação mais eficiente e econômica.

&emsp;&emsp;Realizar testes de usabilidade com um grupo diversificado de usuários permite uma análise mais completa e detalhada das necessidades e dificuldades enfrentadas por diferentes perfis de usuários. Isso nos ajuda a criar uma solução mais inclusiva e acessível, que funcione bem para todos os usuários, independentemente de suas habilidades técnicas ou experiência prévia.

## Metodologia

&emsp;&emsp;Os testes de usabilidade foram conduzidos seguindo uma metodologia estruturada, garantindo a obtenção de resultados relevantes e confiáveis. As etapas incluem:

1. **Seleção de Participantes**: Os participantes dos testes foram cuidadosamente selecionados para representar as personas definidas no projeto. Para que não haja tantos vieses na utilização da solução, nenhum dos testadores é aluno que está desenvolvendo um projeto para resolver este problema da Aegea. Portanto, foram escolhidos 4 alunos do Inteli, sendo 2 alunos de Engenharia da Computação, 1 aluno de Engenharia de Software e 1 aluno de Sistemas da Informação.

2. **Definição das Tarefas**: Foram criadas tarefas específicas que representam as principais funcionalidades da solução, como a geração de rotas otimizadas, a visualização de mapas de rotas e o download dos resultados. As tarefas foram desenhadas para cobrir diferentes aspectos do uso do sistema.

3. **Execução dos Testes**: Os testes foram realizados em sessões individuais, onde cada participante executou as tarefas definidas sob a observação de facilitadores. Durante as sessões, os facilitadores registraram as ações dos usuários, dificuldades encontradas e feedback fornecido.

4. **Registro de Observações**: Todas as observações feitas durante os testes foram documentadas em detalhes, incluindo as reações dos participantes, problemas de usabilidade identificados e sugestões de melhorias. Esta documentação é crucial para a análise subsequente e para a implementação de melhorias.

&emsp;&emsp;Os participantes foram instruídos a executar tarefas reais e relevantes, simulando cenários que eles enfrentariam no dia a dia. Essa abordagem garante que os resultados dos testes de usabilidade sejam aplicáveis e proporcionem insights práticos e úteis para o desenvolvimento da solução. Estas tarefas foram:

| Tarefa | Descrição |
|---|---|
| 1. Planejamento das rotas | Suponha que você é um planejador das rotas de atendimento dos leituristas da Águas do Rio e gostaria de fazer a roteirização de uma amostra de dados e gostaria de uma jornada de 22 dias de trabalho para 50 leituristas. |
| 2. Visualização das rotas no mapa | Suponha que você é um planejador das rotas de atendimento dos leituritas da Águas do Rio e gostaria de consultar o resultado de uma roteirização anterior realizada no dia 07 de junho de 2024 às 13h47m e visualizar a rota no mapa  |
| 3. Download do resultado | Suponha que você é um planejador das rotas de atendimento dos leituritas da Águas do Rio e gostaria de fazer o download do resultado de uma roteirização anterior realizada no dia 07 de junho de 2024 às 13h47m para poder inserir esses dados no sistema dos leituristas  |

## Resultados Obtidos

### Tarefa 01

&emsp;&emsp;Para esta tarefa, somente um dos testadores conseguiu concluí-la sem dificuldade, enquanto os demais não conseguiram. O principal motivo para isso acontecer se deu por:

1. Não haver símbolo de loading para indicar que o carregamento do CSV está sendo feito. (Baixa severidade)

2. Não houve feedback visual para indicar que o algoritmo iniciou/finalizou a execução. (Alta severidade)

3. No primeiro contato do usuário com a tela, houve uma confirmação de que o algoritmo já tinha sido executado, dando a entender que nenhuma outra interação era necessária (Catastrófe).

### Tarefa 02

&emsp;&emsp;Já nesta tarefa, um dos testadores conseguiu concluir com dificuldade, ao mesmo passo que os demais não conseguiram. Esse cenário aconteceu por:

1. A tela de histórico de execução demora bastante para trazer os resultados (aproximadamente 50 segundos), mas nenhum símbolo de carregamento é exibido enquanto isso, o que fez os usuários pensarem que não havia nada no histórico e saírem da tela, quebrando o fluxo de navegação inicialmente pensado (Castastrófe).

### Tarefa 03

&emsp;&emsp;Por fim, em relação a última tarefa, nenhum usuário foi capaz de completá-la. Isso se deu principalmente porque os três usuários que não conseguiram consultar o histórico conforme elucidado na tarefa 2, também não conseguiram aqui. Além disso, o usuáiro que conseguiu passar pelo histórico clicou no botão de download de resultados e nada aconteceu (catástrofe).

### Relatos adicionais

&emsp;&emsp;Outros dois pontos relatados pelos usuários não estavam diretamente relacionados com as tarefas, mas é válido o registro. Estes pontos consistem em:

1. Não existe seta (botão) de voltar entre as páginas. Assim, a navegação é controlada pelo usuário dentro do navegador. (Baixa severidade)

2. Ao clicar nos _cards_ informativos que explicam sobres os dados a serem colocados nos inputs, havia muito texto com pouco espaçamento que causou desconforto na leitura. (Cosmética)

&emsp;&emsp;É possível acessar a tabulação dos testes aqui descritos no arquivo [`assets/Tabulação testes de usabilidade - Aegis - Grupo 4.xlsx`](./assets/Tabulação%20testes%20de%20usabilidade%20-%20Aegis%20-%20Grupo%204.xlsx).

## Melhorias Sugeridas

&emsp;&emsp;Para melhorar a usabilidade da aplicação e resolver os problemas identificados nos testes, algumas medidas podem ser implementadas. As sugestões que destacamos abaixo são baseadas nas heurísticas de Nielsen.

### Tarefa 01

1. **Implementar Símbolo de Carregamento:**
   Adicionar um indicador de carregamento para o upload do CSV, proporcionando ao usuário uma confirmação visual de que a operação está em andamento. Isso está relacionado à heurística de **Visibilidade do Status do Sistema**, que recomenda manter os usuários informados sobre o que está acontecendo.

2. **Feedback Visual do Algoritmo:**
   Incluir uma mensagem ou animação que indique claramente quando o algoritmo está sendo executado e quando foi concluído. Esse feedback visa garantir que os usuários entendam o estado atual da aplicação e evitem conclusões precipitadas sobre a necessidade de interação. Novamente, esta melhoria está ligada à heurística de **Visibilidade do Status do Sistema**.

3. **Revisão da Primeira Tela:**
   Ajustar a primeira tela para evitar a confusão sobre a necessidade de interação adicional. Pode-se incluir uma mensagem de que a execução anterior do algoritmo foi concluída e que o usuário pode iniciar uma nova execução ou visualizar os resultados passados. Esta sugestão está relacionada à heurística de **Correspondência entre o Sistema e o Mundo**, a qual sugere que o sistema deve falar a linguagem do usuário.

### Tarefa 02

1. **Indicador de Carregamento no Histórico:**
   Implementar um símbolo de carregamento para a tela de histórico de execução, informando os usuários que os resultados estão sendo carregados. Isso ajudará a manter os usuários informados sobre o progresso e reduzirá a frustração causada pela espera sem feedback visual, atendendo à heurística de **Visibilidade do Status do Sistema**.

### Tarefa 03

1. **Correção do Botão de Download:**
   Garantir que o botão de download dos resultados funcione corretamente e fornecer feedback imediato ao usuário quando a ação é iniciada e concluída. Isso pode incluir uma mensagem de confirmação ou uma animação que mostre o progresso do download. Esta melhoria se alinha com a heurística de **Visibilidade do Status do Sistema** e **Prevenção de Erros**, que busca informar o usuário sobre ações em andamento e evitar mal-entendidos.

### Relatos Adicionais

1. **Navegação entre Páginas:**
   Adicionar um botão de voltar entre as páginas para facilitar a navegação e evitar que os usuários precisem usar os controles do navegador. Isso melhorará a experiência de navegação e manterá os usuários dentro do fluxo da aplicação, relacionado à heurística de **Controle e Liberdade do Usuário**.

2. **Melhoria na Leitura dos _Cards_ Informativos:**
   Revisar o design dos _cards_ informativos para aumentar o espaçamento entre o texto e melhorar a legibilidade. Um layout mais arejado e visualmente agradável pode reduzir o desconforto e facilitar a compreensão das informações. Esta melhoria está ligada à heurística de **Estética e Design Minimalista**.

## Conclusão

&emsp;&emsp;Os testes de usabilidade são uma parte essencial do desenvolvimento de soluções centradas no usuário. Eles não apenas ajudam a identificar e resolver problemas de usabilidade, mas também garantem que a solução final seja eficiente, intuitiva e alinhada com as necessidades dos usuários. Através desses testes, esperamos que seja possível melhorar a solução, contribuindo para o sucesso do projeto e a satisfação dos usuários finais.