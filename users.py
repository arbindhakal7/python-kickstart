from site import USER_BASE
import sqlite3
import csv


DB_NAME = 'users.db'
FILE_NAME = "sample_users.csv"



USER_INPUT = """
Enter the option:
        1. CREATE TABLE users
        2. Import data from CSV file
        3. Select Records from users    
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




def open_csv_file(file_name):

    db_data = []

    with open('sample_users.csv') as f:
        data = csv.reader(f) #iterator
        for datum in data:
            db_data.append(tuple(datum))
    return db_data

def insert_record_to_table(conn, data):
    insert_query = """
    INSERT INTO 
        users
            (first_name, last_name, company_name, address, city, country, state, zip, phone1, phone2, email, web)
    VALUES
        (?,?,?,?,?,?,?,?,?,?,?,?)
    
    """

    cur = conn.executemany(insert_query, data)
    conn.commit()
    print("All records inserted to table")




def select_records_from_table(conn):
    cur = conn.execute("SELECT * from users;")
    for row in cur:
        print(row)




def main():
    conn = create_connection(DB_NAME)

    user_input = input(USER_INPUT)

    if user_input == '1':
        #create table users
        create_table_user(conn)

    elif user_input == "2":
        data = open_csv_file(FILE_NAME)
        insert_record_to_table(conn, data)

    elif user_input == "3":
        select_records_from_table(conn)



if __name__ == '__main__':
    main()