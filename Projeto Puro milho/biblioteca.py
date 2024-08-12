from conexao import conectar

def importarPrecos():
    conexao = conectar()
    cursor = conexao.cursor
    select = """select * from valores where id = 1"""
    cursor.execute(select)
    resultado = cursor.fetchone()
    milho = resultado[1]
    canjicaPequena = resultado[2]
    canjicaGrande = resultado[3]
    pamonha = resultado[4]
    boloMilho = resultado[5]
    boloMacaxeira = resultado[6]
    peDeMoleque = resultado[7]

    return milho,canjicaPequena,canjicaGrande,pamonha,boloMilho,boloMacaxeira,peDeMoleque

def saida(qtdMilhoCozido, qtdPamonha, qtdCanjica):
    valorMilhoCozido = qtdMilhoCozido * minhoCozido
    valorPamonha = qtdPamonha * pamonha
    valorCanjica = qtdCanjica * canjica
    valorTotalSaida = valorMilhoCozido + valorCanjica + valorPamonha
    return valorTotalSaida

def retorno(qtdMilhoCozido, qtdPamonha, qtdCanjica):
    valorMilhoCozido = qtdMilhoCozido * minhoCozido
    valorPamonha = qtdPamonha * pamonha
    valorCanjica = qtdCanjica * canjica
    valorTotalRetorno = valorMilhoCozido + valorCanjica + valorPamonha
    return valorTotalRetorno

def cadastroPreco(vlrMilho,vlrCanjicaPequena,vlrCanjicaGrande,
                  vlrPamonha,vlrBoloMilho,vlrBoloMacaxeira,vlrPeDeMoleque):
    conexao = conectar()
    cursor = conexao.cursor
    inserir = f"""UPDATE `valores` SET `vlrMilho` = '{vlrMilho}', 
            `vlrCanjicaPequena` = '{vlrCanjicaPequena}', 
            `vlrCanjicaGrande` = '{vlrCanjicaGrande}', 
            `vlrPamonha` = '{vlrPamonha}', 
            `vlrBoloMilho` = '{vlrBoloMilho}', 
            `vlrBoloMacaxeira` = '{vlrBoloMacaxeira}', 
            `vlrPeDeMoleque` = '{vlrPeDeMoleque}' 
             WHERE `valores`.`id` = 1"""
    cursor.execute(inserir)
    conexao.commit()
    return ("Alteração realizada com sucesso!!!")