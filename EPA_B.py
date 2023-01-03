import mysql.connector as ep


class EPHelper:

    def __init__(self):
        self.connection = ep.connect(user='root', password='Gurudev@50',
                                     host='127.0.0.1',
                                     database='majorproject')
        print("EP CONNECTED :)")
        self.cursor = self.connection.cursor()
        print("CURSOR CREATED :)")

    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL QUERY EXECUTED :)")

    def read(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
