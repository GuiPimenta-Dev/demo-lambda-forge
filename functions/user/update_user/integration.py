import pytest
import requests


@pytest.mark.integration(method="PUT", endpoint="/user/{id}")
def test_update_user_status_code_is_200():

    response = requests.put(url="")

    assert response.status_code == 200
