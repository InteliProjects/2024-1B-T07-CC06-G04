import random
import math


class SimulatedAnnealing:
    """
    Implements the Simulated Annealing algorithm to find an approximate solution
    to the traveling salesman problem.

    Attributes:
        graph (object): An object containing the data of the problem, including the distance matrix and the points.
    """

    def __init__(self, graph):
        """
        Initializes the SimulatedAnnealing with a specific graph.

        Args:
            graph (object): The graph on which the annealing process will be performed. This graph should contain a distance matrix attribute, the points, and, obviously a number of points attribute.
        """
        self.graph = graph

    def route_cost(self, route):
        """
        Calculates the total cost of a given route.

        Args:
            route (list): A list of indices representing the route of travel.

        Returns:
            int: The total cost of the route.
        """
        return sum(self.graph.distance_matrix[route[i], route[i+1]] for i in range(len(route) - 1)) + \
            self.graph.distance_matrix[route[-1], route[0]]

    def swap(self, route):
        """
        Performs a random swap of two cities in the route.

        Args:
            route (list): A list of city indices representing the current route.

        Returns:
            list: The new route after the swap.
        """
        a, b = random.sample(range(len(route)), 2)
        route[a], route[b] = route[b], route[a]
        return route

    def run(self, initial_temp, cooling_rate, stopping_temp):
        """
        Executes the Simulated Annealing algorithm to find the optimal route.

        Args:
            initial_temp (float): The initial temperature for the annealing process.
            cooling_rate (float): The rate at which the temperature will decrease.
            stopping_temp (float): The temperature at which the annealing process stops.

        Returns:
            tuple: A tuple containing the best route found and its cost.
        """
        num_points = self.graph.num_points
        current_solution = list(range(num_points))
        random.shuffle(current_solution)
        current_cost = self.route_cost(current_solution)
        best_solution = current_solution[:]
        best_cost = current_cost
        temperature = initial_temp

        while temperature > stopping_temp:
            new_solution = self.swap(current_solution[:])
            new_cost = self.route_cost(new_solution)
            delta_cost = new_cost - current_cost

            # Accepts the new solution if the cost is lower or with a probability depending on the cost and temperature
            if delta_cost < 0 or random.random() < math.exp(-delta_cost / temperature):
                current_solution = new_solution
                current_cost = new_cost

                # If the new cost is lower than the best cost found, updates the best solution
                if current_cost < best_cost:
                    best_solution = current_solution
                    best_cost = current_cost

            temperature *= cooling_rate

        return best_solution, best_cost
