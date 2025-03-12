import mysql.connector

class Conexion:
    def __init__(self):

        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "prueba"
        self.conn = None

    def open(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            database=self.database
        )
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
