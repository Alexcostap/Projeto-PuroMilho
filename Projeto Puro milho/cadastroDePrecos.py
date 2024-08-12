#from conexao import *
from biblioteca import cadastroPreco
#           Input dos valores a serem alterados na tabela 
vlrMilho = 2#float(input("Informe o valor do MILHO COZIDO: "))
vlrCanjicaPequena = 2#float(input("Informe o valor do CANJICA PEQUENA: "))
vlrCanjicaGrande = 3#float(input("Informe o valor do CANJICA GRANDE: "))
vlrPamonha = 4#float(input("Informe o valor do PAMONHA: "))
vlrBoloMilho = 2#float(input("Informe o valor do BOLO DE MILHO: "))
vlrBoloMacaxeira = 4#float(input("Informe o valor do BOLO DE MACAXEIRA: "))
vlrPeDeMoleque = 3#float(input("Informe o valor do PÉ DE MOLEQUE: "))


alterarPreco = cadastroPreco(vlrMilho,vlrCanjicaPequena,vlrCanjicaGrande,
                  vlrPamonha,vlrBoloMilho,vlrBoloMacaxeira,vlrPeDeMoleque)

print(alterarPreco)
# inserir = f"""UPDATE `valores` SET `vlrMilho` = '{vlrMilho}', 
#             `vlrCanjicaPequena` = '{vlrCanjicaPequena}', 
#             `vlrCanjicaGrande` = '{vlrCanjicaGrande}', 
#             `vlrPamonha` = '{vlrPamonha}', 
#             `vlrBoloMilho` = '{vlrBoloMilho}', 
#             `vlrBoloMacaxeira` = '{vlrBoloMacaxeira}', 
#             `vlrPeDeMoleque` = '{vlrPeDeMoleque}' 
#              WHERE `valores`.`id` = 1"""
# cursor.execute(inserir)
# conexao.commit()