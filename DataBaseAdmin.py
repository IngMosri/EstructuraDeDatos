import sqlite3
import os

if os.path.exists("accounts.db"):
	conn = sqlite3.connect("accounts.db")
	c = conn.cursor()
else:
	conn = sqlite3.connect("accounts.db")
	c = conn.cursor()

	c.execute('''CREATE TABLE accounts
		(uname text, pwd text)''')

accOrLog = input("Enter 1 if you wanna add accounts, or 2 if you want to login: ")

if accOrLog == "1":
	uname = input("Enter account username to add: ")
	pwd = input("Enter account password to add: ")

	c.execute("INSERT INTO accounts VALUES (?, ?)", [uname, pwd])

	conn.commit()
	conn.close()

	print("Account added")

elif accOrLog == "2":
	uname = input("Enter username: ")
	pwd = input("Enter password: ")

	c.execute("SELECT * FROM accounts WHERE uname=? and pwd=?", [uname, pwd])
	
	if c.fetchone() == None:
		print("Incorrect credentials")
	else:
		print("Logged in!")

else:
	print("You have to enter 1 or 2")
