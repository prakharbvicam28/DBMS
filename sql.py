import mysql.connector as myc
def connect():
    conn=myc.connect(
        host="localhost",
        user='root',
        password='bvicam',
        db='prakhar'
    )
    if conn.is_connected():
        return [True,conn]
rel=connect()
if rel[0]:
    cur=rel[1].cursor()

def fetch_table():
    query="select*from MCA_SecA"
    cur.execute(query)
    rec=cur.fetchall()
    for i in rec:
        print(i)

fetch_table()
