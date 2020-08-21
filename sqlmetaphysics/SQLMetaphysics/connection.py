import sqlite3


class DatabaseConnection:

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.connection
        
    def execute(self, query, params):
        self.cursor.execute(query, params or ())

    def __exit__(self, exec_type, exc_val, traceback):
        self.connection.close()