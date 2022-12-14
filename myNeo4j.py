from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable


class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    ##### FUNÇÕES DO USUÁRIO #####
    # CREATE:
    def createUser(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createUser)

    @staticmethod
    def _createUser(db):
        print("\nCriação do Usuário")

        query = (
            "CREATE (object:user { nome: $nome_user, cpf: $cpf_user, email: $email_user, rua: $rua_user, numero: $numero_user, bairro: $bairro_user, cidade: $cidade_user, estado: $estado_user, país: $pais_user })"
        )

        nome_user = input("Insira o nome do usuário: ")
        email_user = input("Insira o email do usuário: ")
        cpf_user = input("Insira o cpf do usuário: ")
        rua_user = input("Insira a rua do usuário: ")
        numero_user = input("Insira o número: ")
        bairro_user = input("Insira o bairro: ")
        cidade_user = input("Insira a cidade: ")
        estado_user = input("Insira o estado: ")
        pais_user = input("Insira o país: ")

        result = db.run(query,
                        nome_user=nome_user,
                        email_user=email_user,
                        cpf_user=cpf_user,
                        rua_user=rua_user,
                        numero_user=numero_user,
                        bairro_user=bairro_user,
                        cidade_user=cidade_user,
                        estado_user=estado_user,
                        pais_user=pais_user
                        )

        return [{"object": row["object"]["nome"]["email"]["cpf"]["rua"]["numero"]["bairro"]["cidade"]["estado"]["pais"]}
                for row in result]

    # FIND
    def findUsers(self):
        with self.driver.session(database="neo4j") as session:
            session.find_transaction(self._findUsers)

    @staticmethod
    def _findUsers(db):
        print("\nEncontrar todos os Usuários")

        query = "MATCH (u:user) RETURN u"

        result = db.run(query)

        return [print([row]) for row in result]

    def findUser(self):
        with self.driver.session(database="neo4j") as session:
            session.find_transaction(self._findUser)

    @staticmethod
    def _findUser(db):
        print("\nEncontrar Usuario pelo Documento")

        cpf_user = input("Insira o numero do documento do Usuário: ")

        query = "MATCH (u:user) WHERE u.cpf = $cpf_user RETURN u"

        result = db.run(query,
                        cpf_user=cpf_user
                        )

        return [print([row]) for row in result]

    # UPDATE
    def updateUser(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updateUser)

    @staticmethod
    def _updateUser(db):
        print("\nAtualizar Usuário")

        cpf_user = input("Insira o numero do documento do Usuário: ")

        print('''\nSelecione o que deseja atualizar\n
                1 - Nome
                2 - Email
                3 - CPF
                4 - Rua
                5 - Numero
                6 - Bairro
                7 - Cidade
                8 - Estado
                9 - País
            ''')

        option = input("Insira o número da opção: ")

        while int(option) < 1 or int(option) > 7:
            print("Opção inválida.")
            option = input("Insira o número da opção: ")

        if option == "1":
            option = "nome"
        elif option == "2":
            option = "email"
        elif option == "3":
            option = "cpf"
        elif option == "4":
            option = "rua"
        elif option == "5":
            option = "numero"
        elif option == "6":
            option = "bairro"
        elif option == "7":
            option = "cidade"
        elif option == "8":
            option = "estado"
        elif option == "9":
            option = "pais"

        new_value = input("Insira o novo documento: ")

        query = (
            "MATCH (u:user) WHERE u.cpf = $cpf_user SET u." +
            option + " = $new_value"
        )

        db.run(query,
               cpf_user=cpf_user,
               option=option,
               new_value=new_value
               )

    # DELETE
    def deleteUser(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._deleteUser)

    @staticmethod
    def _deleteUser(db):
        print("\nDeletar Usuário")

        cpf_user = input("Insira o número do documento: ")

        query = "MATCH (u:user) WHERE u.cpf = $cpf_user DETACH DELETE u"

        db.run(query, cpf_user=cpf_user)

    ##### FUNÇÕES DO VENDEDOR #####
    # CREATE:

    def createVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createVendedor)

    @staticmethod
    def _createVendedor(db):
        print("\nCriação do Vendedor")

        query = (
            "CREATE (object:vendedor { nome: $nome_vendedor, cpf: $cpf_vendedor, email: $email_vendedor, $telefone_vendedor, rua: $rua_vendedor, numero: $numero_vendedor, bairro: $bairro_vendedor, cidade: $cidade_vendedor, estado: $estado_vendedor, país: $pais_vendedor })"
        )

        nome_vendedor = input("Insira o nome do vendedor: ")
        email_vendedor = input("Insira o email do usuário: ")
        cpf_vendedor = input("Insira o cpf do usuário: ")
        telefone_vendedor = input("Insira o telefone do vendedor: ")
        rua_vendedor = input("Insira a rua do usuário: ")
        numero_vendedor = input("Insira o número: ")
        bairro_vendedor = input("Insira o bairro: ")
        cidade_vendedor = input("Insira a cidade: ")
        estado_vendedor = input("Insira o estado: ")
        pais_vendedor = input("Insira o país: ")

        result = db.run(query,
                        nome_vendedor=nome_vendedor,
                        email_vendedor=email_vendedor,
                        telefone_vendedor=telefone_vendedor,
                        cpf_vendedor=cpf_vendedor,
                        rua_vendedor=rua_vendedor,
                        numero_vendedor=numero_vendedor,
                        bairro_vendedor=bairro_vendedor,
                        cidade_vendedor=cidade_vendedor,
                        estado_vendedor=estado_vendedor,
                        pais_vendedor=pais_vendedor
                        )

        return [{"object": row["object"]["nome"]["email"]["telefone"]["cpf"]["rua"]["numero"]["bairro"]["cidade"]["estado"]["pais"]}
                for row in result]

    # FIND
    def findVendedores(self):
        with self.driver.session(database="neo4j") as session:
            session.find_transaction(self._findVendedores)

    @staticmethod
    def _findVendedores(db):
        print("\nEncontrar todos os Vendedores")

        query = "MATCH (u:vendedor) RETURN u"

        result = db.run(query)

        return [print([row]) for row in result]

    def findVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.find_transaction(self._findVendedor)

    @staticmethod
    def _findVendedor(db):
        print("\nEncontrar o Vendedor pelo Email")

        email_vendedor = input("Insira o email do Vendedor: ")

        query = "MATCH (u:vendedor) WHERE u.email = $email_vendedor RETURN u"

        result = db.run(query,
                        email_vendedor=email_vendedor
                        )

        return [print([row]) for row in result]

    # UPDATE
    def updateVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updateUser)

    @staticmethod
    def _updateUser(db):
        print("\nAtualizar Vendedor")

        email_vendedor = input("Insira o email do Vendedor: ")

        print('''\nSelecione o que deseja atualizar\n
                1 - Nome
                2 - Email
                3 - Telefone
                4 - CPF
                5 - Rua
                6 - Numero
                7 - Bairro
                8 - Cidade
                9 - Estado
                10 - País
            ''')

        option = input("Insira o número da opção: ")

        while int(option) < 1 or int(option) > 7:
            print("Opção inválida.")
            option = input("Insira o número da opção: ")

        if option == "1":
            option = "nome"
        elif option == "2":
            option = "email"
        elif option == "3":
            option = "cpf"
        elif option == "4":
            option = "telefone"
        elif option == "5":
            option = "rua"
        elif option == "6":
            option = "numero"
        elif option == "7":
            option = "bairro"
        elif option == "8":
            option = "cidade"
        elif option == "9":
            option = "estado"
        elif option == "10":
            option = "pais"

        new_value = input("Insira o novo email: ")

        query = (
            "MATCH (u:vendedor) WHERE u.email = $email_vendedor SET u." +
            option + " = $new_value"
        )

        db.run(query,
               email_vendedor=email_vendedor,
               option=option,
               new_value=new_value
               )

    # DELETE
    def deleteVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._deleteVendedor)

    @staticmethod
    def _deleteVendedor(db):
        print("\nDeletar Vendedor")

        email_vendedor = input("Insira o email: ")

        query = "MATCH (u:vendedor) WHERE u.email = $email_vendedor DETACH DELETE u"

        db.run(query, email_vendedor=email_vendedor)

    ##### FUNÇÕES DE PRODUTO #####
    # CREATE
    def createProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self.createProduto)

    @staticmethod
    def _createProduto(db):
        print("\nCriação de Produto")

        query = (
            "CREATE (object:product { nome: $nome_produto, preco: $preco_produto, quantidade: $quantidade_produto, $emailVendedor: $email_vendedor })"
        )

        nome_produto = input("Insira o nome do produto: ")
        preco_produto = input("Insira o preço: ")
        quantidade_produto = input("Insira a quantidade do produto: ")
        email_vendedor = input("Insira o email do Vendedor: ")

        result = db.run(query,
                        nome_produto=nome_produto,
                        preco_produto=preco_produto,
                        quantidade_produto=quantidade_produto,
                        email_vendedor=email_vendedor
                        )

        return [{"object": row["object"]["nome"]["preco"]["quantidade"]["emailVendedor"]}
                for row in result]

     # FIND
    def findProdutos(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._findProdutos)

    @staticmethod
    def _findProdutos(db):
        print("\nEncontrar todos os Produtos")

        query = "MATCH (p:product) RETURN p"

        result = db.run(query)

        return [print([row]) for row in result]

    def findProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._findProduto)

    @staticmethod
    def _findProduto(db):
        print("\nEncontrar o Produto pelo Nome")

        nome_produto = input("Insira o nome do Produto: ")

        query = "MATCH (p:product) WHERE p.nome = $nome_produto RETURN p"

        result = db.run(query,
                        nome_produto=nome_produto
                        )

        return [print([row]) for row in result]

    # UPDATE
    def updateProduct(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updateProduct)

    @staticmethod
    def _updateProduct(db):
        print("\nAtualizar Produto")

        nome_produto = input("Insira o nome do Produto: ")

        print('''\nSelecione o que deseja atualizar\n
                1 - Nome
                2 - Preço
                3 - Quantidade
            ''')

        option = input("Insira o número da opção: ")

        while int(option) < 1 or int(option) > 4:
            print("Opção Inválida")
            option = input("Insira o número da opção: ")

        if option == "1":
            option = "nome"
        elif option == "2":
            option = "preco"
        elif option == "3":
            option = "quantidade"

        new_value = input("Insira o novo nome do Produto: ")

        query = (
            "MATCH (p:produto) WHERE p.nome = $nome_produto SET p." +
            option + " = $new_value"
        )

        db.run(query,
               nome_produto=nome_produto,
               option=option,
               new_value=new_value
               )

    # DELETE
    def deleteProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._deleteProduto)

    @staticmethod
    def deleteProduto(db):
        print("\nDeletar Produto")

        nome_produto = input("Insira o nome do Produto: ")

        query = "MATCH (p:produto) WHERE p.nome = $nome_produto DETACH DELETE p"

        db.run(query, nome_produto=nome_produto)

    ###### RELAÇÃO DAS FUNÇÕES ######
    # Vendedor com Produto
    def vendProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._vendProduto)

    @staticmethod
    def vendProduto(db):
        vendedor_email = input("Insert the vendor's document number: ")
        nome_produto = input("Insert the product's name: ")

        query = (
            "MATCH (v:vendedor) WHERE v.email = $vendedor_email MATCH (p:produto) WHERE p.nome = $nome_produto CREATE (p)-[:VENDE]->(v) RETURN p, v")

        result = db.run(query,
                        vendedor_email=vendedor_email,
                        nome_produto=nome_produto
                        )

        return [{"p": row["p"]["nome"], "v": row["v"]["email"]} for row in result]

    # Usuario com Produto
    def userProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._userProduto)

    @staticmethod
    def _userProduto(db):
        cpf_user = input("Insira o cpf do usuário: ")
        nome_produto = input("Insira o nome do produto: ")

        query = (
            "MATCH (u:user) WHERE u.cpf = $cpf_user MATCH (p:produto) WHERE p.nome = $nome_produto CREATE (u)-[:COMPRA]->(p) RETURN p, u")

        result = db.run(query,
                        cpf_user=cpf_user,
                        nome_produto=nome_produto
                        )

        return [{"p": row["p"]["nome"], "u": row["u"]["cpf"]} for row in result]


if __name__ == "__main__":
    uri = "neo4j+s://b17f719c.databases.neo4j.io"
    user = 'neo4j'
    password = '5I7bQHWofOK7SGWJr69jM1rizMCAxCdg8k0zn4LLJvA'
    app = app.create_user(uri, user, password)
