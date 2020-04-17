from dao import *

insertInfo = MacInfo('insert', '123', 1, 'test')
select = MacInfo('select', '123', 1, 'test', "SELECT * from ADDRESS_BOOK where MAC = '123'")
updateHostname = MacInfo('updateHostname', '123', 1, 'updated hostname')
updateWatch = MacInfo('updateWatch', '123', 0, 'test')
delete = MacInfo('delete', '123', 1, 'test')


dao(insertInfo)
dao(select)
dao(updateHostname)
dao(select)
dao(updateWatch)
dao(select)
dao(delete)
dao(select)