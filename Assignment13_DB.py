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


# Creates the database
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
def create_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"The query executed successfully")
    except Error as oops:
        print(f"There has been an error: {oops}")


# Executes the insert queries
# Takes the query as a parameter
def read_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"There has been an error: {e}")


# Creates a separation between the menus
def partition():
    print("__" * 70)
    return


connecting = database("myDatabase")

# This variable holds the Person table
person_table = """
CREATE TABLE IF NOT EXISTS 
  customer (
  customer_id    INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name     TEXT    NOT NULL,
  last_name      TEXT    NOT NULL,
  street_address TEXT    NOT NULL,
  zip_code       INTEGER NOT NULL,
  city           TEXT    NOT NULL,
  state          TEXT    NOT NULL
);
"""
create_table(connecting, person_table)  # Adds the person table to the database

# This variable hold the Book table
book_table = """
CREATE TABLE IF NOT EXISTS
  book (
  book_id   INTEGER PRIMARY KEY AUTOINCREMENT,
  title     TEXT    NOT NULL,
  author    TEXT    NOT NULL,
  isbn      TEXT NOT NULL,
  edition   INTEGER NOT NULL,
  price     INTEGER NOT NULL,
  publisher TEXT    NOT NULL
);
"""
create_table(connecting, book_table)  # adds the books table to the database

