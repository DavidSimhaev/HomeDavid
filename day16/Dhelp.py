import mysql.connector

class DataHelp():
    
    def __init__(self):
        
        self.findb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "098098098"
        )
        self.cursor = self.findb.cursor()
        
    def checkNoExist(self, year, month, business): # проверка если не существует данные
        self.cursor = self.findb.cursor()
        self.query = f"select * from predicator.train where year='{year}' and month ='{month}' and business ='{business}'" 
        self.cursor.execute(self.query)
        results = self.cursor.fetchall()
        return len(results) == 0 
    
    def replaceData(self, year, month, business, income):
        self.cursor = self.findb.cursor()
        query = f"update predicator.train set income='{income}' where year='{year}' and month='{month}' and business='{business}' "
        self.cursor.execute(query)
        self.findb.commit()
        self.cursor.close()
    def insertData(self, year, month, business, income):
        self.cursor = self.findb.cursor()
        query = f"insert into predicator.train (year, month, business, income) values ({year},{month},{business},{income})"
        self.cursor.execute(query)
        self.findb.commit()
        self.cursor.close()
    
    def readAllData(self):
        query = f"select year, month, business, income from predicator.train order by year, month" 
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result
    
    def executeQuery(self, query): 
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result
    
    
    def readSomeData(self, key, value):
        query = f"select year, month, business, income from predicator.train where {key}={value} order by year, month" 
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result
    
    
    
    
    
    
d = DataHelp()
#print(d.readSomeData("year", 2002))
#def inserData(year, mouth, business, income):
    



a = 2002
b = 100
c = 2
d = 12342