"""
FastAPI Router for Retrieving Optimization Results

This module provides API endpoints for retrieving the history of all completed tasks and the results of a specific task.

Modules:
    - APIRouter, HTTPException: FastAPI modules for creating routes and handling HTTP exceptions.
    - os, json: Standard Python libraries for operating system dependent functionality and JSON operations.

Functions:
    - get_history():
        Retrieves the history of all completed tasks.
    
    - get_results(task_id: str):
        Retrieves the results of the ACO algorithm for a given task ID.

Variables:
    - router: APIRouter instance to define API routes.
"""

from fastapi import APIRouter, HTTPException
import os
import json

router = APIRouter()

@router.get("/results")
async def get_history():
    """
    Retrieves the history of all completed tasks.

    Returns:
        list: A list of dictionaries, each containing task_id, status, and data.
    """
    history_dir = "./Services/results"
    history = []

    if os.path.exists(history_dir):
        for file_name in os.listdir(history_dir):
            if file_name.endswith(".json"):
                with open(os.path.join(history_dir, file_name), "r") as f:
                    data = json.load(f)
                    history.append({
                        "task_id": file_name.replace(".json", ""),
                        "status": "Completed",
                        "data": data
                    })
    return history

@router.get("/results/{task_id}")
async def get_results(task_id: str):
    """
    Retrieves the results of the ACO algorithm for a given task ID.

    Args:
        task_id (str): Unique identifier for the task.

    Returns:
        dict: A dictionary containing the task_id and the results of the ACO algorithm.

    Raises:
        HTTPException: If the results file is not found.
    """
    results_file = f"./Services/results/{task_id}.json"
    if os.path.exists(results_file):
        with open(results_file, "r") as f:
            results = json.load(f)
        return {"task_id": task_id, "results": results}
    else:
        raise HTTPException(status_code=404, detail="Results not found.")