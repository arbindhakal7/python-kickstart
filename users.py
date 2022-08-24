from site import USER_BASE
import sqlite3


DB_NAME = 'users.db'


USER_INPUT = """
Enter the option:
        1. CREATE TABLE users
"""


CREATE_USERS_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name CHAR(255) NOT NULL,
        last_name CHAR(255) NOT NULL,
        company_name CHAR(255) NOT NULL,
        address CHAR(255) NOT NULL,
        city CHAR(255) NOT NULL,
        country CHAR(233) NOT NULL,
        state CHAR(255) NOT NULL,
        zip REAL NOT NULL,
        phone1 CHAR(255) NOT NULL,
        phone2 CHAR(255),
        email CHAR(255) NOT NULL,
        web text
    );
"""

def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn


def create_table_user(conn):
    cur = conn.cursor()
    cur.execute(CREATE_USERS_TABLE_QUERY)
    print("User table created successfully")



def main():
    conn = create_connection(DB_NAME)

    user_input = input(USER_INPUT)

    if user_input == '1':
        #create table users
        create_table_user(conn)



if __name__ == '__main__':
    main()