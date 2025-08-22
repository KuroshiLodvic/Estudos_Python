senha = 999
cont = 0
soma = 0

while True:
    res = int(input("Digite um valor: (999 para parar) "))
    if res == senha:
        break
    cont += 1
    soma += res

print(f"Você digitou {cont} números e a soma deles é {soma}")