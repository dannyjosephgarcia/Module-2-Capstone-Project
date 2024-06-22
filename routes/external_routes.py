from flask import Blueprint, jsonify, request
from container import Container
from dependency_injector.wiring import Provide, inject
from models.external_routes_model import ExternalRoutesModel

# TODO: Provide the correct arguments to the Blueprint class (there should be two of them)
external_routes_blueprint = Blueprint()  # <<<================================ YOUR CODE HERE ======================== #


@external_routes_blueprint.route('/call_external_api', methods=['PUT'])
@inject
# TODO: Finish the route below by:
#  1. Injecting the ExternalAPIRoute Service
#  2. Parsing the request with the ExternalRoutesModel object
#  3. Leveraging the injected class to receive the required information
#  4. Send back a JSON serialized response
def call_external_routes_api():  # <<<================================ YOUR CODE HERE ======================== #
    external_routes_model = None  # <<<========================== YOUR CODE HERE ============================= #
    response = None  # <<<====== YOUR CODE HERE ====================== #
    return 200  # <<<====== YOUR CODE HERE ====================== #
