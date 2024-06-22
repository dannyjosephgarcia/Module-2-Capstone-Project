import unittest
from app import app
from unittest.mock import patch
from clients.dummyapi_client import DummyAPIClient

HAPPY_REQUEST = {
    "name": "test",
    "salary": "123",
    "age": "23",
    "id": 21
}
MISSING_FIELD = {
    "name": "test",
    "salary": "123",
    "age": "23"
}
WRONG_DATATYPE = {
    "name": 123,
    "salary": "123",
    "age": "23",
    "id": 21
}

# TODO: Create a class called TestExternalRoutes that tests the following functionality:
#  1. A good request returns a 200 AND the response is what we expect
#  2. A missing field returns a 500
#  3. A wrong datatype returns a 500
#  4. Mock a 500 from the DummyAPIClient's 'update_database' route to receive a bad response result


if __name__ == "__main__":
    unittest.main()
