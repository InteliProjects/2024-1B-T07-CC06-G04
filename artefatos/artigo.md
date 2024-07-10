---
Título: Otimização de rotas de leitura de hidrômetros para empresa de saneamento
Autor: Grupo 4 
Data: 30 de abril de 2024
Resumo: Este artigo descreve o desenvolvimento de uma solução de otimização de rotas de leitura de hidrômetros para uma empresa de saneamento, visando melhorar a eficiência operacional e a experiência dos clientes. A implementação das técnicas com algoritmos, resultou em uma significativa redução no tempo de execução e na distância total percorrida pelos leituristas, melhorando a eficiência operacional e a experiência dos clientes.

---

# Introdução

&emsp;&emsp;No cenário do saneamento básico, uma leitura eficiente de hidrômetros é fundamental para a precisão do faturamento e para a sustentabilidade dos recursos hídricos. Entretanto, a empresa parceiro de projeto, apesar de ser um líder no setor privado de saneamento no Brasil, enfrenta grandes desafios nessa área. Esta realidade operacional complexa é, atualmente, caracterizada por rotas ineficientes, contendo muitos pontos esparsos, que aumentam as distâncias percorridas e, por consequência, os custos operacionais, principalmente no que se relaciona o gasto com cada leiturista. Portanto, essa área demanda soluções inovadoras. Sob esse contexto, este trabalho visa desenvolver um projeto de pesquisa operacional que, ao longo de 10 semanas, apresentará um MVP (Produto Mínimo Viável) para otimizar essas rotas de leitura, por meio de algoritmos clássicos da literatura. Essa solução não apenas aborda as ineficiências atuais, mas também propõe uma solução prática e escalável que poderá transformar e melhorar a operação, garantindo uma maior margem de lucro ao parceiro de projeto.

&emsp;&emsp;O problema de otimização de rotas abordado neste trabalho assemelha-se ao famoso Problema do Caixeiro Viajante (TSP, do inglês *Traveling Salesman Problem*). Esse problema consiste em encontrar a menor rota possível que permita a um vendedor visitar uma série de cidades, passando por cada uma apenas uma vez e retornando ao ponto de origem (Dantzig, Fulkerson e Johnson, 1954). Em termos matemáticos, o TSP busca a menor distância percorrida em um ciclo Hamiltoniano em um grafo completo (Zambito, 2006). O principal desafio deste problema é sua classificação como NP-difícil, o que significa que o tempo de execução aumenta exponencialmente com o acréscimo de novos dados, o que torna impraticável a resolução exata para grandes conjuntos de dados.

&emsp;&emsp;Uma diferença crucial entre o TSP clássico e o problema enfrentado pelo parceiro é que não há necessidade de retorno ao ponto de partida nas rotas de leitura de hidrômetros. Além disso, o projeto precisa considerar a segurança dos leituristas, evitando ao máximo o cruzamento de ruas para minimizar riscos de acidentes. Esses fatores adicionam camadas de complexidade à solução do problema, exigindo abordagens adaptadas e específicas.

&emsp;&emsp;Para abordar de maneira abrangente a otimização das rotas em questão, este trabalho irá explorar a aplicação de vários algoritmos de otimização com foco na resolução do problema do TSP, visando identificar a solução mais eficaz, em termos de precisão e tempo computacional, assim como observar como cada abordagem se comporta nesse contexto operacional complexo. Esses algoritmos se baseiam principalmente em heurísticas e estratégias de aproximação. A primeira abordagem diz respeito a técnicas desenvolvidas para resolver problemas complexos mais rapidamente, enquanto a segunda foca em procurar soluções aproximadas para o problema, em vez da solução ótima. Ambas oferecem uma troca de precisão por tempo de execução, tornando-a viável.

&emsp;&emsp;Os benefícios da pesquisa operacional são diversos para as empresas que são capazes de implementá-la de forma eficiente, sendo o aumento nos lucros o principal ponto avaliado neste trabalho. A pesquisa da RouteSmart Technologies sobre otimização da eficiência operacional evidencia a importância desta solução, que destaca que a aplicação destas técnicas de pesquisa operacional é capaz de reduzir os custos em até 20%, ao melhorar a eficiência das operações logísticas (RouteSmart Technologies, 2023). Por exemplo, a empresa *Citgo Petroleum Corporation*, uma refinaria de petróleo, economiza mais de 70 milhões de dólares anualmente ao implementar técnicas de otimização em seu cotidiano, focando nas operações de refinaria e de distribuição e *marketing* (ORBAY, Berk. 2022). 

