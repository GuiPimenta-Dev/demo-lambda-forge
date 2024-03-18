from .main import lambda_handler


def test_authorizer_should_pass_with_correct_secret():

    event = {
        "headers": {"secret": "xEh0z8JfgLR1XFzKNP1K27kTk7tJejWLJx0VN0J6MgHsYomj1NV7"}
    }
    response = lambda_handler(event, None)

    assert response == {
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {"Action": "execute-api:Invoke", "Effect": "allow", "Resource": "*"}
            ],
        },
    }


def test_authorizer_should_fail_with_invalid_secret():

    event = {"headers": {"secret": "INVALID-SECRET"}}
    response = lambda_handler(event, None)

    assert response == {
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {"Action": "execute-api:Invoke", "Effect": "deny", "Resource": "*"}
            ],
        },
    }
