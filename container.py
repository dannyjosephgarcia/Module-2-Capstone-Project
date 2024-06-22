import os
from clients.dummyapi_client import DummyAPIClient
from dependency_injector import containers, providers
from services.external_api_service import ExternalAPIService
from services.mysql_database_service import MySQLDatabaseService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['./config.yaml'])

    dummyapi_client = providers.Singleton(DummyAPIClient,
                                          config.dummyapi.base_url)

    # TODO: Using the hierarchy of the config.yaml file structure, create a Singleton class to inject the
    #  MySQLDatabaseService class into the 'internal_routes.py' route API.
    #  Hint: you'll need to set environment variables...
    # ================================ YOUR CODE HERE ============================== #

    # TODO: Using the hierarchy of the config.yaml file structure, create a Singleton class to inject the
    #  ExternalAPIService class into the 'external_routes.py' route API.
    #  Hint: you'll have to use the dummyapi_client as a dependency
    # ================================ YOUR CODE HERE ============================== #

