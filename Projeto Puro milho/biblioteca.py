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