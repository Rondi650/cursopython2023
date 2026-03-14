import os
import sqlite3
from main import DB_FILE, TABLE_NAME
from rich import print

os.system('clear')

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    print(*row)

cursor.close()
connection.close()

