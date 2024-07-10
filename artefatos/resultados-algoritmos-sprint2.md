# Resultados dos algoritmos implementados na sprint 2

&emsp;&emsp;Este documento inclui um resumo sobre os resultados obtidos na sprint 02 deste projeto, na qual foram implementados três algoritmos de otimização meta-heurística: Ant Colony Optimization, Simulated Annealing e Firefly Algorithm. Para melhor entender estes resultados, principalmente aqueles que se referem a velocidade de execução do algoritmo, é necessário entender que os códigos foram executados em um computador que possui um processador Intel Core i5-1135G7 da 11ª geração, com uma frequência base de 2.40 GHz, equipado com 16 GB de RAM, com um sistema é operacional de 64 bits e o processador baseado em arquitetura x64.

## Ant Colony Optimization

### Explicação conceitual do algoritmo

&emsp;&emsp;O _Ant Colony Optimization Algorithm_ é um algoritmo de busca local inspirado no comportamento das formigas ao buscar o caminho mais curto entre sua colônia e uma fonte de alimento. Um aspecto notável das formigas é que, individualmente, não possuem muitas informações sobre o ambiente ao redor, mas coletivamente conseguem encontrar o caminho mais eficiente por meio da colaboração indireta, tal processo é simulado na otimização. Tal colaboração ocorre mediante um feromônio que as formigas depositam no chão enquanto se movem.

&emsp;&emsp; Supondo duas formigas saindo de sua colônia, uma passa por um caminho mais curto A e a outra por um mais longo B para chegar até uma fonte de comida. A formiga A vai chegar muito mais rápido na fonte de comida depositando seu feromônio por todo o caminho de ida e volta, enquanto a formiga B vai levar muito mais tempo para ir e voltar para a colônia. Com isso, os feromônios da formiga B ficarão em menor concentração, já que com o tempo essa substância evapora, deixando o caminho da formiga A mais atrativo para toda a colônia.

&emsp;&emsp;O _Ant Colony Optimization Algorithm_ usa do mesmo princípio para resolver problemas de otimização. Primeiro, "formigas artificiais" (agentes simulados) exploram o espaço de soluções de um problema depositando rastros de "feromônio artificial", assim via várias iterações, a matriz de feromônios é atualizada mediante uma taxa de reposição e evaporação, enquanto o processo de decisão de qual caminho a formiga irá é feito de forma probabilística baseado na quantidade de feromônio e na "visibilidade" dos caminhos próximos.

&emsp;&emsp;A _ACO_ é uma poderosa estratégia de busca local, além de muito flexível. Além de suas aplicações em problemas de roteirização, tal técnica também pode ser aplicada em outras áreas como otimização de redes e de recursos.

### Aplicação no projeto

&emsp;&emsp;O _Ant Colony Optimization Algorithm_ foi aplicado no projeto em questão através do desenvolvimento de uma série de _Abstract Data Types_ para facilitar a compreensão e aplicação do código. Para isso, no diretório `./codigo/algorithm/python/utils` os _TADs_ `Graph.py`, `Point.py` e `MapPlotter.py`, classes gerais que podem ser utilizadas para outros algoritmos. Ademais, foram implementadas classes específicas para a otimização da colônia de formigas no diretório `./codigo/algorithm/python/AntColonyOptimization` com os _TADs_ `Ant.py`, `AntColonyOptmization.py`, `GraphAntColony.py` e o `main.py` aonde o algoritmo é implementado.

&emsp;&emsp;`Graph.py` e `Point.py` são duas classes utilizadas para organizar a estrutura de dados para o funcionamento dos algoritmos, tal necessidade foi percebida devido à característica geoespacial do problema a ser resolvido. A classe `Ant.py` representa as "formigas artificiais" necessárias para o funcionamento da busca local da otimização. A classe `GraphAntColony.py` herda os principais métodos de `Graph.py` e implementa um método de atualização da matriz de "feromônios artificiais". A classe `AntColonyOptimization.py` é efetivamente a implementação do algoritmo usando todos os _TADs_ apresentados. `MapPlotter.py` é uma classe auxiliar para facilitar a plotagem dos mapas usados para visualização das rotas otimizadas.

### Resultados

