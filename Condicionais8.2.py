print("Qual a renda mensal do indivíduo?")
RendaMensal = float(input())

if RendaMensal < 1434.59:
    print("Você está isento de impostos, a sua renda anual é de R${0:.2f}".format(RendaMensal*12))

else:


    if RendaMensal < 2150:
        Imposto = (7.8/100)
    elif RendaMensal < 2866.70:
        Imposto = (15/100)
    elif RendaMensal < 3582:
        Imposto = (22.5/100)
    elif RendaMensal > 3582:
        Imposto = (27.5/100)

    print("A sua renda mensal líquida é de R${0:.2f}, R${1:.2f} ao ano.Atualmente você paga R${2:.2f} em impostos ao governo mensalmente, R${3:.2f} anualmente.".format(RendaMensal-(RendaMensal*Imposto),12*(RendaMensal-(RendaMensal*Imposto)),RendaMensal*Imposto, RendaMensal*Imposto*12))
