#koneksi
#https://www.c-sharpcorner.com/UploadFile/75a48f/micro/

import pypyodbc as pyodbc

db_host = '.'
db_name = 'RestoDb'
#db_user = 'username'
#db_password = 'password'
connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';Integrated Security=SSPI'

def get_all_jenis():
    datajenis = []
    db = pyodbc.connect(connection_string)
    cursor = db.cursor()
    SQLCommand = ("select * from Jenis")
    cursor.execute(SQLCommand)
    results = cursor.fetchone()
    while results:
        datajenis.append({"JenisID":results[0],"NamaJenis":results[1]})
        results = cursor.fetchone()
    db.close()
    return datajenis