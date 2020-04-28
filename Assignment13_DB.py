# Jackson J
# 4.27.2020
# This file contain 2 tables that use the sqlite3 import.
# This program will allow the user to:
# -create(add) new customers and books
# -modify those tables
# -print the contents of the table
# -delete from that table
# These will all be in menu's presented to the user
import sqlite3
from sqlite3 import Error


def database(connection):
    connect = None
    try:
        connect = sqlite3.connect(connection)
        print('connection successful'.upper())
    except Error as oops:
        print('There has been an error:', oops)
    return connect


# Executes the table queries
# Takes the query as a parameter
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Executes the insert queries
# Takes the query as a parameter
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def partition():
    print("__" * 70)
    return


connecting = database("myDatabase")

# String holds the query to create a table
person_table = """
CREATE TABLE IF NOT EXISTS 
  person (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER
);
"""

book_table = """
CREATE TABLE IF NOT EXISTS
  book (
  book_id   INTEGER PRIMARY KEY AUTOINCREMENT,
  title     TEXT    NOT NULL,
  author    TEXT    NOT NULL,
  isbn      INTEGER NOT NULL,
  edition   INTEGER NOT NULL,
  price     INTEGER NOT NULL,
  publisher TEXT    NOT NULL
);
"""

menu = "ONWARD"
while menu != "END":
    partition()
    choice = input("\nWould you like to do?" +
                   "\n*press the number next to your desired choice*".upper() +
                   "\n\n1. Go to the Customers Menu"
                   "\n2. Go to the Books Menu"
                   "\n3. Leave this program"
                   "\n>>>")
    while choice != "A Long And Random String Of Text":
        try:
            choice = int(choice)
            if 4 > choice > 0:
                break
            else:
                int("# Forces this try statement to fail if the choice isn't 1, 2, or 3")
        except ValueError:
            choice = input("Enter 1, 2 or 3"
                           "\n>>>")

    if choice == 1:
        menu = "ONWARD"
        while menu != "END":
            partition()
            choice = input("\nWhat would you like to do?"
                           "\n1. ADD new customer"
                           "\n2. MODIFY a customer"
                           "\n3. DELETE a customer"
                           "\n4. Print the customer table"
                           "\n5. Leave this menu"
                           "\n>>>")
            while choice != "A Long And Random String Of Text":
                try:
                    choice = int(choice)
                    if 6 > choice > 0:
                        break
                    else:
                        int("# Forces this try statement to fail if the choice isn't 1, 2, 3, 4, or 5")
                except ValueError:
                    choice = input("Enter 1, 2, 3, 4, or 5"
                                   "\n>>>")
            if choice == 1:
                customer_id = input("\nWhat is the Customer ID of this new customer?"
                                    "\n>>>")
                first_name = input("\nFirst Name?"
                                   "\n>>>")
                last_name = input("\nLast Name?"
                                  "\n>>>")
                street_address = input("\nWhat is the Street Address of this customer?"
                                       "\n>>>")
                zip_code = input("\nWhat Zip Code is that?"
                                 "\n>>>")
                city = input("\nWhat City does this customer live in?"
                             "\n>>>")
                state = input("\nAnd the State?"
                              "\n>>>")

                add_person = f"""
                INSERT INTO
                  person
                VALUES
                ({customer_id}, {first_name}, {last_name}, {street_address}, {zip_code}, {city}, {state})"""

                print("\nThe values have been entered."
                      "\nI will now take you back you the main menu.")

            if choice == 2:
                menu = "ONWARD"
                update_person = f"""
                UPDATE
                  person
                SET
                  last_name = ''
                WHERE
                  last_name = ''
                """

            if choice == 3:
                menu = "ONWARD"

            if choice == 4:
                every_one = "SELECT * FROM person"
                people = execute_read_query(connecting, every_one)

                for peeps in people:
                    print(people)

            if choice == 5:
                print("Back to the main menu it is.")
                break

    if choice == 2:
        menu = "ONWARD"
        while menu != 'END':
            partition()
            choice = input("\nWhat would you like to do?"
                           "\n1. ADD new book"
                           "\n2. MODIFY a book"
                           "\n3. DELETE a book"
                           "\n4. Print the books table"
                           "\n5. Leave this menu"
                           "\n>>>")
            while choice != "A Long And Random String Of Text":
                try:
                    choice = int(choice)
                    if 6 > choice > 0:
                        break
                    else:
                        int("# Forces this try statement to fail if the choice isn't 1, 2, 3, 4, or 5")
                except ValueError:
                    choice = input("Enter 1, 2, 3, 4, or 5"
                                   "\n>>>")

                if choice == 1:
                    book_id = input("\nWhat is the Book ID?"
                                    "\n>>>")
                    title = input("\nWhat is the Book Title?"
                                  "\n>>>")
                    author = input("\nWho is the Author of the book?"
                                   "\n>>>")
                    isbn = input("\nWhat is the ISBN of the book?"
                                 "\n>>>")
                    edition = input("\nWhat Edition is the book?"
                                    "\n>>>")
                    price = input("\nWhat is the Price of the book?"
                                  "\n>>>")
                    publisher = input("\nAnd the Publisher is?"
                                      "\n>>>")

                    print("I'm taking you back you the main menu.")

            if choice == 2:
                menu = "ONWARD"
                update_book = """
                """
            if choice == 3:
                menu = "ONWARD"

            if choice == 4:
                all_books = "SELECT * FROM book"
                books = execute_read_query(connecting, all_books)

                for book in books:
                    print(book)

            if choice == 5:
                print("Back to the main menu it is.")
                break

    if choice == 3:
        print("Bye")
        menu = "END"
