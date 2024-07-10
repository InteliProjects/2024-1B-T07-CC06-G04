# Complexidade e corretude dos algoritmos

## 1. Introdução à Complexidade e Sua Importância

&emsp;&emsp;A complexidade de um algoritmo está relacionada à quantidade de recursos computacionais que ele consome à medida que o tamanho da entrada aumenta. Esses recursos são geralmente categorizados em duas principais formas: o tempo (complexidade temporal) e a memória (complexidade espacial). A complexidade pode ser expressa através da notação $Big$ $O$, uma representação matemática que descreve o limite superior do crescimento de um algoritmo, permitindo prever seu comportamento nos piores cenários possíveis.

&emsp;&emsp;A análise de complexidade é uma ferramenta fundamental na ciência da computação, já que permite comparar diferentes algoritmos de forma objetiva. Isso é essencial para otimizar o desempenho de programas e garantir que as aplicações possam escalar eficientemente à medida que lidam com volumes maiores de dados.

&emsp;&emsp;Por exemplo, um algoritmo com complexidade $O(n)$ terá um desempenho que cresce linearmente em relação ao tamanho da entrada, enquanto um algoritmo com complexidade $O(n^2)$ terá um desempenho que cresce quadraticamente, tornando-se muito menos eficiente com grandes volumes de dados.

&emsp;&emsp;Compreender a complexidade dos algoritmos é crucial para cientistas da computação, pois decisões bem-informadas sobre qual algoritmo utilizar podem levar a melhorias consideráveis no desempenho e na eficiência dos sistemas computacionais.

## 2. _Ant Colony Optimization_

### 2.1. Introdução ao algoritmo

&emsp;&emsp;O Algoritmo de Otimização por Colônia de Formigas _(ACO - Ant Colony Optimization)_ é uma técnica inspirada no comportamento das formigas reais na busca de alimentos. Desenvolvido por Marco Dorigo nos anos 90, o ACO pertence à categoria de algoritmos de otimização baseados em populações, e é amplamente utilizado para resolver problemas complexos de otimização combinatória, como o Problema do Caixeiro Viajante _(TSP - Traveling Salesman Problem)_ e o Problema de Roteamento de Veículos _(VRP - Vehicle Routing Problem)_.

&emsp;&emsp;O ACO imita o processo natural das formigas que depositam uma substância química chamada feromônio em seus caminhos enquanto procuram por comida. Outras formigas são atraídas por essas trilhas de feromônio, seguindo-as e reforçando-as se encontrarem comida no final do caminho. Com o tempo, as trilhas com maior concentração de feromônio indicam os caminhos mais curtos ou eficientes.

&emsp;&emsp;No contexto computacional, o ACO funciona da seguinte forma:

1. **Inicialização:** Um número de formigas virtuais é colocado aleatoriamente no grafo que representa o problema a ser resolvido.  
2. **Construção da Solução:** Cada formiga constrói uma solução (um caminho) passo a passo, selecionando o próximo nó (ou cidade, no caso do TSP) com base em uma probabilidade que depende da quantidade de feromônio presente na aresta e da heurística do problema (por exemplo, a distância no TSP).
3. **Atualização do Feromônio:** Após todas as formigas terem construído suas soluções, as trilhas de feromônio são atualizadas. Trilhas que foram percorridas por soluções de alta qualidade recebem um incremento maior de feromônio, enquanto todas as trilhas sofrem uma evaporação de feromônio para evitar convergência prematura.
4. **Iteração:** O processo se repete por várias iterações até que um critério de parada seja alcançado (por exemplo, um número fixo de iterações ou uma melhoria insignificante na solução).

### 2.2. Análise Matemática da Complexidade

&emsp;&emsp;A análise de complexidade envolve considerar as principais operações realizadas pelo algoritmo em cada etapa (May et al., [2021?]).

#### 2.2.1. Complexidade de tempo

1. **Inicialização:**
   - **Construção da matriz de distâncias e de feromônios:** $O(n²)$. Tanto o array de distâncias quanto o de feromônio são bidimensionais, com um tamanho que depende do número de cidades $n$.

