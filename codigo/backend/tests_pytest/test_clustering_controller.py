import os
import shutil
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.Services.CSVService import CSVService

client = TestClient(app)

# get the absolute path of the test directory
current_dir = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope="module")
def setup_environment():
    """
    Fixture to set up the environment before tests and clean up after tests.
    """

    upload_directory = os.path.join(current_dir, "..", "Services", "uploaded_files")
    cluster_directory = os.path.join(current_dir, "..", "Services", "clusters")
    
    os.makedirs(upload_directory, exist_ok=True)
    os.makedirs(cluster_directory, exist_ok=True)

    # clean up after tests
    yield
    if os.path.exists(upload_directory):
        shutil.rmtree(upload_directory)
    if os.path.exists(cluster_directory):
        shutil.rmtree(cluster_directory)

@pytest.mark.asyncio
async def test_cluster_csv_no_file_uploaded(setup_environment):
    """
    Test the cluster CSV endpoint without any file uploaded.
    """
    response = client.post("/cluster-csv?n_clusters_primary=10&n_clusters_secondary=22")
    assert response.status_code == 400
    assert response.json()["detail"] == "No CSV file uploaded yet."

@pytest.mark.asyncio
async def test_cluster_csv_valid_file(setup_environment):
    """
    Test the cluster CSV endpoint with a valid CSV file and parameters.
    """
    # upload a CSV file first
    file_path = os.path.join(current_dir, "test_files", "arquivo_mockado.csv")
    with open(file_path, "rb") as file:
        upload_response = client.post("/upload-csv", files={"file": ("test_file.csv", file, "text/csv")})
    assert upload_response.status_code == 200

    # cluster the uploaded CSV file
    response = client.post("/cluster-csv?n_clusters_primary=5&n_clusters_secondary=2")
    assert response.status_code == 200
    assert "clustered_file_location" in response.json()
    
    clustered_file_location = response.json()["clustered_file_location"]
    assert os.path.exists(clustered_file_location)
    
    clustered_data = await CSVService.process_csv(clustered_file_location)
    assert clustered_data is not None
    assert isinstance(clustered_data, list)
    assert len(clustered_data) > 0

@pytest.mark.asyncio
async def test_upload_csv(setup_environment):
    """
    Test the CSV upload endpoint with a valid CSV file.
    """
    file_path = os.path.join(current_dir, "test_files", "arquivo_mockado.csv")
    with open(file_path, "rb") as file:
        response = client.post("/upload-csv", files={"file": ("test_file.csv", file, "text/csv")})
    
    assert response.status_code == 200
    assert "file_location" in response.json()
    file_location = response.json()["file_location"]
    
    # verify the file content was processed correctly
    processed_data = await CSVService.process_csv(file_location)
    assert processed_data is not None
    assert isinstance(processed_data, list)
    assert len(processed_data) > 0
