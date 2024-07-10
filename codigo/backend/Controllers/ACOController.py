"""
FastAPI Router for Ant Colony Optimization (ACO) Service

This module provides an API for running Ant Colony Optimization (ACO) tasks and notifying clients via WebSocket.

Modules:
    - APIRouter, HTTPException, BackgroundTasks, WebSocket, WebSocketDisconnect: FastAPI modules for creating routes and handling HTTP and WebSocket communications.
    - ACOService: Service module that implements the ACO algorithm.
    - pandas as pd: Library for data manipulation and analysis.
    - os, json, uuid: Standard Python libraries for file and JSON operations, and generating unique IDs.
    - asyncio: Library to handle asynchronous operations.
    - datetime: Module to handle date and time operations.
    - typing.List: Used for type hinting.

Functions:
    - notify_clients(task_id: str, message: str):
        Sends a message to all active WebSocket connections for the specified task ID.
    
    - run_aco_background(task_id: str, num_ants: int, alpha: float, beta: float, evaporation_rate: float, iterations: int):
        Runs the ACO algorithm in the background, saves the results to a file, and notifies clients upon completion.
    
    - run_aco(num_ants: int, alpha: float, beta: float, evaporation_rate: float, iterations: int, background_tasks: BackgroundTasks):
        API endpoint to start an ACO task and run it in the background.
    
    - websocket_endpoint(websocket: WebSocket, task_id: str):
        WebSocket endpoint for clients to connect and receive updates about a specific ACO task.

Variables:
    - router: APIRouter instance to define API routes.
    - active_connections: Dictionary to keep track of active WebSocket connections for each task ID.
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks, WebSocket, WebSocketDisconnect
from Services.ACOService import ACOService
import pandas as pd
import os
import json
import uuid
import asyncio
from datetime import datetime
from typing import List

router = APIRouter()

# active WebSocket connections
active_connections: dict[str, List[WebSocket]] = {}

async def notify_clients(task_id: str, message: str):
    """
    Sends a message to all active WebSocket connections for the specified task ID.

    Args:
        task_id (str): Unique identifier for the ACO task.
        message (str): Message to be sent to the clients.
    """
    if task_id in active_connections:
        for connection in active_connections[task_id]:
            await connection.send_text(message)

def run_aco_background(task_id: str, num_ants: int, alpha: float, beta: float, evaporation_rate: float, iterations: int):
    """
    Runs the ACO algorithm in the background, saves the results to a file, and notifies clients upon completion.

    Args:
        task_id (str): Unique identifier for the ACO task.
        num_ants (int): Number of ants used in the ACO algorithm.
        alpha (float): Parameter controlling the influence of pheromone trails.
        beta (float): Parameter controlling the influence of heuristic information.
        evaporation_rate (float): Rate at which pheromone trails evaporate.
        iterations (int): Number of iterations to run the ACO algorithm.
    """
    try:
        clustered_file_location = "./Services/clusters/clustered_file.csv"
        clustered_data = pd.read_csv(clustered_file_location)
        results = ACOService.run_aco_on_clusters(clustered_data, num_ants, alpha, beta, evaporation_rate, iterations)
        
        results_dir = "./Services/results"
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        
        results_file = f"{results_dir}/{task_id}.json"
        result_data = {
            "algorithm": "Ant Colony Optimization",
            "parameters": {
                "num_ants": num_ants,
                "alpha": alpha,
                "beta": beta,
                "evaporation_rate": evaporation_rate,
                "iterations": iterations
            },
            "datetime": datetime.now().isoformat(),
            "results": results
        }
        with open(results_file, "w") as f:
            json.dump(result_data, f)
        
        # notify clients about the completion
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(notify_clients(task_id, json.dumps(result_data)))
        loop.close()

        print(f"Results saved to {results_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

@router.post("/run-aco")
async def run_aco(num_ants: int, alpha: float, beta: float, evaporation_rate: float, iterations: int, background_tasks: BackgroundTasks):
    """
    API endpoint to start an ACO task and run it in the background.

    Args:
        num_ants (int): Number of ants used in the ACO algorithm.
        alpha (float): Parameter controlling the influence of pheromone trails.
        beta (float): Parameter controlling the influence of heuristic information.
        evaporation_rate (float): Rate at which pheromone trails evaporate.
        iterations (int): Number of iterations to run the ACO algorithm.
        background_tasks (BackgroundTasks): FastAPI background tasks manager.

    Returns:
        dict: Task ID and message indicating that the optimization has started.
    """
    try:
        task_id = str(uuid.uuid4())  # unique task ID
        background_tasks.add_task(run_aco_background, task_id, num_ants, alpha, beta, evaporation_rate, iterations)
        return {"task_id": task_id, "message": "Optimization started. Check back later for results."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.websocket("/ws/{task_id}")
async def websocket_endpoint(websocket: WebSocket, task_id: str):
    """
    WebSocket endpoint for clients to connect and receive updates about a specific ACO task.

    Args:
        websocket (WebSocket): WebSocket connection instance.
        task_id (str): Unique identifier for the ACO task.
    """
    await websocket.accept()
    if task_id not in active_connections:
        active_connections[task_id] = []
    active_connections[task_id].append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        active_connections[task_id].remove(websocket)
        if not active_connections[task_id]:
            del active_connections[task_id]