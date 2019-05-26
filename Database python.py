



import sqlite3

def DB():
    db=sqlite3.connect("information.db")
    db.row_factory=sqlite3.Row
    db.execute("create table if not exists Admin(Name text,age int)")
    db.execute("insert into Admin (Name,age) values (? , ?)",("Farid",23))
    db.execute("insert into Admin (Name,age) values (? , ?)",("mmm",1))
    db.commit()
    
    cusror=db.execute("select * from Admin")
    for row in cusror:
        print("Name:{}, Age:{}".format(row["Name"],row["age"]))




DB()