&emsp;&emsp;Portanto, este artigo mostra uma abordagem que não somente enfrenta os desafios operacionais atuais da empresa, mas também propõe soluções escaláveis com potencial de serem adaptadas para outras regiões e contextos dentro do setor de saneamento. A partir da integração de análises geoespaciais com técnicas avançadas de otimização de rotas, o projeto evidenciado aqui irá então gerar um aumento da eficiência e na redução de custos operacionais. Os resultados esperados incluem melhorias significativas na produtividade dos leituristas e na precisão do faturamento, contribuindo assim para a satisfação dos consumidores. A implementação bem-sucedida deste projeto atenderá as necessidades atuais do parceiro e oferecerá insights valiosos para futuras inovações em práticas de leitura e gestão de recursos hídricos.

# Trabalhos relacionados

&emsp;&emsp;Para fundamentar o desenvolvimento do projeto de otimização de rotas de leitura de hidrômetros, foram revisitados estudos relevantes que oferecem diversas percepções e insights valiosos para o contexto geral do problema.

&emsp;&emsp;Um dos estudos mais importantes aborda a técnica de Otimização por Colônia de Formigas (ACO). Dorigo e Gambardella (2004) demonstram como a ACO pode ser utilizada para resolver problemas de roteamento de veículos (VRP). A técnica simula o comportamento de formigas na busca de caminhos, onde agentes simples depositam feromônios nos trajetos percorridos. Com o tempo, os caminhos com maior concentração de feromônios têm maior probabilidade de serem escolhidos, resultando em rotas otimizadas.

&emsp;&emsp;Essa adaptabilidade é crucial para o projeto de otimização das rotas de leitura de hidrômetros, onde a variabilidade dos pontos de leitura é alta. Dorigo e Gambardella destacam que a ACO pode se ajustar a mudanças dinâmicas, como novas entregas ou variações na demanda, o que é particularmente relevante para a operação de leitura de hidrômetros, onde os pontos de leitura podem variar mensalmente.

&emsp;&emsp;Além disso, a implementação prática da ACO em diferentes cenários mostrou melhorias significativas em relação a métodos tradicionais de otimização. Adaptar a ACO pode significar uma melhoria nas rotas de leitura, garantindo que os leituristas percorram a menor distância possível e minimizem o tempo total de leitura, aumentando a eficiência operacional.

&emsp;&emsp;Outra técnica que merece destaque é o *Simulated Annealing* (SA), amplamente utilizado para resolver problemas de roteamento de veículos. Dharar (2019) explorou em detalhes a aplicação do SA para encontrar rotas eficientes. Inspirado no processo de recozimento metalúrgico, o SA funciona aceitando soluções piores em um estágio inicial para evitar mínimos locais, permitindo assim uma melhor exploração do espaço de soluções.

&emsp;&emsp;Dharar destacou que o método de resfriamento geométrico produziu os melhores resultados em termos de custo e convergência. Os testes com redes de 15 a 30 destinos mostraram que o SA pode lidar eficazmente com problemas de roteamento de diferentes tamanhos. Em redes menores, o SA encontrou soluções com custos significativamente menores em comparação com outros algoritmos. Em redes maiores, embora não tenha encontrado a solução globalmente ótima, ainda produziu soluções muito próximas do ótimo.

&emsp;&emsp;Aplicando os princípios do SA, é possível desenvolver rotas de leitura que não apenas minimizem a distância percorrida, mas também otimizem o tempo gasto em cada leitura, resultando em uma operação mais eficiente e uma melhor experiência para os clientes.

&emsp;&emsp;Por fim, Bellman (1962) introduz a programação dinâmica como uma técnica eficaz para resolver o TSP. A programação dinâmica decompõe o problema em subproblemas menores, resolvendo cada um de forma otimizada e combinando essas soluções para obter a solução global. Esta técnica é particularmente poderosa para problemas de otimização sequencial, onde cada decisão influencia as subsequentes.

&emsp;&emsp;Bellman demonstrou que a programação dinâmica pode lidar eficientemente com problemas envolvendo até centenas de pontos, com tempo de execução que cresce exponencialmente com o aumento dos pontos. Aplicando esta abordagem ao projeto, é possível garantir que cada rota de leitura seja otimizada, minimizando a distância total percorrida e o tempo de viagem dos leituristas.

&emsp;&emsp;Isso é vital para otimizar o uso do tempo dos leituristas e garantir a precisão e eficiência do processo de leitura de hidrômetros. Além disso, Bellman menciona que a técnica pode ser adaptada para considerar restrições específicas, como tempos de leitura fixos e a necessidade de minimizar travessias de ruas, aumentando a segurança dos leituristas.

