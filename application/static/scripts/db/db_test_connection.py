import psycopg2

def test_connection():

	print('Connecting to the PostgreSQL database...TESTING')
	# TEST db = simple_logger, schema = my_log, table = main

	# Establish a connection to the database
	conn = psycopg2.connect(
		host='localhost',
		port=5432,
		dbname='simple_logger',
		user='postgres',
		password='mysecretpassword'
	)

	# Create a cursor object
	cur = conn.cursor()
	print('Connected to the PostgreSQL database')

	# Execute a query:
	# To display the PostgreSQL 
	# database server version
	cur.execute('SELECT version()')
	print(cur.fetchone())



	cur.execute("SELECT schema_name FROM information_schema.schemata;")
	print("List of schemas in your database:")
	schemas = cur.fetchall()
	for schema in schemas:
		print(schema)


	cur.execute("""SELECT table_name FROM information_schema.tables
					WHERE table_schema = 'my_log'""")
	print("List of tables in schema my_log:")
	tables = cur.fetchall()
	for table in tables:
		print(table)

	# Execute a query
	cur.execute("select * from my_log.main;")

	# Fetch the results
	rows = cur.fetchall()
	print("Data from table my_log.main:")
	for row in rows:
		print(row)
	print("End of data from table my_log.main")

	# Close the cursor and connection
	cur.close()
	conn.close()
	print('Connection closed')

if __name__ == '__main__':
	test_connection()