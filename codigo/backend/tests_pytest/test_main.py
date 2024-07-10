import pytest # type: ignore
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    """
    Test the root endpoint.

    This test sends a GET request to the root endpoint (`/`) and asserts the 
    following:
    - The response status code is 200 (OK).
    - The response JSON contains a message with the text "Hello, Aegis".

    Raises:
        AssertionError: If any of the assertions fail.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Aegis"}
