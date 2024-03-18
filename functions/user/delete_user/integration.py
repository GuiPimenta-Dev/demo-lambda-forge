import pytest
import requests

@pytest.mark.integration(method="DELETE", endpoint="/user/{id}")
def test_delete_user_status_code_is_200():

    response = requests.delete(url="")

    assert response.status_code == 200 
