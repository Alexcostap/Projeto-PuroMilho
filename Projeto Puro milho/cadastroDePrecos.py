from biblioteca import cadastroPreco
#           Input dos valores a serem alterados na tabela 
vlrMilho = float(input("Informe o valor do MILHO COZIDO: "))
vlrCanjicaPequena = float(input("Informe o valor do CANJICA PEQUENA: "))
vlrCanjicaGrande = float(input("Informe o valor do CANJICA GRANDE: "))
vlrPamonha = float(input("Informe o valor do PAMONHA: "))
vlrBoloMilho = float(input("Informe o valor do BOLO DE MILHO: "))
vlrBoloMacaxeira = float(input("Informe o valor do BOLO DE MACAXEIRA: "))
vlrPeDeMoleque = float(input("Informe o valor do PÉ DE MOLEQUE: "))

# Chamada da função de cadastrar os preços no banco
alterarPreco = cadastroPreco(vlrMilho,vlrCanjicaPequena,vlrCanjicaGrande,
                  vlrPamonha,vlrBoloMilho,vlrBoloMacaxeira,vlrPeDeMoleque)
# Exibir retorno da função
print(alterarPreco)
