import numpy as np

class Agent:
    """
    Represents an agent navigating a set of points on a graph.

    Attributes:
        tour (list): A list containing the sequence of points visited by the agent.
        visited (numpy.ndarray): An array marking visited points.
        current_point: The current point where the agent is located.
        reading_time (int): Reading time in minutes.
        speed (int): Walking speed in km/h.
    """

    def __init__(self, num_points, reading_time=2, speed=5):
        """
        Initializes an Agent object.

        Args:
            num_points (int): Number of points in the graph.
            reading_time (int, optional): Reading time in minutes. Defaults to 2.
            speed (int, optional): Walking speed in km/h. Defaults to 5.
        """
        self.tour = []
        self.visited = np.zeros(num_points, dtype=bool)
        self.current_point = None
        self.reading_time = reading_time  # reading time in minutes
        self.speed = speed  # walking speed in km/h

    def visit_point(self, point):
        """
        Marks a point as visited and adds it to the tour.

        Args:
            point (int): The index of the point to be visited.
        """
        self.tour.append(point)
        self.visited[point] = True
        self.current_point = point

    def tour_length(self, graph):
        """
        Calculates the total length of the tour.

        Args:
            graph: The graph containing distance matrix information.

        Returns:
            float: Total length of the tour.
        """
        length = 0
        for i in range(1, len(self.tour)):
            length += graph.distance_matrix[self.tour[i-1]][self.tour[i]]
        length += graph.distance_matrix[self.tour[-1]][self.tour[0]]  # return to the starting point
        return length

    def tour_time(self, graph):
        """
        Calculates the total time taken for the tour.

        Args:
            graph: The graph containing distance matrix information.

        Returns:
            float: Total time taken for the tour.
        """
        time = 0
        for i in range(1, len(self.tour)):
            distance = graph.distance_matrix[self.tour[i-1]][self.tour[i]]
            time += distance / self.speed  # time to traverse the distance
        time += len(self.tour) * (self.reading_time / 60)  # add reading time in hours
        return time
