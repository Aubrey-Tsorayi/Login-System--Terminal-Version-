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