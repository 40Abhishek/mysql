from mysql.connector import connect 
conn = connect( 
host="localhost", 
user="root", 
password="ADMIN", 
database="teacher" 
) 
cur = conn.cursor() 
cur.execute("create role if not exists 'student';") 
conn.commit() 
conn.close() 
print("role student created successfully")
