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

# inclusao de dados hardcoded
cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) '
    'VALUES '
    '("rondi",35), '
    '("samara", 28)'
)

# inclusao por tupla ou lista
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) '
    'VALUES '
    '(%s,%s) '
)
print(sql)

data1 = ["heitor", 8]

cursor.execute(sql, data1)

# inclusao por dicionario
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) '
    'VALUES '
    '(%(name)s,%(age)s) '
)
print(sql)

data2 = {
    "name": "joao",
    "age": 22
}
cursor.execute(sql, data2)

# inclusao de varios valores por dicionario
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) '
    'VALUES '
    '(%(name)s,%(age)s) '
)
print(sql)

data2 = (
    {"name": "joao","age": 22},
    {"name": "maria","age": 15},
    {"name": "ana","age": 18},
    {"name": "sofia","age": 13},
    )

cursor.executemany(sql, data2)


# padrao para todas consultas
connection.commit()
cursor.close()
connection.close()
