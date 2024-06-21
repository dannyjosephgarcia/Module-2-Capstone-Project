import logging


class InternalRoutesModel:
    def __init__(self, request):
        self.validate_internal_routes_request(request)
        # TODO: Extract the 'firstName' field from the request and store it as an attribute called 'self.first_name'

    @staticmethod
    def validate_internal_routes_request(request):
        if 'firstName' not in request:
            logging.error('The firstName field is a required field')
            raise ValueError('The firstName field is a required field')
        if not isinstance(request['firstName'], str):
            raise TypeError('The firstName field must be of a string datatype')
