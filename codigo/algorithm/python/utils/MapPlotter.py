import folium
import numpy as np

class MapPlotter:
    """
    Represents a map plotter for visualizing a tour of points on a geographical map using the Folium library.

    Attributes:
        graph_points (list): A list of Point objects representing the nodes of a graph.
        best_tour (list): A list of indices representing the best path through the points.
        map_name (str): The filename for the saved HTML map visualization.
    """

    def __init__(self, graph_points, best_tour, map_name):
        """
        Initializes a new MapPlotter instance.

        Parameters:
            graph_points (list): A list of Point objects that represent the nodes of the graph.
            best_tour (list): A list of indices denoting the order of the best tour found.
            map_name (str): The name of the file to which the map will be saved, without the extension.
        """
        self.graph_points = graph_points
        self.best_tour = best_tour
        self.map_name = map_name

    def plot_map(self):
        """
        Plots and saves a map showing the best tour among the points.
        The map centers around the geographic center of the tour. It marks each point in the tour,
        connects consecutive points with lines, and saves the map as an HTML file.

        The tour path is highlighted, and the return path (to start the point) is distinguished by a different color.
        """
        # Calculate the geographic center of the tour
        center_lat = np.mean([self.graph_points[idx].latitude for idx in self.best_tour])
        center_lon = np.mean([self.graph_points[idx].longitude for idx in self.best_tour])
        map = folium.Map(location=[center_lat, center_lon], zoom_start=13)

        # Add circle markers for each point in the tour
        for idx in self.best_tour:
            point = self.graph_points[idx]
            folium.CircleMarker(
                [point.latitude, point.longitude],
                popup=f'Point {point.index}',
                radius=5,
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.7
            ).add_to(map)

        # Draw lines between consecutive points in the tour
        for i in range(len(self.best_tour) - 1):
            start_point = self.graph_points[self.best_tour[i]]
            end_point = self.graph_points[self.best_tour[i + 1]]
            folium.PolyLine(
                locations=[
                    [start_point.latitude, start_point.longitude],
                    [end_point.latitude, end_point.longitude]
                ],
                color='blue'
            ).add_to(map)

        # Connect the last point back to the first to close the tour
        start_point = self.graph_points[self.best_tour[-1]]
        end_point = self.graph_points[self.best_tour[0]]
        folium.PolyLine(
            locations=[
                [start_point.latitude, start_point.longitude],
                [end_point.latitude, end_point.longitude]
            ],
            color='red',  # Use a different color to indicate the return path
            popup='Return Path'
        ).add_to(map)

        # Save the map to an HTML file
        map.save(f'./codigo/algorithm/python/miscellaneous/{self.map_name}.html')