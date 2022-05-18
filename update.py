import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\chels\OneDrive - DEPED REGION 4A-1\Documents\Database1.accdb;')
    print("Database is Connected")


    Address = "Cavite"
    user_id = 3

    database = connection.cursor()
    database.execute('UPDATE Table1 SET Address=? WHERE id=?',(Address,user_id))
    connection.commit()

    print("Database is updated")

except pyodbc.Error:
    print("Database is NOT connected")