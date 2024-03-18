import pytest
import requests


@pytest.mark.integration(method="GET", endpoint="/user/{id}")
def test_get_user_status_code_is_200():

    response = requests.get(url="")

    assert response.status_code == 200
