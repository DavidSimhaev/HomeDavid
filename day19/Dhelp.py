import mysql.connector


class DataHelp:
    def __init__(self):

        self.findb = mysql.connector.connect(
            host="localhost", user="root", password="098098098"
        )
        self.cursor = self.findb.cursor()

    def executeSomeQuery(self, query):
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def queryWithCommit(self, query):
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        self.findb.commit
        self.cursor.close()
        return


d = DataHelp()
query = "select year, month, business.name as business, income from chema.finances left join chema.business on business.id=business"

r = d.executeSomeQuery(query=query)

print(r)
