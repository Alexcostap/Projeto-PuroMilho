import mysql.connector
def conectar():
    conexao = mysql.connector.connect(host="localhost",
                                    database = 'puromilho',
                                    user = 'root',
                                    password = '')
    return conexao
conexao = conectar()
cursor = conexao.cursor()
if conexao.is_connected():
    print("Conexão realizada com sucesso")

else:
    print('Não conectou')


conexao.close()
cursor.close()