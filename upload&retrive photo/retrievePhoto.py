import mysql.connector

# this class will retrieve image from database
# and write it on the local machine
def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file_holder:
        file_holder.write(data)

def readBLOB(emp_id, filename):
    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='cs411_project',
                                             user='root',
                                             password='12345678',
                                             use_pure=True)
        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT photo from Python_upload_Photo where id = %s"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        print("Query executed")
        photo = cursor.fetchone()[-1]

        # write blob data into a file
        write_file(photo, filename)


    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

readBLOB("6rqhFgbbKwnb9MLmUQDhG6", "/Users/yuhao/Desktop/CS411/test/graph.jpg")
