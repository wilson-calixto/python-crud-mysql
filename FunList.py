  

from FuncionarioDAO import FuncionarioDAO

class FunList:

    def getList(self):
        d = FuncionarioDAO()
        d.list()