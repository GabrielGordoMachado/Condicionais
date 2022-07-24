print('Escreva o valor das coordenadas X e Y, respectivamente:')
X, Y = map(float, input().split())
if X == 0 and Y == 0:
 print('O ponto se encontra na origem dos eixos X e Y.')
elif X == 0 and Y != 0:
 print("O ponto se encontra na origem do eixo X e sobre a coordenada ({0:.1f}) do eixo Y".format(Y))
elif Y == 0 and X != 0:
 print("O ponto se encontra na origem do eixo Y e sobre a coordenada ({0:.1f}) do eixo X".format(X))
else:
    if X < 0 and Y < 0:
      Quadrante = 3
    elif Y < 0 < X:
      Quadrante = 4
    elif X > 0 and Y > 0:
      Quadrante = 1
    elif X < 0 < Y:
      Quadrante = 2

    print("O ponto se encontra no {0}º Quadrante, nas coordenadas ({1:.1f}) e ({2:.1f}), respectivamente X e Y".format(Quadrante, X, Y))