&emsp;&emsp;O algoritmo foi implementado usando a rota **72_203** como base, ou seja, uma base de 400 pontos para realização de testes e comparação com outros algoritmos de otimização. Segue uma tabela com resultados de testes realizados com diferentes parâmetros. "N de formigas" diz respeito ao número de agentes na otimização, "Influência do feromônio" e "Influência da visibilidade" dizem respeito ao quanto esses dois fatores impactam nas probabilidades de escolha de caminho de cada agente, a matriz de feromônios é atualizada a cada iteração, enquanto visibilidade depende da distância entre cada ponto. A "Taxa de evaporação" está diretamente relacionada com o quanto que os valores dos feromônios irão diminuir ao passar das iterações, "N de iterações" corresponde a quantas vezes a otimização irá rodar antes de parar, enquanto "Melhor distância percorrida" e "Tempo para rodar" são métricas de avaliação da qualidade e eficiência dos algoritmos.

| N de formigas | Influência do feromônio | Influência da visibilidade | Taxa de evaporação | N de iterações | Melhor distância percorrida | Tempo para rodar |
|----------|-------|------|------------------|------------|------------------|-------------|
| 05       | 1.0   | 4.0  | 0.5              | 50         | 9.29km           | 29.29s      |
| 05       | 1.0   | 4.0  | 0.5              | 100        | 9.22km           | 62.35s      |
| 10       | 1.0   | 4.0  | 0.5              | 100        | 9.05km           | 115.75s     |
| 10       | 1.0   | 5.0  | 0.5              | 100        | 8.69km           | 114.51s     |
| 10       | 1.0   | 6.0  | 0.5              | 100        | 8.89km           | 115.74s     |

## Simulated Annealing

### Explicação conceitual do algoritmo

&emsp;&emsp;O Simulated Annealing (em português, recozimento simulado) é um algoritmo de otimização que simula o processo de recozimento de metais, no qual o material é aquecido e em seguida resfriado lentamente para aumentar a resistência e reduzir defeitos. Essa abordagem é usada para encontrar uma solução aproximada para problemas de otimização global, especialmente aqueles que podem ter muitos mínimos locais.

&emsp;&emsp;Inicialmente, o algoritmo escolhe uma solução aleatória no espaço de soluções e uma "temperatura" inicial elevada. A cada iteração, uma nova solução é gerada a partir da atual por um processo de perturbação aleatória. Se essa nova solução for melhor, ela é aceita. Caso contrário, ainda pode ser aceita com uma probabilidade que depende da diferença entre as soluções e da temperatura atual. Essa probabilidade diminui à medida que a temperatura é gradualmente reduzida, o que ajuda a explorar amplamente o espaço de soluções no início e refinar a busca conforme a temperatura cai. Essa abordagem permite que o algoritmo escape de mínimos locais em busca de um mínimo global mais satisfatório, tornando-o eficaz para problemas complexos e não convexos.

### Aplicação no projeto
&emsp;&emsp;Neste projeto, o Simulated Annealing foi integrado utilizando algumas classes e estruturas de dados. Os códigos estão organizados no diretório `./codigo/algorithm/python/SimulatedAnnealing`, incluindo a classe SimulatedAnnealign que faz a execução do algoritmo da maneira que foi descrita anteriormente. Essa classe ainda faz uso de outras estruturas que estão disponíveis em `./codigo/algorithm/python/utils`.

### Resultados

&emsp;&emsp;Assim como no algoritmo anterior, a rota utilizada como base foi a **72_203** como base. Abaixo é possível conferir uma tabela com os resultados obtidos a partir de diferentes parâmetros.

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

## Lazy Algorithm

### Explicação e Aplicação no projeto

&emsp;&emsp;Com intuito de modelar com maior facilidade as especificidades do projeto, foi desenvolvido um _lazy algorithm_ que basicamente apenas faz uma busca sequencial através dos pontos do grafo. Tal algoritmo não apresenta resultados muito precisos em questão de distância nem em clusterização. Sua implementação por conta da facilidade de customizar um algoritmo mais simples para conter características específicas para o projeto em questão, assim facilitando a implementação de tais _features_ em algoritmos mais complexos. Suas principais características são a aplicação da lógica de tempo de trabalho para cada agente que realiza a busca e o uso de múltiplos agentes em rotas distintas com uma velocidade média de deslocamento e tempo de leitura entre cada vértice do grafo em exploração.

