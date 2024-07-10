import numpy as np

class GraphAntColony:
    """
    Represents a graph of points with distances calculated using the Haversine formula.

    Attributes:
        points (list): A list of Point objects representing the vertices of the graph.
        num_points (int): The number of points in the graph.
        distance_matrix (numpy.ndarray): A 2D array where each entry (i, j) is the distance between points i and j.
        pheromone_matrix (numpy.ndarray): A 2D array initialized to one, representing the pheromone level on each edge.
    """

    def __init__(self, points):
        """
        Initializes a new Graph instance, calculates the distance matrix using the Haversine formula, 
        and initializes the pheromone matrix.

        Parameters:
            points (list): A list of Point objects that are the vertices of the graph.
        """
        self.points = points
        self.num_points = len(points)
        self.distance_matrix = self.build_distance_matrix()
        self.pheromone_matrix = np.ones((self.num_points, self.num_points), dtype=float)
    
    def build_distance_matrix(self):
        """
        Constructs the distance matrix for the graph using the Haversine formula to calculate distances.

        Returns:
            numpy.ndarray: A symmetric 2D array with distances between each pair of points in the graph.
        """
        distances = np.zeros((self.num_points, self.num_points), dtype=float)
        for i in range(self.num_points):
            for j in range(i+1, self.num_points):
                dist = self.haversine(self.points[i], self.points[j])
                distances[i][j] = dist
                distances[j][i] = dist

        return distances
    
    def haversine(self, point1, point2):
        """
        Calculates the great-circle distance between two points on the Earth's surface specified by latitude and longitude
        using the Haversine formula.

        Parameters:
            point1 (Point): The first point with latitude and longitude.
            point2 (Point): The second point with latitude and longitude.

        Returns:
            float: The distance between the two points in kilometers.
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
        Updates the pheromone levels on all edges based on the tours completed by a list of ants and a given decay rate.
        The method applies the decay to the current pheromone matrix and then adds new pheromone based on the quality of
        each ant's tour.

        Parameters:
            ants (list): A list of Ant objects that have completed tours and calculated their respective tour lengths.
            decay_rate (float): The rate at which the current pheromone level decays, typically a value between 0 and 1.

        Effects:
            Modifies the pheromone_matrix attribute by decaying its current values and then adding new pheromone based
            on the inverses of the tour lengths of the ants.
        """
        # Apply decay to all pheromones
        self.pheromone_matrix *= decay_rate

        # Add pheromone based on each ant's tour contribution
        for ant in ants:
            contribution = 1.0 / ant.tour_length(self)  # Calculate the contribution of the ant based on its tour length
            for i in range(1, len(ant.tour)):
                self.pheromone_matrix[ant.tour[i-1]][ant.tour[i]] += contribution
                self.pheromone_matrix[ant.tour[i]][ant.tour[i-1]] += contribution  # Ensure the matrix remains symmetric
