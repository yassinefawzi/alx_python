import MySQLdb as host

# defining our function states
def states(userr, passwrd, data, name_searched):
    databe = None
    try:
        # making connection to the localhost
        databe = host.connect(host="localhost", port=3306, user=userr, password=passwrd, database=data)
        cursor = databe.cursor()
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(name_searched)
        cursor.execute(query)
        result = cursor.fetchall()
        
        # printing the results
        for i in result:
            print(i)
    except host.Error as err:
        # printing an error message using erno to explain the type of error
        print(f"couldn't connect to localhost: {err}")
    finally:
        # ending the database connection
        if databe:
            databe.close()
