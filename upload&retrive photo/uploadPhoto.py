import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(emp_id, name, photo):
    print("Inserting BLOB into Python_upload_Photo table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='cs411_project',
                                             user='root',
                                             password='12345678',
                                             use_pure=True)

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO Python_upload_Photo
                          (id, name, photo) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image inserted successfully as a BLOB into Python_upload_Photo table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB("6rqhFgbbKwnb9MLmUQDhG6", "Eric", "/Users/yuhao/Desktop/yuhao.jpg")
