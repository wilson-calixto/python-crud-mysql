  



import pymysql



class FuncionarioDAO:

    def conect(self):
        db = pymysql.connect("localhost", "root", "1@asdfg", "projeto")
        return db

    def insert(self, FuncionarioTO):
        db = self.conect()
        cursor = db.cursor()

        sql = "INSERT INTO funcionario (nome, nasc, salario, foto) VALUES ('"
        sql += str(FuncionarioTO.getNome())
        sql += "','"
        sql += str(FuncionarioTO.getNasc())
        sql += "','"
        sql += str(FuncionarioTO.getSalario())
        sql += "','"
        sql += str(FuncionarioTO.getFoto())
        sql += ".jpeg');"

        print(sql)  # imprimir o SQL para visualizar e verificar se tem erros
        print(type(sql))  # ver se é string

        cursor.execute(sql)
        db.commit()
        db.close()

    def list(self):
        db = self.conect()
        cursor = db.cursor()

        sql = "SELECT * FROM funcionario;"

        cursor.execute(sql)
        for row in cursor:
            print(row)

    def delete(self, FuncionarioTO):
        db = self.conect()
        cursor = db.cursor()

        sql = "DELETE from funcionario WHERE id="
        sql += str(FuncionarioTO.getId())
        sql += ";"

        print(sql)  # imprimir o SQL para visualizar e verificar se tem erros
        print(type(sql))  # ver se é string

        cursor.execute(sql)
        db.commit()
        db.close()

    def update(self, FuncionarioTO):
        db = self.conect()
        cursor = db.cursor()

        sql = "UPDATE funcionario SET "
        sql += "nome ='"
        sql += str(FuncionarioTO.getNome())
        sql += "', nasc='"
        sql += str(FuncionarioTO.getNasc())
        sql += "', salario='"
        sql += str(FuncionarioTO.getSalario())
        sql += "',foto='"
        sql += str(FuncionarioTO.getFoto())
        sql += "'"

        sql += " WHERE id="
        sql += str(FuncionarioTO.getId())
        sql += ";"

        print(sql)  # imprimir o SQL para visualizar e verificar se tem erros
        print(type(sql))  # ver se é string
        cursor.execute(sql)
        db.commit()
        db.close()