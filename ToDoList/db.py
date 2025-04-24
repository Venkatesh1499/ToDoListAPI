import sqlite3

def get_connection():
	conn = sqlite3.connect('tasks.db')
	conn.row_factory = sqlite3.Row
	return conn

#connecting to db naemd tasks.db
conn = sqlite3.connect('tasks.db')

#creating cursor to modify the db
cursor = conn.cursor()

#creating table if not there
cursor.execute('''
	CREATE TABLE IF NOT EXISTS Tasks (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		task TEXT NOT NULL,
		is_done BOOLEAN NOT NULL
	)
''')

#Added new column day in the table Tasks
# cursor.execute('ALTER TABLE Tasks ADD COLUMN day TEXT NOT NULL')

#commiting the changes
conn.commit()

#closing the connection
conn.close()
