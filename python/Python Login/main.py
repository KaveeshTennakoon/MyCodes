import sqlite3


def signup(cursor):

    while True:

        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter your email: ")


        try :
            cursor.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
            break
        except sqlite3.IntegrityError:
            print("\nUsername or Email alredy uesd\nPlease enter again\n")
        

def login():

    username = input("Enter your username: ")
    password = input("Enter your password: ")

def main():

    sql = sqlite3.connect("info.db")

    cursor = sql.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
                   username TEXT PRIMARY KEY,
                   password TEXT,
                   email TEXT PRIMARY KEY)    
        ''') 

    while True:

        option = int(input("1: Sign up\n2: Log in\nEnter the int you need: "))
        print()

        if option == 1 :
            signup(cursor)
            sql.commit()
        else:
            login()

        quit = input("\nEnter 'quit' to exit the program(if not type anything): ").lower()

        if quit == "quit":
            break

    sql.close()

if __name__ == "__main__":
    main()