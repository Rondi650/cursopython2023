# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
from curses.ascii import TAB
import os
import dotenv
import pymysql

TABLE_NAME = 'customers'

os.system('clear')
dotenv.load_dotenv()

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)

cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (' 
    'id INT NOT NULL AUTO_INCREMENT, ' 
    'nome VARCHAR(50) NOT NULL, ' 
    'idade INT NOT NULL, ' 
    'PRIMARY KEY (id) '
    ') '
)
cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')

cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) '
    'VALUES '
    '("rondi",35), '
    '("samara", 28)'
)

connection.commit()

cursor.close()
connection.close()
