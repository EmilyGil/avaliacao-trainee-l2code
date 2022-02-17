palavras = open("verb_in.txt", "r")

lista = []

mat = ['person', '1st', '2nd', '3rd', '4th', '5th', '6th'], \
      ['present', 'o', 'os', 'a', 'om', 'ons', 'am'], \
      ['past', 'ei', 'es', 'e', 'em', 'est', 'im'], \
      ['future', 'ai', 'ais', 'i', 'aem', 'aist', 'aim']

vogais = ['a', 'e', 'i', 'o', 'u']

for linha in palavras:
    if linha.endswith("\n"):
        linha = linha[:-1]
    lista.append(linha)

print("\nEntrada: ", lista, "\n")

for i in lista:
    inc = 1
    palavra_raiz = i[:-1]
    while palavra_raiz[-1:] in vogais:
        palavra_raiz = palavra_raiz[:-1]
        inc += 1
    verbo_inf = palavra_raiz + "en"

    cont = 0
    for j in range(1, 4, 1):
        for k in range(1, 7, 1):
            if i[-inc:] == mat[j][k]:
                print(i, "- verb", verbo_inf, ",", mat[j][0], "tense,", mat[0][k], "person")
                cont = 1

    if cont == 0:
        print(i, "- not a verb case")
