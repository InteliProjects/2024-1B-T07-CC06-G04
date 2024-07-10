import numpy as np

class Ant:
    """
    Represents an ant used in the Ant Colony Optimization algorithm, capable of traversing a graph by visiting points
    and calculating the length of the tour made.

    Attributes:
        tour (list): A list that stores the indices of points visited by the ant in the order they were visited.
        visited (numpy.ndarray): A boolean array where each element indicates whether the corresponding point has been visited.
        current_point (int or None): The index of the current point where the ant is located, or None if not yet started.
    """

    def __init__(self, num_points):
        """
        Initializes a new instance of the Ant class.

        Parameters:
            num_points (int): The number of points in the graph that the ant will explore.
        """
        self.tour = []
        self.visited = np.zeros(num_points, dtype=bool)  # Initializes all points as not visited
        self.current_point = None  # Starting point is not defined yet
    
    def visit_point(self, point):
        """
        Records the visit of an ant to a particular point, marking it as visited and updating the current location.

        Parameters:
            point (int): The index of the point being visited.
        """
        self.tour.append(point)  # Add point to the tour
        self.visited[point] = True  # Mark this point as visited
        self.current_point = point  # Update the current point

    def tour_length(self, graph):
        """
        Calculates the total length of the ant's current tour based on the distances between consecutively visited points,
        including the return trip to the starting point.

        Parameters:
            graph (Graph): The graph on which the ant is traveling, providing a distance matrix.

        Returns:
            float: The total length of the tour.
        """
        length = 0
        # Sum the distances for each consecutive pair of points in the tour
        for i in range(1, len(self.tour)):
            length += graph.distance_matrix[self.tour[i-1]][self.tour[i]]
        # Add the distance from the last point back to the starting point to complete the tour
        length += graph.distance_matrix[self.tour[-1]][self.tour[0]]  
        return length
