import pypyodbc as pyodbc

db_host = '.'
db_name = 'RestoDb'
#db_user = 'username'
#db_password = 'password'

connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';Integrated Security=SSPI'
db = pyodbc.connect(connection_string)
cursor = db.cursor()

SQLCommand = ("select * from Jenis")
cursor.execute(SQLCommand)
results = cursor.fetchone()
while results:
    print("JenisID {}".format(results[0]))
    print("Nama Jenis :"+str(results[1]))
    results = cursor.fetchone()

db.close()