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
        self.cnx = mysql.connector.connect(user=self.username,
                                           password=self.password,
                                           host=self.host,
                                           database=self.database)

    def execute_internal_route_query(self, request):
        # TODO: Complete this class method to return the firstName field of the individual(s) contained in the request.
        #  Note: in the event that more than one individual is returned, return the name found at index 0
        # ================================ YOUR CODE HERE ============================== #

        names = []
        first_name = names[0]
        return first_name
