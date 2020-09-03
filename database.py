import sqlite3

"""con = sqlite3.connect('users.db')
c = con.cursor()
c.execute('''CREATE TABLE info (
	username text,
	password text
)''')
print('Done!')
con.commit()
con.close() """

#add a new user
def add_user(username,password):
	con = sqlite3.connect('users.db')
	c = con.cursor()
	info = [(username),(password)]
	c.execute("INSERT INTO info VALUES (?,?)",info)
	con.commit()
	con.close()

#login user
def login():
	while True:
		username = input("Enter username: ")
		password = input("Enter password: ")
		with sqlite3.connect("users.db") as db:
				c = db.cursor()
		finduser = ("SELECT * FROM info WHERE username = ? AND password = ?")
		c.execute(finduser,[(username),(password)])
		results = c.fetchall()

		if results:
			for i in results:
				print("Welcome " + i[0].upper())
			return("exit")
			break

		else:
			print("Username and password incorrect")
			again = input("Do you with to try again? (y/n): ")
			if again.lower() == "n":
				print("Goodbye")
				time.sleep(1)
			break

print("Done")