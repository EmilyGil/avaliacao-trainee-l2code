lista = ['casos', 'porre', 'corraem', 'picel', 'oficina', 'param']

mat = ['person', '1st', '2nd', '3rd', '4th', '5th', '6th'], \
      ['present', 'o', 'os', 'a', 'om', 'ons', 'am'], \
      ['past', 'ei', 'es', 'e', 'em', 'est', 'im'], \
      ['future', 'ai', 'ais', 'i', 'aem', 'aist', 'aim']

vogais = ['a', 'e', 'i', 'o', 'u']

for i in lista:
    for k in range(7):
        for j in range(4):
            if i[-1:] == mat[j][k]:
                fim = i[-1:]
                raiz = i[:-1]
                if raiz[-1:] not in vogais:
                    verbo = raiz + "en"
                    print(i, "- verb", verbo, ",", mat[j][0], "tense,", mat[0][k], "person")
            elif i[-2:] == mat[j][k]:
                fim = i[-2:]
                raiz = i[:-2]
                if raiz[-1:] not in vogais:
                    verbo = (i[:-2]) + "en"
                    print(i, "- verb", verbo, ",", mat[j][0], "tense,", mat[0][k], "person")
            elif i[-3:] == mat[j][k]:
                fim = i[-3:]
                raiz = i[:-3]
                if raiz[-1:] not in vogais:
                    verbo = (i[:-3]) + "en"
                    print(i, "- verb", verbo, ",", mat[j][0], "tense,", mat[0][k], "person")

            #else:
            #    print(i, "- not a verb case")