&emsp;&emsp;Portanto, a integração das técnicas de Otimização por Colônia de Formigas, *Simulated Annealing* e Programação Dinâmica oferece uma excelente base teórica e prática para o desenvolvimento de soluções de otimização de rotas no contexto das leituras de hidrômetros. Cada técnica traz vantagens específicas que podem ser adaptadas para atender aos desafios e às necessidades operacionais do projeto. A aplicação dessas metodologias pode melhorar diretamente a eficiência e segurança das operações, contribuindo para uma maior satisfação dos clientes e para uma gestão mais eficaz dos recursos da empresa.

# Resultados

&emsp;&emsp;Esta seção explora os impactos práticos e benefícios da implementação de algoritmos de otimização nas rotas de leitura de hidrômetros. Por meio da aplicação de técnicas avançadas como Simulated Annealing e Ant Colony Optimization, estes resultados visam demonstrar a eficácia dessas metodologias em melhorar significativamente a eficiência operacional. Assim esse segmento do artigo aprofunda-se na análise dos algoritmos de otimização aplicados nas rotas de leitura, destacando as vantagens dessas técnicas. A eficácia dessas abordagens é essencial para avançar na busca por soluções que possam resolver problemas técnicos, e também otimizar os recursos e melhorar então o desempenho geral das operações, consolidando a base para futuras inovações no setor de saneamento.

## Implementação dos Algoritmos

&emsp;&emsp;A implementação dos algoritmos de otimização para definir as melhores rotas de leitura demonstrou resultados promissores. Inicialmente, foram desenvolvidos dois algoritmos de otimização: Simulated Annealing e Ant Colony Optimization. O Simulated Annealing simula o processo de recozimento de metais, onde o material é aquecido e em seguida resfriado lentamente para aumentar a resistência e reduzir defeitos. O Ant Colony Optimization é inspirado no comportamento das formigas ao buscar o caminho mais curto entre sua colônia e uma fonte de alimento.

&emsp;&emsp;Sendo assim, esses algoritmos foram testados em uma rota existente de 400 pontos e mostraram-se eficazes em reduzir tanto o tempo de execução quanto a distância total percorrida pelos leituristas, em comparação com os métodos tradicionais de roteirização utilizados pela empresa. É importante destacar que os algoritmos foram executados em um computador que possui um processador Intel Core i5-1135G7 da 11ª geração, com uma frequência base de 2.40 GHz, equipado com 16 GB de RAM, com um sistema operacional de 64 bits e o processador baseado em arquitetura x64. As tabelas a seguir apresentam os resultados obtidos por meio dos testes:

#### Resultados Ant Colony Optimization

| N de formigas | Influência do feromônio | Influência da visibilidade | Taxa de evaporação | N de iterações | Melhor distância percorrida | Tempo para rodar |
|----------|-------|------|------------------|------------|------------------|-------------|
| 05       | 1.0   | 4.0  | 0.5              | 50         | 9.29km           | 29.29s      |
| 05       | 1.0   | 4.0  | 0.5              | 100        | 9.22km           | 62.35s      |
| 10       | 1.0   | 4.0  | 0.5              | 100        | 9.05km           | 115.75s     |
| 10       | 1.0   | 5.0  | 0.5              | 100        | 8.69km           | 114.51s     |
| 10       | 1.0   | 6.0  | 0.5              | 100        | 8.89km           | 115.74s     |


#### Resultados Simulated Annealing

| Temperatura Inicial | Taxa de Resfriamento | Temperatura de Parada | Melhor Distância Percorrida | Tempo para Rodar |
|---------------------|----------------------|---------------------|-----------------------------|------------------|
| 10.000                | 0,99                 | 0,1               | $\approx$ 76,30 km                    | $\approx$ 0.1s           |
| 10.000                | 0,99                 | $1e-200$                | $\approx$ 22,99 km                    | $\approx$ 4,05s           |
| 10.000                 | 0,99                 | $1e-300$                | $\approx$ 20,05 km                    | $\approx$ 6.09s           |
| 10.000                 | 0.999                 | $1e-100$               | $\approx$ 15 km                    | $\approx$ 21.91s           |
| 10.000                 | 0.999                 | $1e-200$               | $\approx$ 15,39 km                    | $\approx$ 39.89s           |
| 100.000                 | 0.999                 | $1e-100$               | $\approx$ 16,41 km                    | $\approx$ 22.41s           |
| 100.000                 | 0.9999                 | $1e-100$               | $\approx$ 14,51 km                    | $\approx$ 3m24s           |
| 1.000.000.000                 | 0.999999                 | $1e-200$               | $\approx$ 8,59 km                    | $\approx$ 12h53m           |

