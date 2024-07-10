"""
FastAPI Router for Uploading CSV Files

This module provides an API endpoint for uploading CSV files and saving them to the server.

Modules:
    - APIRouter, UploadFile, File, HTTPException: FastAPI modules for creating routes, handling file uploads, and managing HTTP exceptions.
    - os: Standard Python library for operating system dependent functionality.

Functions:
    - upload_csv(file: UploadFile = File(...)):
        Uploads a CSV file and saves it to the server.

Variables:
    - router: APIRouter instance to define API routes.
    - UPLOAD_DIRECTORY: Directory path to save uploaded CSV files.
"""

from fastapi import APIRouter, UploadFile, File, HTTPException
import os

router = APIRouter()

UPLOAD_DIRECTORY = "./Services/uploaded_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    """
    Uploads a CSV file and saves it to the server.

    Args:
        file (UploadFile): The uploaded CSV file.

    Returns:
        dict: A dictionary containing the location of the uploaded file.

    Raises:
        HTTPException: If the uploaded file is not a CSV.
    """
    if file.filename.endswith(".csv"):
        file_location = f"{UPLOAD_DIRECTORY}/uploaded_file.csv"
        
        # Save the uploaded CSV file to the specified location
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        return {"file_location": file_location}
    else:
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")