menu = "ONWARD"
while menu != "END":
    partition()
    # This is the main menu of the program. It is in a while loop and allows the user to choose to what they want to do
    choice = input("\nWould you like to do?" +
                   "\n*press the number next to your desired choice*".upper() +
                   "\n\n1. Go to the Customers Menu"
                   "\n2. Go to the Books Menu"
                   "\n3. Leave this program"
                   "\n>>>")
    # Checks if the choice they entered is valid
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

    # If the user chooses 1 in the main menu they will be take to another menu for customers
    if choice == 1:
        menu = "ONWARD"
        while menu != "END":
            partition()
            # This menu allows the user to add, modify, delete, and print the customers
            choice = input("\nWhat would you like to do?"
                           "\n1. ADD new customer"
                           "\n2. MODIFY a customer"
                           "\n3. DELETE a customer"
                           "\n4. Print the customer table"
                           "\n5. Leave this menu"
                           "\n>>>")
            # Checks if the user entered a choice on the menu
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

            # This part of the program gets the information for a new customer, then saves the information in variables
            if choice == 1:
                first_name = input("\nWhat is the customer's First Name?"
                                   "\n>>>").title()

                last_name = input("\nLast Name?"
                                  "\n>>>").title()

                street_address = input("\nWhat is the Street Address of this customer?"
                                       "\n>>>").title()

                zip_code = input("\nWhat Zip Code is that?"
                                 "\n>>>")
                # Zip codes are 5 digits long, so I put a try statement to check if the user put 5 numbers
                while zip_code != "A Long And Random String Of Text":
                    try:
                        if len(zip_code) == 5:  # This checks the length. I found out that len() can't count integers
                            zip_code = int(zip_code)
                            break
                        else:
                            int("# Forces this try statement to fail if the value doesn't contain a proper zip code")
                    except ValueError:
                        zip_code = input("Enter a valid Zip Code please"
                                         "\n>>>")

                city = input("\nWhat City does this customer live in?"
                             "\n>>>").title()

                state = input("\nAnd the State? (2 letter abbreviation is fine)"
                              "\n>>>").title()

                # This variable contains the string to add this new person using the variables
                add_person = f"""
                INSERT INTO
                  customer (first_name, last_name, street_address, zip_code, city, state)
                VALUES
                ('{first_name}', '{last_name}', '{street_address}', '{zip_code}', '{city}', '{state}')"""

                create_table(connecting, add_person)
                print("\nI will now take you back you the menu.")

            # This section allows the user to modify information in the person table excluding the ID. That could be bad
            elif choice == 2:
                menu = "ONWARD"
                category = input("\nAlright, which category of the customer would you like to modify? (The Customer ID will remain unchanged)" +
                                 "\n*type the number next to the desired choice*".upper() +
                                 "\n1. First Name"
                                 "\n2. Last Name"
                                 "\n3. Street Address"
                                 "\n4. Zip Code"
                                 "\n5. City"
                                 "\n6. State"
                                 "\n>>>")
                # Checks if the user entered a valid choice
                while category != "A Long And Random String Of Text":
                    try:
                        category = int(category)
                        if 7 > choice > 0:
                            break
                        else:
                            int("# Forces this try statement to fail if the choice isn't 1, 2, 3, 4, 5, or 6")
                    except ValueError:
                        category = input("Enter 1, 2, 3, 4, 5, or 6"
                                         "\n>>>")
                if category == 1:
                    category = "first_name"
                elif category == 2:
                    category = "last_name"
                elif category == 3:
                    category = "street_address"
                elif category == 4:
                    category = "zip_code"
                elif category == 5:
                    category = "city"
                elif category == 6:
                    category = "state"

                cat = category.replace("_", " ").title()  # cat was supposed to be short for category.
                                                          # I did this so i could maintain the data in category, while also interacting with the user
                                                          # It just replaces the underscores with spaces, then keeps the title case trend

                value = input(f"What does the current {cat}?"
                              f"\n>>>").title()

                # A zip code contains 5 digits. This it the only category I can check here
                if category == "zip_code":
                    while category != "A Long And Random String Of Text":
                        try:
                            if len(value) == 5:
                                value = int(value)
                                break
                            else:
                                int("# Forces this try statement to fail if the value doesn't contain a proper zip code")
                        except ValueError:
                            value = input("Enter a valid Zip Code please"
                                          "\n>>>")

                new_val = input(f"What do you want to change {cat} to?"
                                f"\n>>>").title()

                # Same deal as before
                if category == "zip_code":
                    while category != "A Long And Random String Of Text":
                        try:
                            if len(value) == 5:
                                value = int(value)
                                break
                            else:
                                int("# Forces this try statement to fail if the value doesn't contain a proper zip code")
                        except ValueError:
                            value = input("Enter a valid Zip Code please"
                                          "\n>>>")

                # This variable holds the query to update a person using the variables
                update_person = f"""
                UPDATE
                  customer
                SET
                  {category} = '{new_val}'
                WHERE
                  {category} = '{value}'
                """
                create_table(connecting, update_person)

            elif choice == 3:
                value = input("\nWhat is the Customer ID of the person you want to remove?"
                              "\n>>>")
                # I wanted to check if the user actually entered an integer so i used another try statement
                while value != "Random Words":
                    try:
                        int(value)  # but i didn't want to make it an integer because i would have to typecast the variable
                        break
                    except ValueError:
                        value = input("\nEnter the ID of the Customer you wish to delete"
                                      "\n>>>")
                # I also asked for the customers last name, sort of as a fail safe
                value1 = input("\nAlright, what is the Last Name of that customer?"
                               "\n>>>").title()
                delete_person = f"""
                DELETE FROM 
                  customer
                WHERE
                  customer_id = '{value}' AND last_name = '{value1}'
                """
                create_table(connecting, delete_person)

            # This simple prints the list of people in the database
            elif choice == 4:
                every_one = "SELECT * FROM customer"
                people = read_table(connecting, every_one)

                for peeps in people:
                    print('\n', peeps)

            elif choice == 5:
                print("Back to the main menu it is.")
                menu = "END"

    # This section of the program is for the book menu
    elif choice == 2:
        menu = "ONWARD"
        while menu != 'END':
            partition()
            # Allows the user to choose what they want to do
            choice = input("\nWhat would you like to do?"
                           "\n1. ADD new book"
                           "\n2. MODIFY a book"
                           "\n3. DELETE a book"
                           "\n4. Print the books table"
                           "\n5. Leave this menu"
                           "\n>>>")
            # Checks to see if the user enter a valid value
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
                title = input("\nWhat is the Book Title?"
                              "\n>>>").title()  # Finally, the .title() is where it belongs

                author = input("\nWho is the Author of the book?"
                               "\n>>>").title()

                isbn = input("\nWhat is the ISBN of the book? (dashes(-) are included)"
                             "\n>>>")
                # The isbn contains - in between some of the numbers, so i will replace them with "" to check it using another variable,
                while isbn != "How did this code get so long":
                    try:
                        checking = isbn.replace("-", "")
                        int(checking)
                        break
                    except ValueError:
                        isbn = input("\nPlease enter a valid ISBN"
                                     "\n>>>")

                edition = input("\nWhat Edition is the book? (Only numbers: 4th = 4) "
                                "\n>>>")
                # Checks if the user entered a digit
                while edition != "Take a guess for how long this will get":
                    try:
                        edition = int(edition)
                        break
                    except ValueError:
                        edition = input("\nPlease enter the number of the Edition. No text"
                                        "\n>>>")

                price = input("\nWhat is the Price of the book? (dollar signs($) and dots(.) are included)"
                              "\n>>>")
                # Uses the same method as the ISBN variable
                while price != "Late night coding":
                    try:
                        cost = price.replace("$",'').replace(".", '')
                        int(cost)
                        break
                    except ValueError:
                        price = input("\nEnter the Price of the book. (For example: $12.75)"
                                      "\n>>>")

                publisher = input("\nAnd the Publisher is?"
                                  "\n>>>").title()

                # This variable contains the string to add this new person using the variables
                add_book = f"""
                INSERT INTO
                  book (title, author, isbn, edition, price, publisher)
                VALUES
                ('{title}', '{author}', '{isbn}', '{edition}', '{price}', '{publisher}')"""

                create_table(connecting, add_book)
                print("I'm taking you back you the main menu.")

            elif choice == 2:
                category = input("\nAlright, which category of the book would you like to modify? (The Book ID will remain unchanged)" +
                                 "\n*type the number next to the desired choice*".upper() +
                                 "\n1. Title"
                                 "\n2. Author"
                                 "\n3. ISBN"
                                 "\n4. Edition"
                                 "\n5. Price"
                                 "\n6. Publisher"
                                 "\n>>>")
                # Checks if the user entered a valid choice
                while category != "Oof":
                    try:
                        category = int(category)
                        if 7 > choice > 0:
                            break
                        else:
                            int("# Forces this try statement to fail if the choice isn't 1, 2, 3, 4, 5, or 6")
                    except ValueError:
                        category = input("Enter 1, 2, 3, 4, 5, or 6"
                                         "\n>>>")

                if category == 1:
                    category = "title"
                elif category == 2:
                    category = "author"
                elif category == 3:
                    category = "isbn"
                elif category == 4:
                    category = "edition"
                elif category == 5:
                    category = "price"
                elif category == 6:
                    category = "publisher"

                # This variable will contain the information I need to change the data. This has the old data
                value = input(f"What does the current value for the {category.title()} say?"
                              f"\n>>>").title()

                if category == 'isbn':
                    # The isbn contains - in between some of the numbers, so i will replace them with "" to check it using another variable,
                    while value != "I have to reuse some code":
                        try:
                            checking = value.replace("-", "")
                            int(checking)
                            break
                        except ValueError:
                            value = input("\nPlease enter the current and valid ISBN"
                                          "\n>>>")

                if category == "edition":
                    # Checks if the user entered a digit
                    while value != "Blah":
                        try:
                            value1 = int(value)
                            break
                        except ValueError:
                            value = input("\nPlease enter the number of the current Edition. No text"
                                          "\n>>>")

                if category == 'price':
                    # Uses the same method as the ISBN variable
                    while value != "Brain loading":
                        try:
                            val = value.replace("$",'').replace(".", '')
                            int(val)
                            break
                        except ValueError:
                            value = input("\nEnter the current Price of the book. (For example: $12.75)"
                                          "\n>>>")

                # This variable will hold the new data
                value1 = input(f"What is the {category} you want to change it to?"
                               f"\n>>>").title()
                if category == 'isbn':
                    # The isbn contains - in between some of the numbers, so i will replace them with "" to check it using another variable,
                    while value1 != "I still have to reuse some code":
                        try:
                            checking = value1.replace("-", "")
                            int(checking)
                            break
                        except ValueError:
                            value1 = input("\nPlease enter a valid ISBN"
                                           "\n>>>")

                if category == "edition":
                    # Checks if the user entered a digit
                    while value1 != "Blah Blah":
                        try:
                            value1 = int(value1)
                            break
                        except ValueError:
                            value1 = input("\nPlease enter the number of the Edition. No text"
                                           "\n>>>")

                if category == 'price':
                    # Uses the same method as the ISBN variable
                    while value1 != "Brain still loading":
                        try:
                            val1 = value1.replace("$",'').replace(".", '')
                            int(val1)
                            break
                        except ValueError:
                            value1 = input("\nEnter the Price of the book. (For example: $25.50)"
                                           "\n>>>")

                # This variable holds the string to modify book information
                update_book = f"""
                UPDATE
                  customer
                SET
                  {category} = '{value1}'
                WHERE
                  {category} = '{value}'
                """
                create_table(connecting, update_book)

            # This section allows the user to delete a book from the table
            elif choice == 3:
                value = input("\nWhat is the Book ID of the book you want to remove?"
                              "\n>>>")
                # I wanted to check if the user entered an integer so i used another try statement
                while value != "Randoms":
                    try:
                        int(value)  # but i didn't want to save it as an integer
                        break
                    except ValueError:
                        value = input("\nEnter the ID of the Book you wish to delete"
                                      "\n>>>")

                # I also asked for the isbn, as a back up
                value1 = input("\nAlright, what is the ISBN of that book?"
                               "\n>>>")
                # Still the same ISBN checks as before
                while value1 != "I'm starting to get tired now":
                    try:
                        checking = value1.replace("-", "")
                        int(checking)
                        break
                    except ValueError:
                        value1 = input("\nPlease enter a valid ISBN"
                                       "\n>>>")

                delete_book = f"""
                DELETE FROM 
                  book
                WHERE
                  book_id = '{value}' AND isbn = '{value1}'
                """
                create_table(connecting, delete_book)

            elif choice == 4:
                all_books = "SELECT * FROM book"
                books = read_table(connecting, all_books)

                for book in books:
                    print('\n', book)

            elif choice == 5:
                print("Back to the main menu it is.")
                menu = "END"

    elif choice == 3:
        print("Bye")
        menu = "END"
