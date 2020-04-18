import sqlite3

#assuming that macInfo has the following properties: 
# operation (which sql you want), mac (mac address), hostname, watch (1 or 0), statement( required only if op is select) 
class MacInfo(object):
    def __init__(self, operation, mac, hostname, watch, statement=None ):
      self.operation = operation
      self.mac = mac
      self.watch = watch
      self.hostname = hostname
      self.statement = statement

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
        select(database,macInfo.statement)
    elif macInfo.operation == "delete":
        delete(database,macInfo)
    else:
        print("ERROR: Invalid DAO operation")

    database.close()
    print("Closed database")


def insert(database, macInfo):
    sqlStr = "INSERT INTO ADDRESS_BOOK(MAC, WATCH, HOSTNAME) VALUES('{}', {}, '{}')".format(macInfo.mac, macInfo.watch, macInfo.hostname)
    print(sqlStr)
    database.execute(sqlStr)
    database.commit()
    print("inserted: '{}', {}, '{}' into ADDRESS_BOOK".format(macInfo.mac, macInfo.watch, macInfo.hostname))

def select(database, sqlString):
    results = database.execute(sqlString)
    print("Select Results: for query " + sqlString)
    for row in results:
        print(row)

def updateHostname(database, macInfo):
    sqlStr = "UPDATE ADDRESS_BOOK set HOSTNAME = '{}' where MAC = '{}'".format(macInfo.hostname,macInfo.mac)
    database.execute(sqlStr)
    database.commit()
    print("updated hostname: '{}', {}, '{}' in ADDRESS_BOOK".format(macInfo.mac, macInfo.watch, macInfo.hostname))

def updateWatch(database, macInfo):
    sqlStr = "UPDATE ADDRESS_BOOK set WATCH = {} where MAC = '{}'".format(macInfo.watch, macInfo.mac)
    database.execute(sqlStr)
    database.commit()
    print("updated watch status: '{}', {}, '{}' in ADDRESS_BOOK".format(macInfo.mac, macInfo.watch, macInfo.hostname))

def delete(database, macInfo):
    sqlStr = "DELETE from ADDRESS_BOOK where MAC = '{}'".format(macInfo.mac)
    database.execute(sqlStr)
    database.commit()
    print("deleted: MAC = '{}' from ADDRESS_BOOK".format(macInfo.mac))


def remove_prefix(message, prefix):
    if message.startswith(prefix):
        return message[len(prefix):]
    return message


def parsePacket(packet):
    packet = remove_prefix(packet,"**")
    print(packet)
    parsed = packet.split(",")
    cleaned = list(map(lambda x: x.strip(),parsed))
    nItems = len(cleaned)

    if nItems < 4 or nItems > 5:
        print("Invalid Packet length, see MacInfo class for details.")
        return None
    elif (cleaned[0] == "select" and nItems < 5):
        print("Invalid Select packet, see MacInfo class for details.")
        return None
    elif (cleaned[0] != "select" and nItems == 5):
        print("Invalid nonSelect packet, see MacInfo class for details.")
        return None
    elif nItems == 4:
        return MacInfo(cleaned[0], cleaned[1], cleaned[2], cleaned[3])
    elif nItems == 5:
        return MacInfo(cleaned[0], cleaned[1], cleaned[2], cleaned[3], cleaned[4])
    







