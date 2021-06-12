import sqlite3
import math

db_name = 'suicideData.db'


def isDatabaseAvailable():
    try:
        connection = sqlite3.connect(f'file:db\\{db_name}?mode=rw', uri=True)
        print(f"Database {db_name} already exists\n------------------")
        return connection
    except sqlite3.OperationalError:
        connection = sqlite3.connect(f'file:db\\{db_name}?mode=rwc', uri=True)
        print(f"Database {db_name} created\n------------------")
        return connection


def isTableExists(connection, cursor, table_name):
    try:
        cursor.execute(f"SELECT 1 FROM {table_name}")
        print(f"Table {table_name} already exists\n------------------")
        return True
    except sqlite3.OperationalError:
        print(f"Table {table_name} not found...\nCreating.")
        tmp_state = createTable(connection, cursor, table_name)
        if tmp_state:
            return True
        else:
            return False


def createTable(connection, cursor, table_name):
    try:
        cursor.execute(
            f"Create table {table_name}(year integer PRIMARY KEY, suicide_rate text, population_amount text, suicide_amount text)")
        connection.commit()
        print(f"Table {table_name} created\n------------------")
        return True
    except Exception as exc:
        print(f"Table isn't created: {exc}\n------------------")
        return False


def updateSuicideData(connection, cursor, country, **data):
    headers = list(data.keys())
    table_name = country.lower()
    if headers[0] == 'Year' and headers[1] == 'Rate':
        try:
            cursor.execute(f"INSERT INTO {table_name} VALUES ('{data[headers[0]]}', '{data[headers[1]]}', '','')")
            connection.commit()
        except sqlite3.IntegrityError:
            print(f"Data is already exists ({country}, {data})")


def updatePopulationData(connection, cursor, table_name, **data):
    headers = list(data.keys())
    if headers[0] == 'Year' and headers[1] == 'Population':
        cursor.execute(f"SELECT suicide_rate, population_amount FROM {table_name} WHERE year = {data[headers[0]]}")
        tmp_result = cursor.fetchall()
        if tmp_result and tmp_result[0][1] == "":
            suicide_amount = math.ceil((float(tmp_result[0][0]) * float(data[headers[1]])) / 100000)
            cursor.execute(
                f"UPDATE {table_name} SET population_amount = {data[headers[1]]}, suicide_amount = {suicide_amount} WHERE year = {data[headers[0]]}")
            cursor.fetchall()
            connection.commit()
            print(f"Added data to {data[headers[0]]} year: {headers[1]}: {data[headers[1]]}\n------------------")
        else:
            print(f"Data already exists ({data[headers[0]]} year: {headers[1]}: {data[headers[1]]})\n------------------")