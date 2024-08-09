import mysql.connector

conexao = mysql.connector.connect(host="localhost",
                                  database = 'puromilho',
                                  user = 'root',
                                  password = '')

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

#print(retornoSelect)



conexao.close()
cursor.close()