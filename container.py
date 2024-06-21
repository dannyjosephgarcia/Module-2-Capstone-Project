from dependency_injector import containers, providers
from services.mysql_database_service import MySQLDatabaseService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['./config.yaml'])
    # TODO: Using the hierarchy of the config.yaml file structure, create a Singleton class to inject the
    #  MySQLDatabaseService class into the 'internal_routes.py' route API.
    #  Hint: you'll need to set environment variables...
    # ================================ YOUR CODE HERE ============================== #

    # TODO: Using the hierarchy of the config.yaml file structure, create a Singleton class to inject the
    #  ExternalAPIService class into the 'external_routes.py' route API
    # ================================ YOUR CODE HERE ============================== #
