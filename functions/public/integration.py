import pytest
import requests


@pytest.mark.integration(method="GET", endpoint="/public")
def test_public_status_code_is_200():

    response = requests.get(
        url="https://t5rwrwgucd.execute-api.us-east-2.amazonaws.com/dev/public"
    )

    assert response.status_code == 200
