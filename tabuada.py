from re import X
i = 1
x = int(input ('Digite um numero para calcular a tabuada: '))
for i in range(10):   
    print("{} x {} = {}".format(x, (i + 1), (x * (i + 1))))

print("Tabuada finalizada.")