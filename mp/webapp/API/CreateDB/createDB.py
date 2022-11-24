# import MySQLdb


# class CreateDB:

#     def __init__(self):
#         HOST = "sql6.freemysqlhosting.net"
#         USER = "sql6580154"
#         PASSWORD = "DfAgZAZTts"
#         DATABASE = "sql6580154"
#         self.connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
        
#     def createTables(self):
#         with self.connection.cursor() as cursor:
#             cursor.execute(open("sql1.2.sql", "r").read())
#         self.connection.commit()

# if __name__ == "__main__":
#     db = CreateDB()
#     db.createTables()