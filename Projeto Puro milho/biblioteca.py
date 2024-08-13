from conexao import conectar
# Query simples para resgatar preços dos produtos no banco  
# Trás um array com cada valor destinado a uma variavem
def importarPrecos():
    conexao = conectar()
    cursor = conexao.cursor()
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

# Função para calcular o valor total em R$ que saiu da loja.
def saida(qtdMilhoCozido, qtdCanjicaPequena, qtdCanjicaGrande, qtdPamonha, qtdBoloMilho, qtdBoloMacaxeira, qtdPeDeMoleque):
    milho,canjicaPequena,canjicaGrande,pamonha,boloMilho,boloMacaxeira,peDeMoleque = importarPrecos()
    
    valorMilhoCozido = qtdMilhoCozido * milho
    valorCanjicaPequena = qtdCanjicaPequena * canjicaPequena
    valorCanjicaGrande = qtdCanjicaGrande * canjicaGrande
    valorPamonha = qtdPamonha * pamonha
    valorBoloMilho = qtdBoloMilho * boloMilho
    valorBoloMacaxeira = qtdBoloMacaxeira * boloMacaxeira
    valorPeDeMoleque = qtdPeDeMoleque * peDeMoleque
    
    valorTotalSaida = (valorMilhoCozido + valorCanjicaPequena + valorCanjicaGrande +
                       valorPamonha + valorBoloMilho + valorBoloMacaxeira + valorPeDeMoleque)
    
    return valorTotalSaida

# Função para calcular o valor total em R$ que retornou da loja.
def retorno(qtdMilhoCozido, qtdCanjicaPequena, qtdCanjicaGrande, qtdPamonha, qtdBoloMilho, qtdBoloMacaxeira, qtdPeDeMoleque):
    milho,canjicaPequena,canjicaGrande,pamonha,boloMilho,boloMacaxeira,peDeMoleque = importarPrecos()
    
    valorMilhoCozido = qtdMilhoCozido * milho
    valorCanjicaPequena = qtdCanjicaPequena * canjicaPequena
    valorCanjicaGrande = qtdCanjicaGrande * canjicaGrande
    valorPamonha = qtdPamonha * pamonha
    valorBoloMilho = qtdBoloMilho * boloMilho
    valorBoloMacaxeira = qtdBoloMacaxeira * boloMacaxeira
    valorPeDeMoleque = qtdPeDeMoleque * peDeMoleque
    
    valorTotalRetorno = (valorMilhoCozido + valorCanjicaPequena + valorCanjicaGrande +
                       valorPamonha + valorBoloMilho + valorBoloMacaxeira + valorPeDeMoleque)
    
    return valorTotalRetorno


# Função para fazer update dos preços na tabela 'Valores' 
def cadastroPreco(vlrMilho,vlrCanjicaPequena,vlrCanjicaGrande,
                  vlrPamonha,vlrBoloMilho,vlrBoloMacaxeira,vlrPeDeMoleque):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
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
        return "Alteração realizada com sucesso!!!"
    except:
        conexao.rollback()
        return f"Erro ao realizar alteração: {Exception}"
    finally:
        cursor.close()
        conexao.close()