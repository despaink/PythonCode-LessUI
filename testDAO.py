from dao import *

insertInfo = MacInfo('insert', '123', 'test',1)
select = MacInfo('select', '123', 'test',1, "SELECT * from ADDRESS_BOOK where MAC = '123'")
updateHostname = MacInfo('updateHostname', '123', 'updated hostname',1)
updateWatch = MacInfo('updateWatch', '123', 'test',0)
delete = MacInfo('delete', '123', 'test',1)


dao(insertInfo)
dao(select)
dao(updateHostname)
dao(select)
dao(updateWatch)
dao(select)
dao(delete)
dao(select)