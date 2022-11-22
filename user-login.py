import mariadb

s = mariadb.connect(
    host="localhost",
    user="root",
    password="",
    database="user"
)
a = s.cursor()

def existinguser(username):
    a.execute("select names from info")
    db=a.fetchall()
    if (db):
        print("Username already exists")
        signin()
    else:
        signup()


def signin():
    newname = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Login successful")


def signup():
    name = input("Re-enter your username: ")
    password = input("Please enter your password: ")
    a.execute("insert into info values(?,?)", (name, password))
    s.commit()
    print("Account created successfully")


username = input("Enter your username: ")
existinguser(username)