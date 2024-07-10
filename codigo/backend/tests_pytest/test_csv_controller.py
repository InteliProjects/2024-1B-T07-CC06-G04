import os
import shutil
import pytest # type: ignore
import asyncio
from fastapi.testclient import TestClient
from backend.main import app
from backend.Services.CSVService import CSVService

client = TestClient(app)

# Get the absolute path of the test directory
current_dir = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope="module")
def clean_services_folder():
    """
    Fixture to clean up the Services folder after tests.
    """
    yield
    services_folder = os.path.join(current_dir, "..", "..", "Services", "uploaded_files")
    if os.path.exists(services_folder):
        shutil.rmtree(services_folder)

@pytest.mark.asyncio
async def test_upload_csv(clean_services_folder):
    """
    Test the CSV upload endpoint with a valid CSV file.
    """
    file_path = os.path.join(current_dir, "test_files", "arquivo_mockado.csv")
    with open(file_path, "rb") as file:
        response = client.post("/upload-csv", files={"file": ("test_file.csv", file, "text/csv")})
    
    assert response.status_code == 200
    assert "file_location" in response.json()
    file_location = response.json()["file_location"]
    
    # Verify the file content was processed correctly
    processed_data = await CSVService.process_csv(file_location)
    assert processed_data is not None
    assert isinstance(processed_data, list)
    assert len(processed_data) > 0

@pytest.mark.asyncio
async def test_upload_csv_invalid_format(clean_services_folder):
    """
    Test the CSV upload endpoint with an invalid file format.
    """
    file_path = os.path.join(current_dir, "test_files", "actually_this_is_not_a_csv.txt")
    with open(file_path, "rb") as file:
        response = client.post("/upload-csv", files={"file": ("test_file.txt", file, "text/plain")})
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid file format. Please upload a CSV file."