import MySQLdb as host

# defining our function states
database = None
try:
    # making connection to the localhost
    database = host.connect(host="localhost", port=3306, user=userr, password=passwrd, database=base)
    cursor = database.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)
    result = cursor.fetchall()

    # printing the results
    for i in result:
        print(i)
except host.Error as err:
    # printing an error message using erno to explain the type of error
        print(f"Error couldn't connect to localhost: {err}")
finally:
    # ending the database connection
    if database:
        database.close()
