import sqlite3

conn = sqlite3.connect('data.db')

c = conn.cursor()


c.execute('CREATE TABLE IF NOT EXISTS accounts(id INTEGER PRIMARY KEY, platform TEXT, username TEXT, email TEXT, password TEXT, backup_email TEXT, two_factor_auth TEXT)')

def entry():
    platform = input("platform: ")
    username = input("username: ")
    email = input("email address: ")
    password = input("password: ")
    backup_email = input("backup email address: ")
    two_factor_auth = input("two factor auth: ")

    c.execute("INSERT INTO accounts (platform, username, email, password, backup_email, two_factor_auth) VALUES (?, ?, ?, ?, ?, ?)",
        (platform, username, email, password, backup_email, two_factor_auth))
    conn.commit()

def read():
    c.execute('SELECT * FROM accounts')
    for row in c.fetchall():
        print(row)

def search():
    test = True
    while test == True:     #set column you want to search
        userSearch = input("1. platform\n2. username\n3. email\n4. password\n5. backup email\n6. two factor\n(q)uit\nType column number you want to search: ")

        if userSearch == "1":
            search = input("Enter query: ")
            c.execute('SELECT * FROM accounts WHERE platform=?', (search,))
            for row in c:
                print(row)
            test = False
        elif userSearch == "2":
            search = input("Enter query: ")
            c.execute('SELECT * FROM accounts WHERE username=?', (search,))
            for row in c():
                print(row)
            test = False
        elif userSearch == "3":
            search = input("Enter query: ")
            c.execute('SELECT * FROM accounts WHERE email=?', (search,))
            for row in c:
                print(row)   
            test = False
        elif userSearch == "4":
            search = input("Enter query: ")
            c.execute('SELECT * FROM accounts WHERE password=?', (search,))
            for row in c:
                print(row)         
            test = False
        elif userSearch == "5":
            search = input("Enter query: ")
            c.execute('SELECT * FROM accounts WHERE backup_email=?', (search,))
            for row in c:
                print(row)      
            test = False
        elif userSearch == "6":
            search = input("Enter query: ")
            c.execute('SELECT * FROM accounts WHERE two_factor_auth=?', (search,))
            for row in c:
                print(row)      
            test = False
        elif userSearch == "q" or userSearch == "Q":
            break
        else:
            print("Invalid input...")

def edit():
    test = True
    while test == True:
        row = input("Enter the row number: ")
        userSearch = input("1. platform\n2. username\n3. email\n4. password\n5. backup email\n6. two factor\nType column number you want to edit: ")
        newValue = input("Enter the new value: ")
        if userSearch == "1":
            c.execute('UPDATE accounts SET platform=? WHERE id=?', (newValue, row))
            test = False
        elif userSearch == "2":
            c.execute('UPDATE accounts SET username=? WHERE id=?', (newValue, row))
            test = False
        elif userSearch == "3":
            c.execute('UPDATE accounts SET email=? WHERE id=?', (newValue, row))
            test = False
        elif userSearch == "4":
            c.execute('UPDATE accounts SET password=? WHERE id=?', (newValue, row))
            test = False
        elif userSearch == "5":
            c.execute('UPDATE accounts SET backup_email=? WHERE id=?', (newValue, row))
            test = False
        elif userSearch == "6":
            c.execute('UPDATE accounts SET two_factor_auth=? WHERE id=?', (newValue, row))
            test = False
        elif userSearch == "q" or userSearch == "Q":
            break
        else:
            print("Invalid input...")

    testy = True
    while testy == True:
        print("Row: ", str(row), " changed to:", str(newValue))
        commit = input("Are you sure you want to save? (y)es / (n)o : ")
        if commit == "y" or commit == "Y":
            print("Saved!")
            conn.commit()
            testy = False
        elif commit == "n" or commit == "N":
            print("No changes were made!")
            conn.rollback()
            testy = False
        else:
            print("Invalid input...")

def delete():
    row = input("Enter the row number you would like to delete: ")
    c.execute('DELETE FROM accounts WHERE id=?', (row))
    testy = True
    while testy == True:
        choice = input("Row: " + str(row) + " will be deleted, are you sure? (y)es / (n)o : ")
        if choice == "y" or choice == "Y":
            print("Deleted!")
            conn.commit()
            testy = False
        elif choice == "n" or choice == "N":
            print("No changes were made!")
            conn.rollback()
            testy = False
        else:
            print("Invalid input...")


testX = True
while testX == True:
    option = input("(a)dd / (v)iew / (s)earch / (e)dit / (d)elete / (q)uit : ")
    if option == "a" or option == "A":
        entry()
        print("Successfully added")
    elif option == "v" or option == "V":
        read()
    elif option == "s" or option == "S":
        search()
    elif option == "e" or option == "E":
        edit()
    elif option == "d" or option == "D":
        delete()
    elif option == "q" or option == "Q":
        testX = False
    else:
        input("Invalid input...")

c.close()  
conn.close()
