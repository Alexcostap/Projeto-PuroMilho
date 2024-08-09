from conexao import *
#           Input dos valores a serem alterados na tabela 
vlrMilho = float(input("Informe o valor do MILHO COZIDO: "))
vlrCanjicaPequena = float(input("Informe o valor do CANJICA PEQUENA: "))
vlrCanjicaGrande = float(input("Informe o valor do CANJICA GRANDE: "))
vlrPamonha = float(input("Informe o valor do PAMONHA: "))
vlrBoloMilho = float(input("Informe o valor do BOLO DE MILHO: "))
vlrBoloMacaxeira = float(input("Informe o valor do BOLO DE MACAXEIRA: "))
vlrPeDeMoleque = float(input("Informe o valor do PÉ DE MOLEQUE: "))



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