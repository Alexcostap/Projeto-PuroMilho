import mysql.connector
def conectar():
    conexao = mysql.connector.connect(host="localhost",
                                    database = 'puromilho',
                                    user = 'root',
                                    password = '')
    return conexao
conexao = conectar()
if conexao.is_connected():
    print("Conexão realizada com sucesso")
    cursor = conexao.cursor()
else:
    print('Não conectou')

# inserir = """INSERT INTO 
#             `vendedor` (`nomeVendedor`) 
#             VALUES ('Arielle Lima')"""
# cursor.execute(inserir)
# conexao.commit()
# select = """select * from vendedor"""
# cursor.execute(select)
# retornoSelect = cursor.fetchall()[0]

# def cadastroPreco(vlrMilho,vlrCanjicaPequena,vlrCanjicaGrande,
#                   vlrPamonha,vlrBoloMilho,vlrBoloMacaxeira,vlrPeDeMoleque):
#     inserir = f"""UPDATE `valores` SET `vlrMilho` = '{vlrMilho}', 
#             `vlrCanjicaPequena` = '{vlrCanjicaPequena}', 
#             `vlrCanjicaGrande` = '{vlrCanjicaGrande}', 
#             `vlrPamonha` = '{vlrPamonha}', 
#             `vlrBoloMilho` = '{vlrBoloMilho}', 
#             `vlrBoloMacaxeira` = '{vlrBoloMacaxeira}', 
#             `vlrPeDeMoleque` = '{vlrPeDeMoleque}' 
#              WHERE `valores`.`id` = 1"""
#     cursor.execute(inserir)
#     conexao.commit()
#     print ("Alteração realizada com sucesso!!!")

# vlrMilho = float(input("Informe o valor do MILHO COZIDO: "))
# vlrCanjicaPequena = float(input("Informe o valor do CANJICA PEQUENA: "))
# vlrCanjicaGrande = float(input("Informe o valor do CANJICA GRANDE: "))
# vlrPamonha = float(input("Informe o valor do PAMONHA: "))
# vlrBoloMilho = float(input("Informe o valor do BOLO DE MILHO: "))
# vlrBoloMacaxeira = float(input("Informe o valor do BOLO DE MACAXEIRA: "))
# vlrPeDeMoleque = float(input("Informe o valor do PÉ DE MOLEQUE: "))


# alterarPreco = cadastroPreco(vlrMilho,vlrCanjicaPequena,vlrCanjicaGrande,
#                   vlrPamonha,vlrBoloMilho,vlrBoloMacaxeira,vlrPeDeMoleque)

# print(alterarPreco)

conexao.close()
cursor.close()