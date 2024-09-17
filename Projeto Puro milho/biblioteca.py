from conexao import conectar
# Query simples para resgatar preços dos produtos no banco  
# Trás um array com cada valor destinado a uma variavel
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


# Função para calcular o valor total em R$ que saiu da loja e fazer o insert no banco de dados.
def saida(nomeVendedor, qtdMilhoCozido, qtdCanjicaPequena, qtdCanjicaGrande, qtdPamonha, qtdBoloMilho, qtdBoloMacaxeira, qtdPeDeMoleque):
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
#   Fazer o insert na tabela 'saida'.
    conexao = conectar()
    cursor = conexao.cursor()
    inserir = f"""INSERT INTO `saida` (`id`, `nomeVendedor`, `qtdMilho`, 
                                    `qtdCanjicaPequena`, `qtdCanjicaGrande`, 
                                    `qtdPamonha`, `qtdBoloMilho`, `qtdBoloMacaxeira`, 
                                    `qtdPeDeMoleque`,`valorTotalSaida`) VALUES (NULL, '{nomeVendedor}', 
                                    '{qtdMilhoCozido}', '{qtdCanjicaPequena}', '{qtdCanjicaGrande}',
                                    '{qtdPamonha}', '{qtdBoloMilho}','{qtdBoloMacaxeira}', 
                                    '{qtdPeDeMoleque}','{valorTotalSaida}')"""
    cursor.execute(inserir)
    conexao.commit()
    return nomeVendedor, valorTotalSaida

# Função para calcular o valor total em R$ que retornou para loja e fazer o insert no banco de dados.
def retorno(nomeVendedor, qtdMilhoCozido, qtdCanjicaPequena, qtdCanjicaGrande, qtdPamonha, qtdBoloMilho, qtdBoloMacaxeira, qtdPeDeMoleque):
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
    
    #   Fazer o insert na tabela 'retorno'.
    conexao = conectar()
    cursor = conexao.cursor()
    inserir = f"""INSERT INTO `retorno` (`id`, `nomeVendedor`, `qtdMilho`, 
                                    `qtdCanjicaPequena`, `qtdCanjicaGrande`, 
                                    `qtdPamonha`, `qtdBoloMilho`, `qtdBoloMacaxeira`, 
                                    `qtdPeDeMoleque`,`valorTotalRetorno`) VALUES (NULL, '{nomeVendedor}', 
                                    '{qtdMilhoCozido}', '{qtdCanjicaPequena}', '{qtdCanjicaGrande}',
                                    '{qtdPamonha}', '{qtdBoloMilho}','{qtdBoloMacaxeira}', 
                                    '{qtdPeDeMoleque}','{valorTotalRetorno}')"""
    cursor.execute(inserir)
    conexao.commit()
    
    selectSaida = f"""SELECT valorTotalSaida FROM `saida` WHERE nomeVendedor = '{nomeVendedor}' ORDER BY id DESC LIMIT 1;"""
    cursor.execute(selectSaida)
    valorTotalSaida = cursor.fetchone()[0]
    valorFinal = valorTotalSaida - valorTotalRetorno
    comissao = (valorFinal * 30) / 100
    return valorTotalRetorno,valorFinal, comissao, nomeVendedor

def vendaTotal():
    conexao = conectar()
    cursor = conexao.cursor()
    selectSaida = """SELECT * FROM `saida` WHERE nomeVendedor = 'Alex Costa' ORDER BY id DESC LIMIT 1;"""
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
