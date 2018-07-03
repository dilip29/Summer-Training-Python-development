import sqlite3
mystore=sqlite3.connect('bookstores.db')
mycursor=mystore.cursor()
sql=''' create table book (id integer primary key not null,title text(20),
author text(20),price real);'''
mycursor.execute(sql)

sql='''insert into book
values(1,'think java','rhooney',550.0);'''
mycursor.execute(sql)
mystore.commit()

sql='''insert into book
values(2,'think python','allen',450.0);'''
mycursor.execute(sql)
mystore.commit()

sql='''insert into book
values(3,'think c++','booty',375.0);'''
mycursor.execute(sql)
mystore.commit()

mystore.close()



