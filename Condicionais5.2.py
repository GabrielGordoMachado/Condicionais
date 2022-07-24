Numero1, Numero2 = map(int, input().split())
if (Numero1 % Numero2) == 0:
 print("É múltiplo de {0}!".format(Numero2))
else:
 print("Não é múltiplo de {0}.".format(Numero2))