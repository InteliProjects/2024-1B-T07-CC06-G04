"""
FastAPI Router for Clustering CSV Data

This module provides an API endpoint for clustering data from an uploaded CSV file using a specified number of primary and secondary clusters.

Modules:
    - APIRouter, HTTPException: FastAPI modules for creating routes and handling HTTP exceptions.
    - CSVService: Service module for processing CSV files.
    - ClusteringService: Service module for clustering data.
    - os: Standard Python library for operating system dependent functionality.

Functions:
    - cluster_csv(n_clusters_primary: int, n_clusters_secondary: int):
        Clusters the uploaded CSV file data using specified number of primary and secondary clusters.

Variables:
    - router: APIRouter instance to define API routes.
    - CLUSTER_DIRECTORY: Directory path to save clustered data files.
"""

from fastapi import APIRouter, HTTPException
from Services.CSVService import CSVService
from Services.ClusteringService import ClusteringService
import os

router = APIRouter()

CLUSTER_DIRECTORY = "./Services/clusters"

if not os.path.exists(CLUSTER_DIRECTORY):
    os.makedirs(CLUSTER_DIRECTORY)

@router.post("/cluster-csv")
async def cluster_csv(n_clusters_primary: int, n_clusters_secondary: int):
    """
    Clusters the uploaded CSV file data using the specified number of primary and secondary clusters.

    Args:
        n_clusters_primary (int): Number of primary clusters to form.
        n_clusters_secondary (int): Number of secondary clusters to form within each primary cluster.

    Returns:
        dict: A dictionary containing the location of the clustered file.

    Raises:
        HTTPException: If no CSV file has been uploaded yet.
    """
    file_location = "./Services/uploaded_files/uploaded_file.csv"
    if not os.path.exists(file_location):
        raise HTTPException(status_code=400, detail="No CSV file uploaded yet.")

    # Process the uploaded CSV file
    data = await CSVService.process_csv(file_location)
    
    # Perform clustering on the processed data
    clustered_data = ClusteringService.cluster_data(data, n_clusters_primary, n_clusters_secondary)
    
    # Save the clustered data to a new CSV file
    clustered_file_location = f"{CLUSTER_DIRECTORY}/clustered_file.csv"
    clustered_data.to_csv(clustered_file_location, index=False)

    return {"clustered_file_location": clustered_file_location}