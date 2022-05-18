import pyodbc
msa_drivers = [x for x in pyodbc.drivers() if 'access']

print(f'MS-ACCESS Drivers:{msa_drivers}')
connection b/n access and pycharm:
import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ="C:\Users\chels\OneDrive - DEPED REGION 4A-1\Documents\Database1.accdb";')
    print("Database is Connected")

except pyodbc.Error:
    print("Database is NOT connected")



    operations:
    Save, Update, Delete, View, Generator