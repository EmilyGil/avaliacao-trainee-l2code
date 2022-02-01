import sys

lista_num = [3, -5, 1, 7, 0]

# Funções
def plusone(val):
    val = 1
    return val


def minusone(val):
    val = -1
    return val


def inc(val):
    val = val + 1
    return val


def dup(val):
    val = val * 2
    return val


def listar(lista):
    for i in lista:
        print(i)


for k in lista_num:
    instr = []
    valor = 0

    # Encerra o programa
    if k == 0:
        sys.exit()

    print("\nConstant", k)
    if k > 0:
        valor = plusone(valor)
        instr.append("PLUSONE")
        while valor != k:
            if k % 2 == 0:
                while valor < k:
                    valor = dup(valor)
                    instr.append("DUP")
            else:
                while valor < k:
                    valor = dup(valor)
                    instr.append("DUP")
                    valor = inc(valor)
                    instr.append("INC")

    else:
        valor = minusone(valor)
        instr.append("MINUSONE")
        while valor != k:
            if k % 2 == 0:
                while valor > k:
                    valor = dup(valor)
                    instr.append("DUP")
            else:
                while valor > (k + 1):
                    valor = dup(valor)
                    instr.append("DUP")
                valor = inc(valor)
                instr.append("INC")

    listar(instr)
