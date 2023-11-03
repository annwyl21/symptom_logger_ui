import psycopg2

print('Connecting to the PostgreSQL database...')
# symptom_log is the name of both my database and the schema within it

# Establish a connection to the database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='symptom_log',
    user='postgres',
    password='mysecretpassword'
)

print('Connected to the PostgreSQL database')

#query & commit function to create clean code &  prevent SQL injection
def query_db(query, args=(), one=False):
	try:
		dbcon = conn
		dbCursor = conn.cursor()
		dbCursor.execute(query, args) # args helps prevent SQLinjection
		results = dbCursor.fetchall() # setting one to True will return only the first result, making single returns easier to handle
		dbCursor.close()
		dbcon.close()
		return (results[0] if results else None) if one else results
	except Exception as e:
		# logger.error("Database Error: DB Read Failed")
		return 'error'

def modify_db(statement, args=()):
	try:
		dbcon = conn
		dbCursor = conn.cursor()
		dbCursor.execute(statement, args)
		dbcon.commit()
		dbCursor.close()
		dbcon.close()
		return 'success'
	except Exception as e:
		# logger.error("Database Error: DB Modify Failed")
		return 'error'

class Symptom_log:

	def add_a_symptom(date, time, pain_score, symptom):
		modify_db("INSERT INTO logger.symptom_collection(date, time, pain_score, symptom) VALUES(?, ?, ?, ?)", (date, time, pain_score, symptom))

		return True
	
