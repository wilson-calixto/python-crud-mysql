  

from FunInsert import FunInsert
from FunDelete import FunDelete
from FunUpdate import FunUpdate
from FunList import FunList


class Main:

    fins = FunInsert()

    fdel = FunDelete()

    fupd = FunUpdate()

    flist = FunList()

    fins.getIns()

    flist.getList()