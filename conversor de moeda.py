import os

os.system('cls')
print("Conversor de moeda universall. atenção! esse codigo serve somente como ilustração")
print("Para converter, real em dolar digite (1)")
print("Para converter, dolar em real digite (2)")
escolha = int(input ('Sua escolha: '))

if escolha == 1:
    Real = int(input ("Qual o valor em real deseja converter?:$"))
    print("{} reais na cotação atual é igual a {:.2f} dolares".format(Real, (Real/5.10)))

if escolha == 2:
    dolar = int(input ("Qual o valor em dolar deseja converter?:$"))
    print("{} dolares na cotação atual é igual a {:.2f} reais".format(dolar, (dolar*5.10)))  

if ((escolha != 1) and (escolha != 2)):
    print("Erro valor invalido")