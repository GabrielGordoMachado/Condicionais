Numero1, Numero2, Acao = input().split()
Numero1, Numero2 = int(Numero1), int(Numero2)
if Acao.__contains__('+'):
 print("({0}) {1} ({2}) = {3:.2f}".format(Numero1, Acao, Numero2, Numero1 + Numero2))
elif Acao.__contains__('/'):
 print("({0}) {1} ({2}) = {3:.2f}".format(Numero1, Acao, Numero2, Numero1 / Numero2))
elif Acao.__contains__('-'):
 print("({0}) {1} ({2}) = {3:.2f}".format(Numero1, Acao, Numero2, Numero1 - Numero2))
elif Acao.__contains__('*'):
 print("({0}) {1} ({2}) = {3:.2f}".format(Numero1, Acao, Numero2, Numero1 * Numero2))