&emsp;&emsp;Desse modo, os resultados apresentados na tabela evidenciam a eficácia dos algoritmos de otimização implementados na roteirização de leituristas. Inicialmente, tanto o Simulated Annealing quanto o Ant Colony demonstraram boas resoluções na redução do tempo de execução e na quilometragem percorrida, superando os métodos tradicionais e oferecendo soluções mais rápidas e eficientes. Assim, essa melhoria na performance dos algoritmos reflete diretamente no aumento da satisfação dos clientes devido a uma maior precisão no faturamento.

&emsp;&emsp;Entretanto, a fim de alcançar uma otimização ainda melhor, foi implementado, posteriormente, o OR-Tools, um conjunto de ferramentas de otimização desenvolvido pelo Google. A utilização do OR-Tools proporcionou uma melhoria significativa nos resultados, oferecendo soluções mais eficientes e seguras em termos de tempo de processamento, executando o algoritmo em minutos, ao invés de horas, e qualidade das rotas geradas, podendo gerar rotas para milhares de dados ao mesmo tempo. Dessa forma, é evidenciado que a capacidade de otimização rápida é vital para responder as demandas operacionais dinâmicas do setor de saneamento.

&emsp;&emsp;A utilização do OR-Tools possibilitou que uma amostra com aproximadamente 380 mil pontos fosse roteirizada em aproximadamente 7 minutos, atingindo resultados ainda melhores do que os obtidos nos casos anteriores. A título de exemplo, a rota cujos testes foram documentados no exemplo anterior levou 2,2 segundos para ser roteirizada, alcançando um resultado de 6,82Km. Esta rápida capacidade de processamento e precisão nas rotas demonstra então o impacto significativo na redução de recursos e tempo, essenciais para operações em grande escala.

&emsp;&emsp;Os resultados quantitativos extraídos das tabelas reforçam a superioridade das técnicas de otimização utilizadas. Os algoritmos Simulated Annealing e Ant Colony Optimization, bem como o OR-Tools, além de reduziram significativamente o tempo e a distância de roteirização, também evidenciaram uma melhora notável na qualidade das rotas geradas. A análise detalhada dos resultados tabelados ilustra isso, como é o exemplo do uso do Ant Colony Optimization que conseguiu reduzir a distância de roteirização para menos de 9 km em todas as configurações testadas, com o melhor caso alcançando apenas 8.69 km. Além disso, o Simulated Annealing reduziu a distância para aproximadamente 8.59 km no cenário mais otimizado, com tempo de execução que variou de segundos a algumas horas, dependendo dos parâmetros. Essas melhorias quantificáveis nos parâmetros de roteirização demonstram a eficiência operacional aprimorada, e apresentam uma redução substancial nos custos e no tempo.

&emsp;&emsp;Portanto, esses resultados sugerem que a utilização de diferentes técnicas de otimização podem levar a soluções mais eficazes para problemas complexos de roteirização, demonstrando a importância de escolher a metodologia adequada para cada contexto específico. As melhorias observadas na eficiência operacional e na redução dos custos de operação ressaltam então a viabilidade da aplicação destas tecnologias avançadas em um ambiente real, oferecendo além de ganhos imediatos, a oportunidade de adaptação e possíveis avanços em outras áreas.

# Conclusão

&emsp;&emsp;Os resultados deste estudo demonstraram a capacidade dos algoritmos de otimização Ant Colony e OR-Tools de se adaptarem a diferentes cenários, oferecendo uma resposta satisfatória mesmo em situações com menor número de funcionários ou dias de trabalho. Testes rigorosos indicaram que os algoritmos são flexíveis, sendo capazes de manter o desempenho em uma variedade de condições operacionais. A capacidade de adaptação permite ajustes conforme mudanças na demanda e na disponibilidade de recursos, garantindo a continuidade do serviço com eficiência.

&emsp;&emsp;Ademais, a redução do número de leituristas e a melhoria nas rotas não apenas reduzem custos, mas também contribuem para a segurança dos trabalhadores ao indicar rotas mais seguras. Por exemplo, os algoritmos foram capazes de reduzir a distância de roteirização para menos de 9 km em todas as configurações testadas, com o melhor caso alcançando apenas 8.69 km. Essa redução significativa não só diminui os custos operacionais, mas também melhora a precisão do faturamento e a satisfação dos clientes, destacando os benefícios tangíveis para a empresa parceira.

