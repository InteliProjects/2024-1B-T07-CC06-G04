import math
import pandas as pd
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import json
import os
from datetime import datetime
import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, force=True)


class ORToolsService:
    @staticmethod
    def create_data_model(df_filtered):
        """Stores the data for the problem."""
        data = {}

        # Convert latitude and longitude to a different scale. This happens because OR Tools sensibility with distances.
        df_filtered.loc[:, 'LATITUDE'] = df_filtered['LATITUDE'] * -1000000
        df_filtered.loc[:, 'LONGITUDE'] = df_filtered['LONGITUDE'] * -1000000

        # Create a list of tuples with coordinates (latitude, longitude)
        data["locations"] = list(
            zip(df_filtered['LATITUDE'], df_filtered['LONGITUDE']))

        data["num_vehicles"] = 1
        data["depot"] = 0
        # Add the filtered dataframe to data
        data["df_filtered"] = df_filtered

        return data

    @staticmethod
    def compute_euclidean_distance_matrix(locations):
        """Creates callback to return distance between points."""
        distances = {}
        for from_counter, from_node in enumerate(locations):
            distances[from_counter] = {}
            for to_counter, to_node in enumerate(locations):
                if from_counter == to_counter:
                    distances[from_counter][to_counter] = 0
                else:
                    # Euclidean distance
                    distances[from_counter][to_counter] = int(
                        math.hypot((from_node[0] - to_node[0]),
                                   (from_node[1] - to_node[1]))
                    )
        return distances

    @staticmethod
    def haversine(point1, point2):
        """
        Calculates the Haversine distance between two points.
        """
        R = 6371.0  # Earth radius in kilometers

        lat1, lon1 = np.radians(point1[0]), np.radians(point1[1])
        lat2, lon2 = np.radians(point2[0]), np.radians(point2[1])

        diff_lat = lat2 - lat1
        diff_lon = lon2 - lon1

        a = np.sin(diff_lat / 2)**2 + np.cos(lat1) * \
            np.cos(lat2) * np.sin(diff_lon / 2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        distance = R * c

        return distance

    @staticmethod
    def get_solution_order(manager, routing, solution):
        """Returns the order of the nodes in the solution."""
        index = routing.Start(0)
        order = []
        while not routing.IsEnd(index):
            order.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        order.append(manager.IndexToNode(index))
        return order

    @staticmethod
    def solve_routing_problem(df_filtered):
        """Solves the routing problem."""
        results = {}
        # Instantiate the data problem.
        data = ORToolsService.create_data_model(df_filtered)

        # Create the routing index manager.
        manager = pywrapcp.RoutingIndexManager(
            len(data["locations"]), data["num_vehicles"], data["depot"])

        # Create Routing Model.
        routing = pywrapcp.RoutingModel(manager)

        distance_matrix = ORToolsService.compute_euclidean_distance_matrix(
            data["locations"])

        def distance_callback(from_index, to_index):
            """Returns the distance between the two nodes."""
            # Convert from routing variable Index to distance matrix NodeIndex.
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return distance_matrix[from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(
            distance_callback)

        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        # Print solution on console.
        if solution:
            order = ORToolsService.get_solution_order(
                manager, routing, solution)

            # Reorder the dataframe according to the solution order
            df_reordered = data["df_filtered"].iloc[order]

            # Utilize o valor da coluna "CODIGO_ROTA" da primeira linha como chave
            route_code = str(df_reordered.iloc[0]['CODIGO_ROTA'])

            # Divida as latitudes e longitudes por -1e6 antes de adicionar ao resultado
            df_reordered.loc[:, 'LATITUDE'] = df_reordered['LATITUDE'] / -1e6
            df_reordered.loc[:, 'LONGITUDE'] = df_reordered['LONGITUDE'] / -1e6

            reordered_points = df_reordered[[
                'LATITUDE', 'LONGITUDE']].values.tolist()

            # Calcular a distância Haversine total da rota
            total_distance = 0
            for i in range(len(reordered_points) - 1):
                total_distance += ORToolsService.haversine(
                    reordered_points[i], reordered_points[i + 1])

            # Adicionar a distância Haversine final de volta ao ponto inicial
            total_distance += ORToolsService.haversine(
                reordered_points[-1], reordered_points[0])

            results[route_code] = {
                "best_tour_length": total_distance,
                "best_tour": reordered_points
            }

        return results

    @staticmethod
    def run_optimization(task_id: str):
        """
        Runs the OR-Tools optimization.
        """
        try:
            clustered_file_location = "./Services/clusters/clustered_file.csv"
            df = pd.read_csv(clustered_file_location)
            results = {}
            leiturista = 1
            while True:
                dia = 1
                while True:
                    df_filtered = df[(df['LEITURISTA'] == leiturista)
                                     & (df['DIA'] == dia)]
                    if df_filtered.empty:
                        break
                    logging.info(f"Processing Leiturista: {
                                 leiturista}, Dia: {dia}")  # Using logging
                    route_result = ORToolsService.solve_routing_problem(
                        df_filtered)
                    results.update(route_result)
                    dia += 1
                leiturista += 1
                if df[df['LEITURISTA'] == leiturista].empty:
                    break

            results_dir = "./Services/results"
            if not os.path.exists(results_dir):
                os.makedirs(results_dir)

            results_file = f"{results_dir}/{task_id}.json"
            result_data = {
                "algorithm": "OR-Tools",
                "datetime": datetime.now().isoformat(),
                "results": results
            }
            with open(results_file, "w") as f:
                json.dump(result_data, f)
            logging.info(f"Results saved to {results_file}")  # Using logging
        except Exception as e:
            logging.error(f"Error: {str(e)}")  # Using logging
