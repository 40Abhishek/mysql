from mysql.connector import connect 
conn = connect( 
host="localhost", 
user="root", 
password="ADMIN", 
database="teacher" 
) 
cur = conn.cursor() 
cur.execute(""" 
create view dept_sal as select dept_name,sum(salary) as sal_total from 
instructor group by dept_name; 
""") 
conn.commit() 
conn.close() 
print("dept_sal view created successfully") 
