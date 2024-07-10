from typing import List, Dict
import numpy as np
import pandas as pd

class Point:
    def __init__(self, index, latitude, longitude):
        """
        Represents a point with an index, latitude, and longitude.

        Args:
            index (int): Index of the point.
            latitude (float): Latitude of the point.
            longitude (float): Longitude of the point.
        """
        self.index = index
        self.latitude = latitude
        self.longitude = longitude

class GraphAntColony:
    def __init__(self, points):
        """
        Initializes a graph for Ant Colony Optimization.

        Args:
            points (List[Point]): List of points to include in the graph.
        """
        self.points = points
        self.num_points = len(points)
        self.distance_matrix = self.build_distance_matrix()
        self.pheromone_matrix = np.ones((self.num_points, self.num_points), dtype=float)
    
    def build_distance_matrix(self):
        """
        Builds the distance matrix for the points using the Haversine formula.

        Returns:
            np.ndarray: A matrix containing distances between each pair of points.
        """
        distances = np.zeros((self.num_points, self.num_points), dtype=float)
        for i in range(self.num_points):
            for j in range(i + 1, self.num_points):
                dist = self.haversine(self.points[i], self.points[j])
                distances[i][j] = dist
                distances[j][i] = dist

        return distances
    
    def haversine(self, point1, point2):
        """
        Calculates the Haversine distance between two points.

        Args:
            point1 (Point): The first point.
            point2 (Point): The second point.

        Returns:
            float: The Haversine distance between the two points.
        """
        R = 6371.0  # Earth radius in kilometers

        lat1, lon1 = np.radians(point1.latitude), np.radians(point1.longitude)
        lat2, lon2 = np.radians(point2.latitude), np.radians(point2.longitude)

        diff_lat = lat2 - lat1
        diff_lon = lon2 - lon1

        a = np.sin(diff_lat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(diff_lon / 2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        distance = R * c

        return distance

    def update_pheromones(self, ants, decay_rate):
        """
        Updates the pheromone levels on the graph based on the tours of the ants.

        Args:
            ants (List[Ant]): List of ants.
            decay_rate (float): The rate at which pheromone evaporates.
        """
        self.pheromone_matrix *= decay_rate

        for ant in ants:
            tour_length = ant.tour_length(self)
            if tour_length > 0:  # Avoid division by zero
                contribution = 1.0 / tour_length
            else:
                contribution = 0  # Handle zero length tours gracefully

            for i in range(1, len(ant.tour)):
                self.pheromone_matrix[ant.tour[i - 1]][ant.tour[i]] += contribution
                self.pheromone_matrix[ant.tour[i]][ant.tour[i - 1]] += contribution

class Ant:
    def __init__(self, num_points):
        """
        Represents an ant in the Ant Colony Optimization algorithm.

        Args:
            num_points (int): Number of points in the graph.
        """
        self.tour = []
        self.visited = np.zeros(num_points, dtype=bool)  # Initializes all points as not visited
        self.current_point = None  # Starting point is not defined yet
    
    def visit_point(self, point):
        """
        Visits a point, updating the tour and visited status.

        Args:
            point (int): Index of the point to visit.
        """
        self.tour.append(point)  # Add point to the tour
        self.visited[point] = True  # Mark this point as visited
        self.current_point = point  # Update the current point

    def tour_length(self, graph):
        """
        Calculates the total length of the ant's tour.

        Args:
            graph (GraphAntColony): The graph on which the ant is traveling.

        Returns:
            float: Total length of the tour.
        """
        length = 0
        # Sum the distances for each consecutive pair of points in the tour
        for i in range(1, len(self.tour)):
            length += graph.distance_matrix[self.tour[i - 1]][self.tour[i]]
        # Add the distance from the last point back to the starting point to complete the tour
        length += graph.distance_matrix[self.tour[-1]][self.tour[0]]  
        return length

class AntColonyOptimization:
    def __init__(self, graph, num_ants, alpha, beta, evaporation_rate, iterations):
        """
        Initializes the Ant Colony Optimization algorithm.

        Args:
            graph (GraphAntColony): The graph on which the algorithm will run.
            num_ants (int): Number of ants in the colony.
            alpha (float): Influence of pheromone on direction.
            beta (float): Influence of distance on direction.
            evaporation_rate (float): Rate at which pheromone evaporates.
            iterations (int): Number of iterations to run the algorithm.
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
        Runs the Ant Colony Optimization algorithm.
        """
        for _ in range(self.iterations):
            self._reset_ants()
            self._construct_tours()
            self._update_pheromones()
            self._update_best_solution()

    def _reset_ants(self):
        """
        Resets the state of each ant to prepare for a new iteration.
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
        Selects the next point for an ant to visit based on pheromone levels and distances.

        Args:
            ant (Ant): The ant for which to select the next point.

        Returns:
            int: The index of the next point to visit.
        """
        probabilities = []
        current_point = ant.current_point

        for i in range(self.graph.num_points):
            if not ant.visited[i]:
                pheromone = self.graph.pheromone_matrix[current_point][i] ** self.alpha
                inverse_distance = (1.0 / self.graph.distance_matrix[current_point][i]) ** self.beta if self.graph.distance_matrix[current_point][i] > 0 else 0
                probabilities.append(pheromone * inverse_distance)
            else:
                probabilities.append(0)
        
        total = sum(probabilities)
        if total > 0:
            probabilities = [p / total for p in probabilities]
        else:
            probabilities = [1 / len(probabilities)] * len(probabilities)

        return np.random.choice(self.graph.num_points, p=probabilities)

    def _update_pheromones(self):
        """
        Updates the pheromone levels on the graph based on the tours of the ants.
        """
        self.graph.update_pheromones(self.ants, self.evaporation_rate)
    
    def _update_best_solution(self):
        """
        Updates the best solution found by the algorithm if a better solution is found.
        """
        for ant in self.ants:
            tour_length = ant.tour_length(self.graph)
            if tour_length < self.best_tour_length:
                self.best_tour_length = tour_length
                self.best_tour = list(ant.tour)

class ACOService:
    @staticmethod
    def run_ant_colony_optimization(points: List[Dict[str, float]], num_ants: int, alpha: float, beta: float, evaporation_rate: float, iterations: int) -> Dict[str, any]:
        """
        Runs the Ant Colony Optimization algorithm on a set of points.

        Args:
            points (List[Dict[str, float]]): List of points with 'INDICE', 'LATITUDE', and 'LONGITUDE' keys.
            num_ants (int): Number of ants in the colony.
            alpha (float): Influence of pheromone on direction.
            beta (float): Influence of distance on direction.
            evaporation_rate (float): Rate at which pheromone evaporates.
            iterations (int): Number of iterations to run the algorithm.

        Returns:
            Dict[str, any]: Dictionary containing the best tour length and the best tour found.
        """
        point_objects = [Point(point['INDICE'], float(point['LATITUDE']), float(point['LONGITUDE'])) for point in points]
        graph = GraphAntColony(point_objects)
        aco = AntColonyOptimization(graph, num_ants, alpha, beta, evaporation_rate, iterations)
        aco.run()
        best_tour_points = [(graph.points[index].latitude, graph.points[index].longitude, graph.points[index].index) for index in aco.best_tour]
        results = {
            "best_tour_length": float(aco.best_tour_length),  # Convert to native Python float
            "best_tour": best_tour_points
        }
        return results

    @staticmethod
    def run_aco_on_clusters(clustered_data: pd.DataFrame, num_ants: int, alpha: float, beta: float, evaporation_rate: float, iterations: int) -> Dict[int, Dict[str, any]]:
        """
        Runs the Ant Colony Optimization algorithm on clustered data.

        Args:
            clustered_data (pd.DataFrame): DataFrame containing clustered data with 'cluster_labels'.
            num_ants (int): Number of ants in the colony.
            alpha (float): Influence of pheromone on direction.
            beta (float): Influence of distance on direction.
            evaporation_rate (float): Rate at which pheromone evaporates.
            iterations (int): Number of iterations to run the algorithm.

        Returns:
            Dict[int, Dict[str, any]]: Dictionary with cluster labels as keys and optimization results as values.
        """
        cluster_results = {}
        for cluster_label in clustered_data['CODIGO_ROTA'].unique():
            cluster_points = clustered_data[clustered_data['CODIGO_ROTA'] == cluster_label].to_dict(orient='records')
            result = ACOService.run_ant_colony_optimization(cluster_points, num_ants, alpha, beta, evaporation_rate, iterations)
            cluster_results[int(cluster_label)] = result  # Ensure cluster_label is a native Python int
        return cluster_results
