import sqlite3

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


def updateData(connection, cursor, country, **data):
    headers = list(data.keys())
    table_name = country.lower()
    if headers[0] == 'Year' and headers[1] == 'Rate':
        try:
            cursor.execute(f"INSERT INTO {table_name} VALUES ('{data[headers[0]]}', '{data[headers[1]]}', '','')")
            connection.commit()
        except sqlite3.IntegrityError:
            print(f"Data is already filled ({country}, {data})")
