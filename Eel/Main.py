from tabulate import tabulate
from datetime import datetime
import mysql.connector
import eel

eel.init('Web')
print(tabulate([['Eel App Connected At' , f'{datetime.now()}']],tablefmt='grid'))
@eel.expose()
def Connect_Database(host: str, user: str, password: str, port: int , database:str):
    Database = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database
    )
    global cursor
    cursor = Database.cursor()
    print(tabulate([['Database Connected At :' , f'{datetime.now()}']] , tablefmt='grid'))


eel.start('Connect.html', mode='chrome')
