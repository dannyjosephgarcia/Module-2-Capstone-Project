import unittest
from app import app

HAPPY_REQUEST = {'firstName': 'ADAM'}
MISSING_FIELD = {'blabla': '123'}
WRONG_TYPE = {'firstName': 123}

INTERNAL_ROUTES_URL = 'http://127.0.0.1/internal_routes'


class TestInternalRoutes(unittest.TestCase):
    def test_internal_routes_happy_path(self):
        response = app.test_client().get(INTERNAL_ROUTES_URL, json=HAPPY_REQUEST)
        self.assertEqual(200, response.status_code)

    # TODO: Complete the following test cases to ensure that a 500 is received for the bad requests up above
    def test_internal_routes_missing_field(self):
        pass

    def test_internal_routes_wrong_type(self):
        pass


if __name__ == "__main__":
    unittest.main()
