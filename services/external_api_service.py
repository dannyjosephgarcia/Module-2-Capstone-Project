class ExternalAPIService:
    def __init__(self, dummyapi_client):
        self.dummyapi_client = dummyapi_client

    def call_external_api(self, name, salary, age, id):
        # TODO: Using the four arguments, construct a request and call the appropriate dummyapi_client method
        #  to receive the HTTP Status Code
        request = None  # <<<======================== YOUR CODE HERE ============================ #
        status_code = self.dummyapi_client.update_database()  # <<<================ YOUR CODE HERE ================= #
        if status_code == 200:
            return {'response': 'Success!'}
        else:
            return {'response': 'Bad response'}
