from container import Container
from dependency_injector.wiring import Provide, inject
from flask import Blueprint, jsonify, request
from models.internal_routes_model import InternalRoutesModel
import logging

internal_routes_blueprint = Blueprint('internal_routes_blueprint', __name__)


@internal_routes_blueprint.route('/internal_routes', methods=['GET'])
@inject
def invoke_internal_routes(mysql_database_service=Provide[Container.mysql_database_service]):
    logging.info('Internal Routes API has started')
    # TODO: Parse the request using the InternalRoutesModel and assign it to a variable called 'internal_routes_model'
    # ================================ YOUR CODE HERE ============================== #

    internal_routes_model = InternalRoutesModel(request.get_json())
    full_name = mysql_database_service.execute_internal_route_query(internal_routes_model.first_name)
    response = {'fullName': full_name}
    logging.info('Internal Routes API has ended')
    # TODO: Return a JSON serialized form of the response
    return jsonify(response)
