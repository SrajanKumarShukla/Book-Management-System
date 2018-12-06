import sqlite3 as sql
conn=sql.connect('record.db')
c=conn.cursor()
#c.execute('create table userdetail(name text,address text,gender text,mobile real,email text,password text)')
for row in c.execute('select * from book'):
    print(row)
conn.commit()
conn.close()