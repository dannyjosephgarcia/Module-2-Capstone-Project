import mysql.connector


class MySQLDatabaseService:
    def __init__(self, host, username, password, database):
        self.cnx = None
        self.database = database
        self.host = host
        self.password = password
        self.username = username
        self.initialize_db_connection()

    def initialize_db_connection(self):
        # TODO: Use the mysql.connector library to create a connection to your MySQL Database and assign it to
        #  the self.cnx attribute
        # ================================ YOUR CODE HERE ============================== #
        return None

    def execute_internal_route_query(self, first_name):
        # TODO: Complete this class method to return the first and last name of the individual contained in the request.
        #  Note: in the event that more than one individual is returned, return the names found at index 0
        # ================================ YOUR CODE HERE ============================== #

        first_name = []
        last_name = []

        full_name = first_name[0] + ' ' + last_name[0]
        return full_name
