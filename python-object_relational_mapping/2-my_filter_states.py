import MySQLdb as host
from sys import argv

# defining our function states
databe = None
try:
    # making connection to the localhost
    databe = host.connect(host="localhost", port=3306, user=argv[1], password=argv[2], database=argv[3])
    cursor = databe.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(argv[4])
    cursor.execute(query)
    result = cursor.fetchall()

    # printing the results
    for i in result:
        if i[1][0] >= 'A' and i[1][0] <= 'Z':
            print(i)
except host.Error as err:
    # printing an error message using erno to explain the type of error
    print(f"couldn't connect to localhost: {err}")
finally:
    # ending the database connection
    if databe:
        databe.close()
