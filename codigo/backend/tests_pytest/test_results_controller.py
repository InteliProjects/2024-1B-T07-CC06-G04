import pytest # type: ignore
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_history():
    """
    Test the get history endpoint.

    This test sends a GET request to the `/results` endpoint and asserts the 
    following:
    - The response status code is 200 (OK).
    - The response JSON is a list.

    Raises:
        AssertionError: If any of the assertions fail.
    """
    response = client.get("/results")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_results_not_found():
    """
    Test the get results endpoint with a non-existing task ID.

    This test sends a GET request to the `/results/{task_id}` endpoint with a 
    non-existing task ID and asserts the following:
    - The response status code is 404 (Not Found).
    - The response JSON contains a detail message "Results not found."

    Raises:
        AssertionError: If any of the assertions fail.
    """
    task_id = "non_existing_task_id"
    response = client.get(f"/results/{task_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Results not found."
