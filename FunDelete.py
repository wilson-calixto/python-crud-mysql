  

from FuncionarioTO import FuncionarioTO
from FuncionarioDAO import FuncionarioDAO


class FunDelete:

    def getDel(self):
        id = input("Digite o ID para delete: ")
        nasc = ''
        nome = ''
        foto = ''
        salario = ''

        f = FuncionarioTO(nome, nasc, salario, foto, id)
        d = FuncionarioDAO()
        d.delete(f)