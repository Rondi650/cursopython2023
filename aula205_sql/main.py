import os
from curses.ascii import TAB
import sqlite3
from pathlib import Path
from rich import print

os.system('clear')

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

################################################################################

# Apaga todos os registros da tabela
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

################################################################################

# Apaga o historicos de ids automaticos
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

################################################################################

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '( id INTEGER PRIMARY KEY AUTOINCREMENT,' 
    'name TEXT,' 
    'weight REAL'
    ')'
)
connection.commit()

################################################################################

# Registra valores nas colunas da tabela
# Forma errada, devido a sql injection - para valores do usuario
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight)'
    'VALUES'
    '(NULL, "Samara", 85),'
    '(NULL, "Heitor", 35)'
)
connection.commit()

################################################################################

# Forma correta
# Com placeholders os valores sao passados posteriormente
sql = (f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(?,?)')
print(sql)

cursor.execute(sql, ['Pedro',85]) # execute passa apenas 1 valor
connection.commit()

################################################################################

# Forma correta com varios valores simultaneos em executemany
sql = (f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(?,?)')
print(sql)

cursor.executemany(sql, [['Joao',75],['Maria',60]]) # Passa varios valores
connection.commit()

################################################################################

# Forma correta com dicionarios em execute (NAO O EXECUTEMANY)
sql = (f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(:name,:weight)')
print(sql, end='\n\n')

# cursor.execute(sql2, {'name':'Joana', 'weight': 55}) 
cursor.executemany(sql, (
    {'name':'Jurandir', 'weight': 82},
    {'name':'Sandra', 'weight': 98}
     ))
connection.commit()

################################################################################

if __name__ == '__main__':

    # deletar com where 
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id=3'
    )

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET '
        'name = "Rondinelle", '
        'weight = 95 '
        'WHERE id = 6'
    )

    connection.commit()

    cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        print(*row)

################################################################################

    cursor.close()
    connection.close()