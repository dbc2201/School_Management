class DatabaseConnection:
    import mysql.connector as mc
    conn = mc.connect(host="localhost", user="root", passwd="", database="Management")
    cur = conn.cursor()
    # you could use try-catch here
    if cur:
        print("Connected Successfully!")
    else:
        print("Connection failed!")
