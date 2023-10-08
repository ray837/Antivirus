import mysql.connector
#db

def database(s):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Rayid",
        database = "virus"
    )
    mycursor=mydb.cursor()
    s=(s,)
    sql="SELECT * FROM db WHERE Virus_name= %s "
    mycursor.execute(sql,s)
    global myresult
    myresult=mycursor.fetchone()
    if myresult!=None:
        print(myresult)
        return 1
    else:
        #print("not found in database")
        return 0

