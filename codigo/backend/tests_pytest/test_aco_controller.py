import pytest # type: ignore
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_run_aco():
    """
    Test the ACO (Ant Colony Optimization) algorithm endpoint.

    This test sends a POST request to the `/run-aco` endpoint with minimal 
    parameters to avoid overwhelming the test environment. The parameters 
    include `num_ants`, `alpha`, `beta`, `evaporation_rate`, and `iterations`.

    The test asserts the following:
    - The response status code is 200 (OK).
    - The response JSON contains a `task_id`.
    - The response JSON contains a `message` stating "Optimization started. 
      Check back later for results."

    Raises:
        AssertionError: If any of the assertions fail.
    """
    response = client.post("/run-aco", params={
        "num_ants": 1,
        "alpha": 1.0,
        "beta": 1.0,
        "evaporation_rate": 0.5,
        "iterations": 1
    })
    assert response.status_code == 200
    assert "task_id" in response.json()
    assert response.json()["message"] == "Optimization started. Check back later for results."
