"""
Clustering Service for Geographical Points

This module provides a service for clustering geographical points using a two-stage MiniBatch K-Means algorithm. It optimizes cluster sizes and assigns route codes to the clustered data.

Modules:
    - List, Dict: Typing modules for type hinting.
    - pandas as pd, numpy as np: Data manipulation libraries.
    - MiniBatchKMeans: Clustering algorithm from sklearn.
    - distance_matrix: Function from scipy.spatial to compute distance matrices.

Classes:
    - ClusteringService:
        Provides static methods for clustering data.

Functions:
    - cluster_data(points: List[Dict[str, float]], n_clusters_primary: int = 350, n_clusters_secondary: int = 22) -> pd.DataFrame:
        Clusters geographical points using a two-stage MiniBatch K-Means algorithm, optimizes cluster sizes, and assigns route codes.
"""

from typing import List, Dict
import pandas as pd
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from scipy.spatial import distance_matrix

class ClusteringService:
    @staticmethod
    def cluster_data(points: List[Dict[str, float]], n_clusters_primary: int = 350, n_clusters_secondary: int = 22) -> pd.DataFrame:
        """
        Clusters geographical points using a two-stage MiniBatch K-Means algorithm, optimizes cluster sizes, and assigns route codes.

        Args:
            points (List[Dict[str, float]]): List of points, each represented as a dictionary with 'LATITUDE' and 'LONGITUDE' keys.
            n_clusters_primary (int): Number of primary clusters to form. Default is 350.
            n_clusters_secondary (int): Number of secondary clusters to form within each primary cluster. Default is 22.

        Returns:
            pd.DataFrame: DataFrame containing the original points and their assigned primary and secondary cluster labels and route codes.
        """
        # Convert the list of points to a DataFrame
        df = pd.DataFrame(points)

        # Cleaning database
        df = df[["INDICE", "LATITUDE", "LONGITUDE", "LOGRADOURO", "NUMERO"]]
        
        # Ensure LATITUDE and LONGITUDE are numeric
        df['LATITUDE'] = pd.to_numeric(df['LATITUDE'], errors='coerce')
        df['LONGITUDE'] = pd.to_numeric(df['LONGITUDE'], errors='coerce')

        # Drop rows with NaN values in LATITUDE or LONGITUDE
        df.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
        
        # Perform primary clustering
        primary_kmeans = MiniBatchKMeans(n_clusters=n_clusters_primary, random_state=8081)
        df['LEITURISTA'] = primary_kmeans.fit_predict(df[['LATITUDE', 'LONGITUDE']])
        
        # Initialize secondary cluster labels and route codes
        df['DIA'] = -1
        df['CODIGO_ROTA'] = -1
        
        # Perform secondary clustering within each primary cluster
        route_code_counter = 0
        for LEITURISTA in range(n_clusters_primary):
            subcluster_data = df[df['LEITURISTA'] == LEITURISTA]
            if len(subcluster_data) >= n_clusters_secondary:
                secondary_kmeans = MiniBatchKMeans(n_clusters=n_clusters_secondary, random_state=8081)
                df.loc[subcluster_data.index, 'DIA'] = secondary_kmeans.fit_predict(subcluster_data[['LATITUDE', 'LONGITUDE']])
            else:
                df.loc[subcluster_data.index, 'DIA'] = np.arange(len(subcluster_data))
            
            # Assign route codes
            for DIA in range(n_clusters_secondary):
                route_indices = df[(df['LEITURISTA'] == LEITURISTA) & (df['DIA'] == DIA)].index
                df.loc[route_indices, 'CODIGO_ROTA'] = route_code_counter
                route_code_counter += 1

        # Optimize clusters with less than 300 points
        for LEITURISTA in range(n_clusters_primary):
            subcluster_data = df[df['LEITURISTA'] == LEITURISTA]
            rotas_menor_300 = subcluster_data['CODIGO_ROTA'].value_counts()[subcluster_data['CODIGO_ROTA'].value_counts() < 300].index
            menor_300_centroides = subcluster_data[subcluster_data['CODIGO_ROTA'].isin(rotas_menor_300)].groupby('CODIGO_ROTA')[['LATITUDE', 'LONGITUDE']].mean().reset_index()
            
            if len(menor_300_centroides) > 1:
                dist_matrix = distance_matrix(menor_300_centroides[['LATITUDE', 'LONGITUDE']], menor_300_centroides[['LATITUDE', 'LONGITUDE']])
                np.fill_diagonal(dist_matrix, np.inf)  # Avoid self-distance
                
                for i in range(len(menor_300_centroides)):
                    nearest_neighbor_idx = np.argmin(dist_matrix[i])
                    rota_atual = menor_300_centroides.iloc[i]['CODIGO_ROTA']
                    rota_vizinha = menor_300_centroides.iloc[nearest_neighbor_idx]['CODIGO_ROTA']
                    
                    soma_pontos = (subcluster_data['CODIGO_ROTA'].value_counts()[rota_atual] + 
                                   subcluster_data['CODIGO_ROTA'].value_counts()[rota_vizinha])
                    
                    if soma_pontos <= 500:
                        df.loc[df['CODIGO_ROTA'] == rota_vizinha, 'CODIGO_ROTA'] = rota_atual
                        dist_matrix[:, nearest_neighbor_idx] = np.inf
                        dist_matrix[nearest_neighbor_idx, :] = np.inf

        # Recalculate centroids after merging clusters
        centroides = df.groupby('CODIGO_ROTA')[['LATITUDE', 'LONGITUDE']].mean().reset_index()

        return df