import pytest
import requests


# @pytest.mark.integration(method="GET", endpoint="/private")
def test_private_status_code_is_200():

    response = requests.get(url="")

    assert response.status_code == 200
