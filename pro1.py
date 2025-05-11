from mysql.connector import connect

conn = connect(
    host="localhost",
    user="root",
    password="ADMIN",
    database="teacher"
)

cur = conn.cursor()

cur.execute("""
    CREATE VIEW faculty AS
    SELECT id, name, dept_name FROM instructor;
""")

conn.commit()
conn.close()
print("faculty view created successfully")
