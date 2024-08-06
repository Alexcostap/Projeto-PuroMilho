pamonha = 5
canjica = 4
minhoCozido = 3

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

qtdSaidaMilhoCozido = int(input("Insira a quatidade de milho Cozido que está saindo: "))
qtdSaidaPamonha = int(input("Insira a quatidade de Pamonha que está saindo: "))
qtdSaidaCanjica = int(input("Insira a quatidade de canjica que está saindo: "))
valorTotalSaida = saida(qtdSaidaMilhoCozido, qtdSaidaPamonha, qtdSaidaCanjica)
print(valorTotalSaida)

qtdRetornoMilhoCozido = int(input("Insira a quatidade de milho Cozido que está saindo: "))
qtdRetornoPamonha = int(input("Insira a quatidade de Pamonha que está saindo: "))
qtdRetornoCanjica = int(input("Insira a quatidade de canjica que está saindo: "))
valorTotalRetorno = saida(qtdRetornoMilhoCozido, qtdRetornoPamonha, qtdRetornoCanjica)

valorFinal = valorTotalSaida - valorTotalRetorno
comissao = (valorFinal * 30) / 100

print(valorFinal)
print(comissao)