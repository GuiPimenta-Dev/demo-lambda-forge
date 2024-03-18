import pytest
import requests


@pytest.mark.integration(method="POST", endpoint="/user")
def test_create_user_status_code_is_200():

    response = requests.post(url="")

    assert response.status_code == 200
