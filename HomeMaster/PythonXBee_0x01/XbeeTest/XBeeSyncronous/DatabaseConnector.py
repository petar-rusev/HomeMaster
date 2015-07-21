import mysql.connector;
from mysql.connector import errorcode
class DatabaseConnector :
    
    def __init__(self,user,password,host,db):
        self.user = user;
        self.password = password;
        self.host = host;
        self.db = db;
        try:
            self.connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.db);
            self.cursor = self.connection.cursor();
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    
                           
    def initiateQuery(self,query,data_query):
        try:
            self.cursor.execute(query,data_query);
            self.connection.commit();
        except:
            self.connection.rollback();

    def __del__(self):
        self.connection.close();

    def initiateConnection(self):
        self.connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.db)
