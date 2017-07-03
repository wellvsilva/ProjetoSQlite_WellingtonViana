import sqlite3

class BancoDeDados:
    """Classe que representa o  banco de dados(database) da aplicação"""

    def __init__(self, nome='banco.db'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        """Conecta passando o nome do arquivo"""
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        """Desconecta do banco de dados"""
        try:
            self.conexao.close()
        except AttributeError:
            pass

    def criar_tabelas(self):
        """Cria as tabelas do banco"""
        try:
            cursor = self.conexao.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS clientes ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome MESSAGE_TEXT NOT NULL, cpf VARCHAR(11) UNIQUE  NOT NULL, email MESSAGE_TEXT NOT NULL );")
        except AttributeError:
            print('Faça a conexão do banco antes de criar as tabelas.')

    def inserir_cliente(self, nome, cpf, email):
        """Insere cliente no banco de dados"""
        try:
            try:
                cursor = self.conexao.cursor()

                cursor.execute("INSERT INTO clientes(nome, cpf, email) VALUES (?,?,?)", (nome, cpf, email))
            except sqlite3.IntegrityError:
                print('O cpf %s já existe!' % cpf)

            self.conexao.commit()
        except AttributeError:
            print('Faça a conexão do banco de dados antes de inserir clientes.')

    def buscar_cliente(self, cpf):
        """Busca um cliente por cpf"""
        try:
            cursor = self.conexao.cursor()

            # Obtém todos os dados
            cursor.execute("SELECT * FROM clientes;")
            for linha in cursor.fetchall():
                if linha[2] == cpf:
                    print("Cliente %s encontrado." % linha[1])
                    break
        except AttributeError:
            print("Faça a conexão com o banco de dados antes de buscar clientes!")

    def remover_cliente(self, cpf):
        """Removendo cliente pelo cpf"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(" DELETE FROM clientes WHERE cpf = cpf;")
            self.conexao.commit()
        except AttributeError:
            print('Faça a conexão do banco de dados antes de inserir clientes.')


        #self.conexao.commit()

    def buscar_email(self, email):
        """Buscar cleinte por email"""
        try:
            cursor = self.conexao.cursor()

            #obter primeiramente todos os dados
            cursor.execute("SELECT * FROM clientes;")
            for linha in cursor.fetchall():
                if linha[3] == email:
                    print(True)
                    break
                else:
                    print(False)
                    break
        except AttributeError:
            print("Faça a conexão com o banco de dados antes de buscar pelo email do cliente!")