2. **Execução Principal:**
   - Para cada iteração ($i$ iterações):
     - Reinicialização das formigas: $O(m)$, onde $m$ é o número de formigas.
     - Construção das soluções:
       - Para cada formiga ($m$ formigas):
         - Seleção do próximo ponto: $O(n)$ operações para calcular as probabilidades.
         - Total para todas as formigas: $O(m \cdot n)$.
     - Atualização de feromônios: $O(m \cdot n²)$ no pior caso, considerando a atualização da matriz de feromônios.
     - Ademais, por tratar-se de uma meta-heurística, a complexidade de tempo teórica também deve levarem consideração uma taxa na qual as soluções encontradas se estabilizam em um mínimo local ou global (caso encontre o global), sendo essa uma taxa $w$ que depende dos parâmetros inseridos para o algoritmo (número de formigas, influência da visibilidade, influência dos feromônios). Não é possível afirmar com precisão o valor dessa taxa $w$ uma vez que os valores dos parâmetros para o _Ant Colony_ são definidos de forma empírica, dado o fator não determinístico do algoritmo.

&emsp;&emsp;Portanto, a complexidade total de tempo é:

$$
O(i \cdot w \cdot m \cdot n^2)
$$

#### 2.2.2. Complexidade de espaço

1. **Matriz de Distâncias:** $O(n^2)$ - A matriz de distâncias é sempre bidimensional e depende do número $n$ de pontos a serem visitados.
2. **Matriz de Feromônios:** $O(n^2)$ - A matriz de feromônios é sempre bidimensional e depende do número $n$ de pontos a serem visitados.
3. **Inicialização da colônia de formigas:** $O(m \cdot n)$ - Cada formiga possui sua própria lista para armazenar o conjunto de caminhos que seguirá no decorrer das iterações, assim resultando em uma complexidade de espaço que depende do número de formigas vezes o número de pontos a serem visitados.

&emsp;&emsp;Portanto, a complexidade de espaço é: 

$$
O(n^2 + n^2 + m \cdot n) = O(n^2 + m \cdot n)
$$

### 2.3. Análise do melhor e do pior caso

#### 2.3.1. Melhor caso

&emsp;&emsp;No melhor caso, considera-se um cenário ideal onde o algoritmo converge rapidamente para uma solução ótima. Isso pode ocorrer quando as trilhas de feromônio se ajustam rapidamente, e as formigas encontram a melhor solução em poucas iterações.

1. **Inicialização:**
   - Construção da matriz de distâncias: $O(n^2)$, onde $n$ é o número de pontos.

2. **Execução Principal:**
   - Para cada iteração ($i$ iterações):
     - Reinicialização das formigas: $O(m)$, onde $m$ é o número de formigas.
     - Construção das soluções:
       - Para cada formiga ($m$ formigas):
         - Seleção do próximo ponto: $O(n)$ operações para calcular as probabilidades.
         - Total para todas as formigas: $O(m \cdot n)$.
     - Atualização de feromônios: $O(m \cdot n^2)$ no pior caso, considerando a atualização da matriz de feromônios.

&emsp;&emsp;Assumindo que a convergência rápida ocorre em um número constante de iterações ($i$ é constante) e que houve uma rápida convergência para um mínimo local ou global ($w$ é constante), a complexidade de tempo no melhor caso é:

$$
O(m \cdot n^2)
$$

#### 2.3.2. Pior caso

&emsp;&emsp;No pior caso, considera-se que o algoritmo leva o máximo de iterações permitidas para convergir para uma solução. Isso pode ocorrer devido a uma escolha desfavorável dos parâmetros do algoritmo ou um problema com uma configuração difícil.

1. **Inicialização:**
   - Construção da matriz de distâncias: $O(n^2)$, onde $n$ é o número de pontos.

