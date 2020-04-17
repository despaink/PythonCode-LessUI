import sqlite3


def insert(database, macInfo):
    database.execute("INSERT INTO ADDRESS_BOOK(MAC, WATCH, HOSTNAME) VALUES('123', 1, 'test')")
    database.commit()
    print("inserted: ", macInfo)

def select(database, sqlString):
    results = database.execute("SELECT * from ADDRESS_BOOK")
    for row in results:
        print(row)

def updateHostname(database, macInfo):
    database.execute("UPDATE ADDRESS_BOOK set HOSTNAME = 'update' where MAC = '123'")
    database.commit()
    print("updated: ", macInfo)

def updateWatch(database, macInfo):
    database.execute("UPDATE ADDRESS_BOOK set WATCH = 0 where MAC = '123'")
    database.commit()
    print("updated: ", macInfo)

def delete(database, macInfo):
    database.execute("DELETE from ADDRESS_BOOK where MAC = '123'")
    database.commit()
    print("deleted: ", macInfo)

#assuming that macInfo has the following properties: operation (which sql you want), mac_addr (mac address), hostname, watch (true/false), statement(only if op is select) 
def dao(macInfo):
    database = sqlite3.connect('lessDB')
    print ("Opened database successfully")

    if not hasattr(macInfo,'operation'):
        print("ERROR: Missing macInfo.operation")
    elif macInfo.operation == "insert":
        insert(database,macInfo)
    elif macInfo.operation == "updateHostname":
        updateHostname(database,macInfo)
    elif macInfo.operation == "updateWatch":
        updateWatch(database,macInfo)
    elif macInfo.operation == "select":
        select(database,macInfo)
    elif macInfo.operation == "delete":
        delete(database,macInfo)
    else:
        print("ERROR: Invalid DAO operation")

    database.close()
    print("Closed database")



