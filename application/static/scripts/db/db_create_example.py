import psycopg2

# One-time use script to create an example

print('Connecting to the PostgreSQL database...TESTING')
# Establish a connection to the database
conn = psycopg2.connect(
	host='localhost',
	port=5432,
	dbname='simple_logger',
	user='postgres',
	password='mysecretpassword'
)

# Create cursor object
dbcon = conn
dbCursor = conn.cursor()
print('Connected to the PostgreSQL database')

def query_db(query, args=(), one=False):
	try:
		dbCursor.execute(query, args) # args helps prevent SQLinjection
		results = dbCursor.fetchall() # setting one to True will return only the first result, making single returns easier to handle
		
		return (results[0] if results else None) if one else results
	except Exception as e:
		# logger.error(f"Database Error: {e}")
		return f"Database Error: {e}"

def modify_db(statement, args=()):
	try:
		dbCursor.execute(statement, args)
		dbcon.commit()

		return 'success'
	except Exception as e:
		# logger.error(f"Database Error: {e}")
		return f"Database Error: {e}"

def add_a_symptom(date, time, pain_score, symptom):
	# print("INSERT INTO my_log.main(date, time, symptom, pain_score) VALUES(?, ?, ?, ?)", (date, time, symptom, pain_score))
	print(modify_db("INSERT INTO my_log.main(date, time, symptom, pain_score) VALUES(%s, %s, %s, %s)", (date, time, symptom, pain_score)))

	return True

# Even though %s looks like a string formatting operator in Python, when used in SQL statements with psycopg2, it is treated as a placeholder for a parameter, and psycopg2 will safely interpolate the parameters into the SQL query to prevent SQL injection attacks.

# json
example_log = [
	# {"date":"2023-10-01","time":"20:49","pain_score":1,"description":"Slight discomfort in right hip"},
	{"date":"2023-10-03","time":"14:07","pain_score":2,"description":"right hip feels stiff to move, difficulty standing for long periods"},
	{"date":"2023-10-05","time":"07:23","pain_score":3,"description":"Noticeable pain in right hip, especially when climbing stairs."},
	{"date":"2023-10-07","time":"19:21","pain_score":4,"description":"Pain in right hip while sitting"},
	{"date":"2023-10-09","time":"19:56","pain_score":5,"description":"Moderate pain in the right hip, difficulty turning in bed."},
	{"date":"2023-10-11","time":"14:12","pain_score":6,"description":"Sharp pain in right hip while climbing stairs."},
	{"date":"2023-10-13","time":"07:36","pain_score":7,"description":"Intense pain in right hip on waking, maybe I slept on my hip."},
	{"date":"2023-10-15","time":"07:10","pain_score":8,"description":"Hard to get out of bed today, right hip really bothering me"},
	{"date":"2023-10-17","time":"09:30","pain_score":9,"description":"Pain in right hip after walking."},
	{"date":"2023-10-19","time":"09:36","pain_score":10,"description":"Right hip really hurts today, walking is really slow and laboured"},
	{"date":"2023-10-21","time":"16:53","pain_score":10,"description":"Right hip feels really painful, can hardly get up the stairs"},
	{"date":"2023-10-23","time":"07:55","pain_score":10,"description":"Right hip feels very painful after sleeping on it."}
]

for symptom in example_log:
	add_a_symptom(symptom['date'], symptom['time'], symptom['pain_score'], symptom['description'])

print(query_db("SELECT * FROM my_log.main;"))

dbCursor.close()
dbcon.close()