2. **Execução Principal:**
   - Para cada iteração ($i$ iterações):
     - Reinicialização das formigas: $O(m)$, onde $m$ é o número de formigas.
     - Construção das soluções:
       - Para cada formiga ($m$ formigas):
         - Seleção do próximo ponto: $O(n)$ operações para calcular as probabilidades.
         - Total para todas as formigas: $O(m \cdot n)$.
     - Atualização de feromônios: $O(m \cdot n^2)$ no pior caso, considerando a atualização da matriz de feromônios.

&emsp;&emsp;Assumindo que o algoritmo leva o número máximo de iterações permitidas $i$, a complexidade de tempo no pior caso é:

$$
O(i \cdot w \cdot m \cdot n^2)
$$

### 2.4. Invariante do laço principal do algoritmo

**Invariante:** Após $k$ iterações, a matriz de feromônios reflete as experiências acumuladas pelas formigas, incorporando informações sobre as soluções exploradas até o momento.

**Justificativa:** A cada iteração, as formigas constroem novas soluções e atualizam os feromônios com base na qualidade dessas soluções. A evaporação dos feromônios permite que o algoritmo evite a estagnação prematura, incentivando a exploração de novas soluções.

### 2.5. Demonstração formal da corretudo do algoritmo

&emsp;&emsp;Para provar a corretude do algoritmo, podemos usar a indução com base no invariante:

1. **Base $(k = 0)$:** Inicialmente, a matriz de feromônios é homogênea, refletindo a ausência de qualquer informação sobre soluções específicas.

2. **Passo indutivo:** Suponha que após $k$ iterações, o invariante é verdadeiro. Durante a iteração $k+1$:
   - As formigas constroem novas soluções com base nos feromônios existentes.
   - As soluções encontradas pelas formigas são usadas para atualizar a matriz de feromônios. Trilhas que contribuem para melhores soluções são reforçadas, enquanto todas as trilhas sofrem evaporação.
   - A matriz de feromônios é atualizada para refletir essas novas experiências, mantendo a invariante.

&emsp;&emsp;Portanto, por indução, o invariante se mantém verdadeiro para todas as iterações.

&emsp;&emsp;Pode-se expressar essa invariante de forma matemática através da expressão:

$$
\forall (i, j), \tau_{ij}^{(k)} \geq 0
$$

&emsp;&emsp;Nessa expressão, $\tau_{ij}^{(k)}$ representa o nível de feromônio na aresta entre os nós $i$ e $j$ após $k$ iterações.

&emsp;&emsp;Para expressar a atualização da matriz de feromônios pode-se usar a expressão:

$$
\tau_{ij}^{(k+1)} = (1 - \rho) \cdot \tau_{ij}^{(k)} + \Delta \tau_{ij}^{(k+1)}
$$

Na qual:

$\rho \rightarrow$ corresponde á taxa de evaporação do feromônio.  

$\Delta \tau_{ij}^{(k+1)} \rightarrow$ é a quantidade de feromônio depositada na aresta $(i, j)$ pela colônia de formigas na iteração $k + 1$

## 3. _OR Tools_

## 3.1. Introdução

&emsp;&emsp;O OR-Tools não é exatamente um algoritmo, mas sim um conjunto de bibliotecas de software de código aberto desenvolvido pela Google projetado para resolver problemas de otimização combinatória, como roteirização de veículos, planejamento de produção, agendamento e problemas de satisfatibilidade. Ele fornece algoritmos eficientes para otimização linear, programação inteira, e otimização de restrições, facilitando a implementação de soluções complexas de otimização nas linguagens Python, C++, Java e .NET. Assim, este grupo optou por incluir essa ferramenta no projeto para que fosse possível entregar ao cliente uma solução que ofereça uma melhor rapidez e robustez na solução, haja vista que este conjunto de código já recebeu a mais alta premiação na em uma competição de programação para empresas em todos os anos desde 2013 (Google, 2024).

### 3.2. Análise Matemática da Complexidade

