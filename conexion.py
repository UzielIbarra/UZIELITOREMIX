import mysql.connector

class Conexion:
    def __init__(self):
        self.user = "root"
        self.password = ""
        self.database = "dbtaller_mecanico"
        self.host = "localhost"
        self.conn = None

    def open(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.conn

    def close(self):
        if self.conn is not None and self.conn.is_connected():
            self.conn.close()