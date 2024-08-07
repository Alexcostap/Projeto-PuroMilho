from biblioteca import *



qtdSaidaMilhoCozido = int(input("Insira a quatidade de milho Cozido que está saindo: "))
qtdSaidaPamonha = int(input("Insira a quatidade de Pamonha que está saindo: "))
qtdSaidaCanjica = int(input("Insira a quatidade de canjica que está saindo: "))
valorTotalSaida = saida(qtdSaidaMilhoCozido, qtdSaidaPamonha, qtdSaidaCanjica)
print("R$",valorTotalSaida)

qtdRetornoMilhoCozido = int(input("Insira a quatidade de milho Cozido que está saindo: "))
qtdRetornoPamonha = int(input("Insira a quatidade de Pamonha que está saindo: "))
qtdRetornoCanjica = int(input("Insira a quatidade de canjica que está saindo: "))
valorTotalRetorno = retorno(qtdRetornoMilhoCozido, qtdRetornoPamonha, qtdRetornoCanjica)

valorFinal = valorTotalSaida - valorTotalRetorno
comissao = (valorFinal * 30) / 100

print(valorFinal)
print(comissao)