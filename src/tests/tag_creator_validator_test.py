from src.errors.error_types.http_unprocessable_entity_error import HttpUnprocessableEntityError
from src.validators.tag_creator_validator import tag_creator_validator


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


def test_tag_creator_validator():
    request = MockRequest({
        "product_code": "123"
    })
    tag_creator_validator(request)


def test_tag_creator_validator_with_error():
    request = MockRequest(json={"product_code1": 1234})

    try:
        tag_creator_validator(request)
        assert False
    except Exception as exception:
        assert isinstance(exception, dict)
