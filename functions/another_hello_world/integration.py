import pytest
import requests

@pytest.mark.integration(method="GET", endpoint="/another_hello_world")
def test_another_hello_world_status_code_is_200():

    response = requests.get(url="")

    assert response.status_code == 200 
