import pymysql.cursors

# Estabelecendo uma conexão com o banco de dados
con = pymysql.connect(
    host="localhost",
    user="root",
    password="bruno123",
    port=3306,
    db="aulapythonfull",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)
def criar_tabela(nome):
# criando um cursor como gerenciador de contexto
    try:
        with con.cursor() as cursor:
            cursor.execute(f"create table {nome} (nome varchar(50))")
            print('tabela criada com sucesso!')

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def remover_tabela(nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nome}")
            print('tabela removida com sucesso!')

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def inserir_valores(valor):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO teste values('{valor}')")
            # Confirmando a inserção no banco de dados
            con.commit()
            print('valor inserido com sucesso!')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def extrair_valores():
    try:
        with con.cursor() as cursor:
            cursor.execute(f"SELECT * FROM teste")
            # Confirmando a inserção no banco de dados
            con.commit()
            resultado=cursor.fetchall()
            print(resultado)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def atualizar_valores(valor_selecionado, novo_valor):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"UPDATE teste set nome = '{novo_valor}' WHERE nome = '{valor_selecionado}'")
            # Confirmando a inserção no banco de dados
            con.commit()
            print('valor atualizado com sucesso!')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def excluir_valor(valor):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DELETE FROM teste WHERE nome = '{valor}'")
            # Confirmando a inserção no banco de dados
            con.commit()
            print('valor removido com sucesso!')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")



# extrair_valores()
# inserir_valores('bruno')
# criar_tabela('teste2')
# remover_tabela('teste2')
# atualizar_valores('alyne', 'bruno')
excluir_valor('bruno')

con.close()