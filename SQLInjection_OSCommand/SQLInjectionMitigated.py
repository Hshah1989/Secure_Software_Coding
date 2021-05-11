"""
Hiren Shah
3/24/21
SQLInjectionMitigated
"""
import sqlite3

def login_screen ():
    print("--- LOGIN SCREEN ---")
    username = input("Username: ")
    password = input("password: ")
    perform_login(username, password)
    
def perform_login(username, password):
    # mitigate SQL Injection using DB-API's parameter substitution
    varTuple = (username, password)
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", varTuple)
    
    ''' old vulnerable code
     cursor.execute("SELECT * FROM users WHERE username = " + username +
    "' AND password = '" + password + "';")
    '''
    print(cursor.fetchall())

dbConnection = sqlite3.connect('example.db')

cursor = dbConnection.cursor()

#cursor.execute("DROP TABLE users")

#create table
cursor.execute(''' 
CREATE TABLE users (
    userID int primary key,
    username varchar(255),
    password varchar(255)
);
''')
# add some data to table
cursor.execute("INSERT INTO users (username,password) VALUES ('user01','password01');")
cursor.execute("INSERT INTO users (username,password) VALUES ('user02','password02');")
cursor.execute("INSERT INTO users (username,password) VALUES ('user03','password03');")
dbConnection.commit()

# perform login action
login_screen()

# end of program drop table
cursor.execute("DROP TABLE users;")
dbConnection.commit()
dbConnection.close()

    
