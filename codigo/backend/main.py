"""
Main Application for FastAPI Server

This module sets up the FastAPI server with various routers and middleware.

Modules:
    - uvicorn: ASGI server for serving FastAPI applications.
    - FastAPI: The main FastAPI class.
    - CORSMiddleware: Middleware for handling Cross-Origin Resource Sharing (CORS).
    - csv_router: Router for CSV-related endpoints.
    - cluster_router: Router for clustering-related endpoints.
    - aco_router: Router for Ant Colony Optimization (ACO) endpoints.
    - ortools_router: Router for OR-Tools-related endpoints.
    - results_router: Router for results-related endpoints.

Functions:
    - read_root():
        Root endpoint that returns a welcome message.

Usage:
    To run the application, execute this module directly.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Controllers.CSVController import router as csv_router
from Controllers.ClusteringController import router as cluster_router
from Controllers.ACOController import router as aco_router
from Controllers.ORToolsController import router as ortools_router
from Controllers.ResultsController import router as results_router

app = FastAPI()

# CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for different functionalities
app.include_router(csv_router, tags=["CSV"])
app.include_router(cluster_router, tags=["Clustering"])
app.include_router(aco_router, tags=["Ant Colony Optimization"])
app.include_router(results_router, tags=["Results"])
app.include_router(ortools_router, prefix="/api", tags=["ORTools"])

@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary with a welcome message.
    """
    return {"message": "Hello, Aegis"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)