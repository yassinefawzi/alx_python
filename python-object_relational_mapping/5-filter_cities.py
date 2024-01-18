import MySQLdb as host
from sys import argv

# defining our function states
databe = None
try:
    # making connection to the localhost
    databe = host.connect(host="localhost", port=3306, user=argv[1], password=argv[2], database=argv[3])
    cursor = databe.cursor()
    query = query = '''SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id WHERE states.name = (SELECT id FROM states WHERE name = %s)
                ORDER BY cities.id ASC;
            '''
    cursor.execute(query, (argv[4],))
    result = cursor.fetchall()
        
    # printing the results
    for i in result:
        print(i[0])
except host.Error as err:
    # printing an error message using erno to explain the type   of error
    print(f"couldn't connect to localhost: {err}")
finally:
    # ending the database connection
    if databe:
        databe.close()