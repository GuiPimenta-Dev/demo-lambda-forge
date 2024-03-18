import pytest
import requests

@pytest.mark.integration(method="POST", endpoint="/docs")
def test_swagger_status_code_is_200():

    response = requests.post(url="")

    assert response.status_code == 200 
