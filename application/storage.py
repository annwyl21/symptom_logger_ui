import psycopg2
import json
from datetime import date, time

print('Connecting to the PostgreSQL database...')
# symptom_log is the name of both my database and the schema within it

# Establish a connection to the database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='simple_logger',
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
		# logger.error(f"Database Error: {e}")
		return f"Database Error: {e}"

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
		# logger.error(f"Database Error: {e}")
		return f"Database Error: {e}"

class Symptom_log:

	def add_a_symptom(date, time, pain_score, symptom):
		result = modify_db("INSERT INTO my_log.main(date, time, symptom, pain_score) VALUES(%s, %s, %s, %s)", (date, time, symptom, pain_score))

		return True if result == 'success' else False

	
	def get_all_symptoms():
		return query_db("SELECT * FROM my_log.main ORDER BY date DESC, time DESC")
	
	def create_symptom_list(data):
		json_output = Symptom_log.convert_to_json(data)
		# print(json_output)
		return json_output

	def convert_to_json(data):
		# Create a list of dictionaries from the data tuples
		result = [
			{
				"date": str(record[1]),  # Convert the date to a string
				"time": record[2].strftime("%H:%M"),  # Format the time as a string
				"pain_score": record[4],
				"description": record[3]
			} for record in data
		]
		# Convert the list of dictionaries to a JSON string
		json_data = json.dumps(result, indent=4)
		return json_data

if __name__ == '__main__':
	result = Symptom_log.get_all_symptoms()
	print(Symptom_log.create_symptom_list(result))
