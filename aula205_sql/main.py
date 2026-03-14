from curses.ascii import TAB
import sqlite3
from pathlib import Path

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
sql1 = (f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(?,?)')

cursor.execute(sql1, ['Pedro',85]) # execute passa apenas 1 valor
connection.commit()

################################################################################

# Forma correta com varios valores simultaneos em executemany
sql2 = (f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(?,?)')

cursor.executemany(sql2, [['Joao',75],['Maria',60]]) # Passa varios valores
connection.commit()

################################################################################

# Forma correta com dicionarios em execute (NAO O EXECUTEMANY)
sql2 = (f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(:name,:weight)')

# cursor.execute(sql2, {'name':'Joana', 'weight': 55}) 
cursor.executemany(sql2, (
    {'name':'Jurandir', 'weight': 82},
    {'name':'Sandra', 'weight': 98}
     ))
connection.commit()

################################################################################


cursor.close()
connection.close()

if __name__ == '__main__':
    print(sql1)
    print(sql2)