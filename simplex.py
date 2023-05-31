print("Insira as variáveis conforme for solicitado")

vetorFO = []
vetorRestricao = []
variaveisDecisao = 0
qtdRestricao = 0
qtdVariaveisRestricao = 0


def metodoSimplex():

    # CRIANDO O VETOR FUNÇÃO OBJETIVO E AJUSTANDO AS VARIAVEIS DE FOLGA
    qtdVariaveisDecisao = int(
        input("\nQuantas são suas variáveis de decisão ?\n"))

    while len(vetorFO) < qtdVariaveisDecisao:
        variaveisDecisao = input(
            "Insira a variável de maneira que a função objetivo estaja igualada a zero: ")
        vetorFO.append(variaveisDecisao)

    i = qtdVariaveisDecisao
    while i < qtdVariaveisDecisao + 2:
        vetorFO.append(0)
        i = i + 1

    # CRIANDO OS VETORES DE RESTRIÇÃO
    qtdRestricao = int(input("Insira a quantidade de restrições: "))

    while len(vetorRestricao) < qtdRestricao:
        novo_vetor = []
        vetorRestricao.append(novo_vetor)

    # PREENCHENDO OS VETORES DE RESTRIÇÃO COM AS RESTRIÇOES E VARIAVEIS DE FOLGA
    i = 1
    j = 0
    z = 0
    k = 1
    while z < qtdRestricao:
        qtdVariaveisRestricao = int(
            input(f"Quantas variáveis tem sua {k}ª restrição ?\n"))
        while len(vetorRestricao[j]) < qtdVariaveisRestricao:
            vetorRestricao[j].append(
                int(input(f"Insira a sua {i}ª restrição: ")))
            i += 1
        j += 1
        z += 1
        k += 1


metodoSimplex()
print(vetorFO)
print("Quantidade de vetores restrição" + str(vetorRestricao))
print("Valores da primeira restrição" + str(vetorRestricao[0]))
print("Valores da primeira restrição" + str(vetorRestricao[1]))