### Resultados

&emsp;&emsp;O _Lazy Algorithm_ não apresenta muitos resultados em sua primeira aplicação dado que ele foi desenvolvido apenas para ser uma base para futuros desenvolvimentos mais específicos de outros algoritmos voltados para os detalhes da modelagem do parceiro.

## Firefly Algorithm
&emsp;&emsp;O algoritmo *Firefly* é uma metaheurística inspirada no comportamento de vaga-lumes que foi proposta para resolver problemas de otimização (JATI, Gilang Kusuma; MANURUNG, Ruli; Suyanto, 2013). Nesse contexto, é utilizado para computar um problema semelhante ao Problema do Caixeiro Viajante (TSP - *Traveling Salesman Problem*) e, por isso, é utilizado esse problema como base para o projeto. No contexto do TSP, o objetivo é encontrar a rota mais curta que visita todas as cidades exatamente uma vez e retorna à cidade de origem. A principal diferença, em relação às necessidades do projeto, é a restrição de retornar ao primeiro ponto, o qual não é requisitado pelo parceiro.

&emsp;&emsp;O funcionamento do algoritmo é baseado na interação entre vaga-lumes. São utilizadas algumas métricas arbitrárias, como distância e brilho, que ditam a atuação do programa. A cada iteração, um certo vagalume é atraído por outro com um brilho maior, ou seja, uma solução mais otimizada. Após isso, toma um certa quantidade de passos, que retratam a troca de alguns dos caminhos distintos com o vagalume mais próximo, a fim de tentar alcançar um resultado melhor. Em suma, ele segue as seguintes etapas:

&emsp;&emsp;1. Inicialização: Comece com uma população de soluções (possíveis rotas) aleatórias.

&emsp;&emsp;2. Avaliação: Avalie a aptidão de cada solução usando uma função objetivo, que no caso do TSP seria minimizar a distância total percorrida na rota.

&emsp;&emsp;3. Ordenação: Ordene as soluções com base na sua aptidão, da melhor para a pior.

&emsp;&emsp;4. Atualização: Atualize cada solução seguindo o movimento dos vaga-lumes, onde os mais brilhantes atraem aqueles que estão próximos a eles. Isso é feito ajustando as soluções para se moverem em direção às soluções mais brilhantes na vizinhança.

&emsp;&emsp;5. Exploração: Introduza uma aleatoriedade no movimento dos vagalumes para explorar novas regiões do espaço de busca.

&emsp;&emsp;6. Critério de parada: Repita os passos 3 a 5 até que um critério de parada seja atendido (por exemplo, número máximo de iterações ou tempo limite).

&emsp;&emsp;O algoritmo *Firefly* é iterativo e pode convergir para uma solução próxima do ótimo global. No entanto, como qualquer metaheurística, não garante a obtenção da solução ótima, mas pode encontrar soluções de alta qualidade em um tempo razoável. A qualidade do resultado depende das métricas estabelecidas. Quanto mais iterações definidas, melhor o resultado tenderá a ser. Entretanto, haverá um custo operacional maior e, por consequência, um maior tempo de execução. Assim, torna-se necessário encontrar um equilíbrio entre a qualidade do resultado retornado e o tempo necessário para executar o código.

&emsp;&emsp;Em relação à sua implementação, foi utilizada a linguagem de programação Java para fazê-la. Entretanto, até o momento dessa escrita, o seu funcionamento não foi consolidado, ainda apresentando alguns erros de código. Logo, serão feitas as correções necessárias para que seja executado corretamente, assim como uma rodagem robusta de testes.

### Referências
JATI, Gilang Kusuma; MANURUNG, Ruli; Suyanto. Discrete Firefly Algorithm for Traveling Salesman Problem: A New Movement Scheme. 2013. p. x-x.
SUBOTIC, Milos; MISIC, Ivan; TUBA, Milan. An Object-Oriented Implementation of the Firefly Algorithm for Continuous Unconstrained Optimization Problems. 2012.