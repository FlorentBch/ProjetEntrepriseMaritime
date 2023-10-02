from DataBase.ConnectionDatabase import ConnectDB

db = ConnectDB()
BoolConnection = False
try:
    db.database
    BoolConnection = True
except AttributeError:
    BoolConnection = False


def InsertNumberTrade(liste:list()): 
    mycursor = db.cursor()
    for i in liste:
        InsertNumberTrade = """INSERT INTO trade (ID_TRADE) VALUES (%s) """
        mycursor.execute(InsertNumberTrade, (i,))
        db.commit()
        print(mycursor.rowcount, "record inserted.")


#         sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()


# if BoolConnection == True:
#     try:
#         InsertNumberTrade = """INSERT INTO trade (ID_TRADE) 
#                             VALUES 
#                             () """

#         cursor = connection.cursor()
#         cursor.execute(mySql_insert_query)
#         connection.commit()
#         print(cursor.rowcount, "Record inserted successfully into Laptop table")
#         cursor.close()

#     except mysql.connector.Error as error:
#         print("Failed to insert record into Laptop table {}".format(error))

#     finally:
#         if connection.is_connected():
#             connection.close()
#             print("MySQL connection is closed")
# else:
#     print("Connection failed")
