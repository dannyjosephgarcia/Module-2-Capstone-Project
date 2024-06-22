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

    def execute_internal_route_query(self, first_name):
        # TODO: Complete this class method to return the first and last name of the individual contained in the request.
        #  Note: in the event that more than one individual is returned, return the names found at index 0
        # ================================ YOUR CODE HERE ============================== #
        cursor = self.cnx.cursor()
        query = """SELECT * FROM sakila.actor WHERE first_name=%s;"""
        cursor.execute(query, [first_name])
        result = cursor.fetchall()
        cursor.close()
        self.cnx.close()
        first_name = []
        last_name = []
        first_name.append(result[0][1])
        last_name.append(result[0][2])
        full_name = first_name[0] + ' ' + last_name[0]
        return full_name