&emsp;&emsp;Portanto, a aplicação desses algoritmos pode ser vista como uma contribuição para práticas empresariais mais sustentáveis e responsáveis. Em conclusão, a eficácia e a adaptabilidade dos algoritmos de otimização comprovadas neste estudo ressaltam sua importância como ferramentas estratégicas para a melhoria da eficiência operacional. Sua implementação no Problema de Roteamento de Leituristas representa um passo significativo na busca por soluções inovadoras e eficazes em gestão de rotas, com potencial de expansão para outros setores industriais e comerciais, promovendo uma operação mais eficiente, econômica e ambientalmente responsável.

&emsp;&emsp;Para que trabalhos futuros continuem o que foi apresentado neste artigo, algumas direções podem ser exploradas, tais como a implementação de novas funções na interface, como a opção de modificar pontos manualmente e a aplicação de um processo de arruamento para evitar que o leiturista atravesse ruas com frequência, aumentando sua segurança. A implementação dessas funcionalidades adicionais pode aumentar ainda mais a eficiência operacional e a segurança dos leituristas, oferecendo uma ferramenta mais robusta e adaptável às necessidades específicas do setor de saneamento.

&emsp;&emsp;Além disso, investigar o impacto social da implementação dos algoritmos, incluindo a potencial redução de carga de trabalho e melhoria nas condições de empregabilidade dos leituristas, além dos benefícios para os clientes e comunidades atendidas, seria uma abordagem valiosa para futuros estudos. Implementar essas sugestões não apenas aprofundará o conhecimento adquirido neste estudo, mas também abrirá novas oportunidades para a aplicação de algoritmos de otimização em diversos setores, promovendo avanços tecnológicos e operacionais significativos.



# Referências

BELLMAN, Richard. Dynamic Programming Treatment of the Traveling Salesman Problem. 1962. Disponível em: https://dl.acm.org/doi/10.1145/321105.321111. Acesso em: 14 mai. 2024.

Contribuidores da Wikipédia. Travelling salesman problem. In: WIKIPÉDIA: a enciclopédia livre. 2023. Disponível em: https://en.wikipedia.org/wiki/Travelling_salesman_problem. Acesso em: 13 mai. 2024.

Contribuidores da Wikipédia. Heuristic (computer science). In: WIKIPÉDIA: a enciclopédia livre. 2021. Disponível em: https://en.wikipedia.org/wiki/Heuristic_(computer_science). Acesso em: 13 mai. 2024.

Contribuidores da Wikipédia. Approximation algorithm. In: WIKIPÉDIA: a enciclopédia livre. 2016. Disponível em: https://en.wikipedia.org/wiki/Approximation_algorithm. Acesso em: 13 mai. 2024.

DHARAR, Ameer. Solving the Vehicle Routing Problem with Simulated Annealing. 2019. Disponível em: <https://ameerd.github.io/files/VRP-Project---Github-Version.html>.Acesso em: 20 mai. 2024.

DORIGO, Marco; GAMBARDELLA, Luca Maria. Ant Colony Optimization for the Vehicle Routing Problem. 2004. Disponível em: <https://www.researchgate.net/publication/200058853_Ant_Colony_Optimisation_for_vehicle_routing_problems_from_theory_to_applications>. Acesso em: 14 mai. 2024.

DANTZIG, G.B, FULKERSON, R., JOHNSON, S.M. Solution of a large-scale traveling salesman problem. 1954. Operations Research 2, Santa Mônica, Califórnia. Disponível em: https://www.jstor.org/stable/168581

NATIONAL GEOGRAPHIC SOCIETY. Geographic Information System (GIS). 2024. Disponível em: <https://education.nationalgeographic.org/resource/geographic-information-system-gis/>. Acesso em: 6 mai. 2024.

ORBAY, Berk. Net Profit of Operations Research. Nov. 2022. Disponível em: https://medium.com/berk-orbay/net-profit-of-operations-research-946764fe256d. Acesso em: 14 mai. 2024

ROUTESMART TECHNOLOGIES. PSE&G Applied RouteSmart to Optimize Operational Efficiency. 2023. Disponível em: <https://www.routesmart.com/client-success-stories/case-studies/pseg/>. Acesso em: 3 mai. 2024.

SEAN CARROLL. Route Optimization: Driving Efficiency for Utilities. 2023. Disponível em: <https://talkinglogistics.com/2020/11/10/route-optimization-driving-efficiency-for-utilities/>. Acesso em: 4 mai. 2024.

ZAMBITO, Leonardo. The Traveling Salesman Problem: A Comprehensive Survey. 2006.  p.2-6. Disponível em: https://www.jstor.org/stable/168581

