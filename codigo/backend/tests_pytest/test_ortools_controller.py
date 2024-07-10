import pytest  # type: ignore
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_run_ortools():
    """
    Test the OR-Tools optimization algorithm endpoint.

    This test sends a POST request to the `/run-ortools` endpoint with no parameters
    as the endpoint does not require any. It tests the initiation of the background
    optimization task.

    The test asserts the following:
    - The response status code is 200 (OK).
    - The response JSON contains a `task_id`.
    - The response JSON contains a `message` stating "Optimization started. 
      Check back later for results."

    Raises:
        AssertionError: If any of the assertions fail.
    """
    response = client.post("/api/run-ortools")
    assert response.status_code == 200
    assert "task_id" in response.json()
    assert response.json()[
        "message"] == "Optimization started. Check back later for results."
