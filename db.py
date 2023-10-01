import psycopg2
from psycopg2 import OperationalError
from datetime import datetime, date, timedelta

DB_SELECT = "SELECT"
DB_INSERT = "INSERT"
###
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try: 
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection
###
def execute_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")
###      
def check_id(user_id, connection):
    cursor = connection.cursor()
    select_user_id = cursor.execute('SELECT userid FROM "BOTSHEME".infoclickuser')
    select_user_id = cursor.fetchall()
    check_state = True
    for index, elem in enumerate(select_user_id, start=0):
        if (user_id in elem):
            check_state = True
            break
        else: 
            check_state = False
    return check_state        
###
def insert_stroke(user_id, click_to_app, click_to_gift, click_location):
    cursor = DB_CONNECTION.cursor()
    click_date = date.today()
    try:
        if(not check_id(user_id, DB_CONNECTION)):
            insert_query = ('''INSERT INTO "BOTSHEME".infoclickuser (userid, clicktoapp, clicktobutton, click_date) VALUES (%s, %s, %s, %s)''')
            insert_tuple = (user_id, click_to_app, click_to_gift, click_date)
            cursor.execute(insert_query, insert_tuple)
            DB_CONNECTION.commit()
        else:
            select_click_to_app = cursor.execute(f'SELECT clicktoapp FROM "BOTSHEME".infoclickuser WHERE userid = {user_id}')
            select_click_to_app = cursor.fetchall()

            select_click_to_gift = cursor.execute(f'SELECT clicktobutton FROM "BOTSHEME".infoclickuser WHERE userid = {user_id}')
            select_click_to_gift = cursor.fetchall()

            if(not select_click_to_app[0][0] and click_location == "app"):
                update_query = (f'UPDATE "BOTSHEME".infoclickuser SET clicktoapp = {True} WHERE userid = {user_id}')
                cursor.execute(update_query)
                DB_CONNECTION.commit()

            if(not select_click_to_gift[0][0] and click_location == "gift"):
                update_query = (f'UPDATE "BOTSHEME".infoclickuser SET clicktobutton = {True} WHERE userid = {user_id}')
                cursor.execute(update_query)
                DB_CONNECTION.commit()
    except OperationalError as e:
        print(f"The error '{e}' occurred")
###
def getting_over_date(interval):
    all_click_to_gift = 0
    all_click_to_app = 0

    interval_timedelta = timedelta(days = interval)
    date_today = date.today()
    date_for_get = date_today - interval_timedelta

    cursor = DB_CONNECTION.cursor()
    select_click_date = cursor.execute(f"SELECT * FROM " + '"BOTSHEME".infoclickuser ' + f"WHERE click_date BETWEEN '{date_for_get}' AND '{date_today}'")
    select_click_date = cursor.fetchall()

    for index, elem in enumerate(select_click_date):
        if(elem[1]):
            all_click_to_app += 1
        if(elem[2]):
            all_click_to_gift += 1
    
    return all_click_to_app, all_click_to_gift
###
    
DB_CONNECTION = create_connection('BOT_DB', 'admin', '0000', '127.0.0.1', '5432')
DB_TABLE = execute_query(DB_CONNECTION, f'{DB_SELECT} * FROM "BOTSHEME".infoclickuser')