&emsp;&emsp;Nesta análise, consideraremos o algoritmo que é executado pela biblioteca, que consiste na _Guided Local Search_ (em português, busca local guiada). Um algoritmo de busca local começa com uma solução arbitrária e termina com um mínimo local no qual nenhuma melhoria extra é possível de ser encontrada (Voudouris e Tsang, 1998). Já a busca logal guiada têm raízes em uma arquitetura de rede neural (Wang e Tsang, 1991) e sua principal diferença consiste em adicionar termos de penalidade à função de custo original do problema, de tal forma que seja possível direcionar a busca local para regiões promissoras do espaço de busca. Cada vez que a busca local atinge um mínimo local, as penalidades são ajustadas, e a busca é reiniciada para minimizar a função de custo modificada.

&emsp;&emsp;Determinar a complexidade computacional, principalmente considerando que o código não foi produzido por este grupo não é exatamente uma tarefa trivial, mas é fato que um procedimento de busca local depende do tamanho da vizinhança e também do tempo necessário para avaliar um movimento. Em geral, quanto maior a vizinhança, mais tempo é necessário para explorá-la e melhores são os mínimos locais (Voudouris e Tsang, 1998).

#### 3.2.1. Complexidade de tempo

&emsp;&emsp;Para determinar a complexidade de tempo de um algoritmo de busca local guiada, é necessário entender a complexidade de tempo das partes menores que compõem esse algoritmo. Estas podem ser elencadas em:

- **a) Avaliar função de custo**: Considerando o problema do caixeiro viajante, avaliar o custo do percurso é $O(n)$, onde $n$ é o número de cidades.

- **b) Busca local**: Essa fase consiste em, de maneira iterativa, melhorar a solução a cada execução do algoritmo. Para o caixeiro viajante, uma heurística comum de busca local é a 2-opt, a qual tem uma complexidade de tempo no pior caso de $O(n^2)$ por iteração.

- **c) Penalidade**: A complexidade de atualizar penalidades e controlar o processo de busca é geralmente O(n) (assumindo que as penalidades são atualizadas em uma varredura linear dos componentes da solução).

&emsp;&emsp;Portanto, considerando que o itens a) e b) ocorrem uma vez a cada iteração a complexidade de tempo para o algoritmo implementado utilizando o OR Tools pode ser definida como:

$$
\boxed{O(k \cdot n^2 + 2n)}
$$

&emsp;&emsp;Donde $k$ é o número de iterações do algoritmo e $n$ o número de cidades. Contudo, para um $n$ relativamente grande, podemos resumir a complexidade para

$$
\boxed{O(k \cdot n^2)}
$$

#### 3.2.2. Complexidade de espaço

&emsp;&emsp;A complexidade de espaço é analisada considerando a memória necessária para armazenar diferentes componentes do algoritmo. Para isso, avaliamos os seguintes tópicos:

- **a) Estado Atual e Melhor Solução Encontrada**: O GLS precisa armazenar a solução corrente e a melhor solução encontrada até o momento. Considerando _n_ pontos, isso requer $O(n) espaço.

- **b) Penalidades e Estruturas de Custo**: O algoritmo mantém uma estrutura de dados para armazenar as penalidades associadas aos elementos da solução. No caso do caixeira viajante, isso envolve armazenar penalidades para cada aresta entre cidades, resultando em um espaço $O(n^2)$.

&emsp;&emsp;Logo, combinando esses fatores, a complexidade de espaço da busca loca guiada, considerando um número $n$ de cidades é de:

$$
\boxed{O(n^2)}
$$

## Referências

GOOGLE. Google OR-Tools. Disponível em: <https://developers.google.com/optimization?hl=pt-br>. Acesso em: 9 jun. 2024.

MAY, B. et al.. Ant Colony Optimization: An Advanced Approach to the Traveling Salesman Problem. Disponível em: <https://cap.stanford.edu/profiles/cwmd?fid=301672&cwmId=10839>. Acesso em: 05 jun. 2024.

VOUDOURIS, C., TSANG, E. Guided local search and its application to the traveling salesman problem. In: European Journal of Operational Research, v. 113, n. 2, p. 469-499, 1999.

WANG, C. J., TSANG, E. Solving constraint satisfaction problems using neural-networks. In: Proceedings of IEE Second International Conference on Artificial Neural Networks, 1991, p. 295-299.