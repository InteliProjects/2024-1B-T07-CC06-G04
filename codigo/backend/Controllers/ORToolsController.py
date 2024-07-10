"""
FastAPI Router for OR-Tools Optimization

This module provides an API endpoint for running OR-Tools optimization tasks in the background.

Modules:
    - APIRouter, HTTPException, BackgroundTasks: FastAPI modules for creating routes, handling HTTP exceptions, and managing background tasks.
    - ORToolsService: Service module that implements the OR-Tools optimization.
    - uuid: Standard Python library for generating unique identifiers.

Functions:
    - run_optimization_background(task_id: str):
        Runs the OR-Tools optimization in the background.
    
    - run_ortools(background_tasks: BackgroundTasks):
        Starts the OR-Tools optimization as a background task.

Variables:
    - router: APIRouter instance to define API routes.
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from Services.ORToolsService import ORToolsService
import uuid

router = APIRouter()

def run_optimization_background(task_id: str):
    """
    Runs the OR-Tools optimization in the background.

    Args:
        task_id (str): Unique identifier for the task.
    """
    ORToolsService.run_optimization(task_id)

@router.post("/run-ortools")
async def run_ortools(background_tasks: BackgroundTasks):
    """
    Starts the OR-Tools optimization as a background task.

    Args:
        background_tasks (BackgroundTasks): FastAPI BackgroundTasks instance to manage background tasks.

    Returns:
        dict: A dictionary containing the task_id and a message indicating that the optimization has started.

    Raises:
        HTTPException: If there is an error starting the optimization task.
    """
    try:
        task_id = str(uuid.uuid4())  # unique task ID
        background_tasks.add_task(run_optimization_background, task_id)
        return {"task_id": task_id, "message": "Optimization started. Check back later for results."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
