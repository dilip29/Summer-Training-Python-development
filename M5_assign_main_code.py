import sqlite3
mystore=sqlite3.connect('bookstores.db')
mycursor=mystore.cursor()
total=0
while True:
    title=input("enter the title:")
    

    sql="select * from book where title='"+title+"';"
    x=mycursor.execute(sql)
    if x!=None:
        copies=int(input("enter the no. of copies"))
        mycursor.execute("select price from book where title='"+title+"';")
        price=mycursor.fetchone()
        print(price[0])
        total+=price[0]*copies
    else:
        print("searched book not found")
        
        
    inp=input("add more books y/n")
    if inp=='y':
        continue
    else:
        print("the total amt:",total)
        break


