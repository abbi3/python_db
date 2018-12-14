import cx_Oracle
con = cx_Oracle.Connection('user1/pswd1@127.0.0.1/orcl')
cur = cx_Oracle.Cursor(con)
list_of_Id=[100,102,103,104]
for id in list_of_Id:
    cur.execute("SELECT * FROM Computer where CompId=:c_id",{"c_id":id})
    for CompId,Make,Model,MYear in cur:
        print(Make,CompId)
cur.close()
con.close()
