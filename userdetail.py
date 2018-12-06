import sqlite3 as sql
conn=sql.connect('user.db')
c=conn.cursor()
#c.execute('create table userdetail(name text,address text,gender text,mobile real,email text,password text)')
x=('srajan',)
y=''
for row in c.execute('select name from user'):
    print(type(row))
    print(row)
    if(row==x):
        print(row)
#c.execute('delete from userdetail')
conn.commit()
conn.close()