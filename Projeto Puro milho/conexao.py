import sqlite3
def conectar():
    #Conexão com o banco
    conexao = sqlite3.connect('puromilho.db')
    #Cursor para executar comandos
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS retorno (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `nomeVendedor` varchar(40) NOT NULL,
    `qtdMilho` int(3) NOT NULL,
    `qtdCanjicaPequena` int(3) NOT NULL,
    `qtdCanjicaGrande` int(3) NOT NULL,
    `qtdPamonha` int(3) NOT NULL,
    `qtdBoloMilho` int(3) NOT NULL,
    `qtdBoloMacaxeira` int(3) NOT NULL,
    `qtdPeDeMoleque` int(3) NOT NULL,
    `valorTotalRetorno` float NOT NULL)''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS saida (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `nomeVendedor` varchar(40) NOT NULL,
    `qtdMilho` int(3) NOT NULL,
    `qtdCanjicaPequena` int(3) NOT NULL,
    `qtdCanjicaGrande` int(3) NOT NULL,
    `qtdPamonha` int(3) NOT NULL,
    `qtdBoloMilho` int(3) NOT NULL,
    `qtdBoloMacaxeira` int(3) NOT NULL,
    `qtdPeDeMoleque` int(3) NOT NULL,
    `valorTotalSaida` float NOT NULL
        )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS valores (
    `id` int(11) NOT NULL,
    `vlrMilho` float NOT NULL,
    `vlrCanjicaPequena` float NOT NULL,
    `vlrCanjicaGrande` float NOT NULL,
    `vlrPamonha` float NOT NULL,
    `vlrBoloMilho` float NOT NULL,
    `vlrBoloMacaxeira` float NOT NULL,
    `vlrPeDeMoleque` float NOT NULL)''')
    cursor.execute('''SELECT id FROM valores''')
    cadastrou = cursor.fetchone()
    if cadastrou is None:
        cursor.execute('''INSERT INTO `valores` (`id`, `vlrMilho`, `vlrCanjicaPequena`, `vlrCanjicaGrande`, `vlrPamonha`, `vlrBoloMilho`, `vlrBoloMacaxeira`, `vlrPeDeMoleque`) VALUES
        (1, 3, 4, 6, 5, 8, 7, 9);''')
        conexao.commit()

    return  conexao

