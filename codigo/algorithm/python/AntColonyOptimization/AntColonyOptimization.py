from .Ant import Ant
import numpy as np

class AntColonyOptimization:
    """
    Implements the Ant Colony Optimization algorithm for finding the shortest path in a graph.

    Attributes:
        graph (Graph): The graph on which ants will travel.
        num_ants (int): The number of ant agents used in the algorithm.
        ants (list): A list of Ant objects used for exploring the graph.
        alpha (float): The influence factor of pheromone in probability calculation.
        beta (float): The influence factor of distance in probability calculation.
        evaporation_rate (float): The rate at which pheromone decays.
        iterations (int): The number of iterations the algorithm will run.
        best_tour (list): The best tour found by any ant.
        best_tour_length (float): The length of the best tour.
    """

    def __init__(self, graph, num_ants, alpha, beta, evaporation_rate, iterations):
        """
        Initializes a new instance of AntColonyOptimization with the specified parameters.

        Parameters:
            graph (Graph): The graph on which ants will travel.
            num_ants (int): The number of ants to use in the algorithm.
            alpha (float): The exponent to which pheromone influence is raised.
            beta (float): The exponent to which inverse distance influence is raised.
            evaporation_rate (float): The rate at which pheromones evaporate after each iteration.
            iterations (int): The total number of iterations the algorithm will perform.
        """
        self.graph = graph
        self.num_ants = num_ants
        self.ants = [Ant(graph.num_points) for _ in range(num_ants)]
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.iterations = iterations
        self.best_tour = None
        self.best_tour_length = np.inf
    
    def run(self):
        """
        Executes the ant colony optimization algorithm over a set number of iterations.
        """
        for _ in range(self.iterations):
            self._reset_ants()
            self._construct_tours()
            self._update_pheromones()
            self._update_best_solution()

    def _reset_ants(self):
        """
        Resets all ants to start a new tour from a random starting point.
        """
        for ant in self.ants:
            start_point = np.random.randint(self.graph.num_points)
            ant.tour = [start_point]
            ant.visited = np.zeros(self.graph.num_points, dtype=bool)
            ant.visited[start_point] = True
            ant.current_point = start_point
    
    def _construct_tours(self):
        """
        Constructs a complete tour for each ant in the colony by selecting the next point based on pheromone levels and distances.
        """
        for ant in self.ants:
            for _ in range(1, self.graph.num_points):
                next_point = self._select_next_point(ant)
                ant.visit_point(next_point)

    def _select_next_point(self, ant):
        """
        Selects the next point for an ant to visit based on a probabilistic decision rule influenced by pheromone levels and distances.

        Parameters:
            ant (Ant): The ant for which to select the next point.

        Returns:
            int: The index of the next point to be visited.
        """
        probabilities = []
        current_point = ant.current_point

        for i in range(self.graph.num_points):
            if not ant.visited[i]:
                if self.graph.distance_matrix[current_point][i] == 0:
                    pheromone = 0
                    inverse_distance = 0
                else:
                    pheromone = self.graph.pheromone_matrix[current_point][i] ** self.alpha
                    inverse_distance = (1.0 / self.graph.distance_matrix[current_point][i]) ** self.beta

                probabilities.append(pheromone * inverse_distance)
            else:
                probabilities.append(0)
        
        total = sum(probabilities)
        if total > 0:
            probabilities = [p / total for p in probabilities]
        else:
            probabilities = [1 / len(probabilities)] * len(probabilities)  # uniform distribution if all probabilities are zero

        return np.random.choice(self.graph.num_points, p=probabilities)

    def _update_pheromones(self):
        """
        Updates the pheromone levels on the graph based on the tours completed by the ants and the evaporation rate.
        """
        self.graph.update_pheromones(self.ants, self.evaporation_rate)
    
    def _update_best_solution(self):
        """
        Updates the best known solution if a better tour is found during the current iteration.
        """
        for ant in self.ants:
            tour_length = ant.tour_length(self.graph)
            if tour_length < self.best_tour_length:
                self.best_tour_length = tour_length
                self.best_tour = list(ant.tour)
