print("=" * 30)
print('{:^30}'.format("Bancaçaralho"))
print("=" * 30)

money = int(input("Quanto você quer sacar, meu rei? R$"))

nota50 = money // 50
money = money % 50

nota10 = money // 10
money = money % 10

nota5 = money // 5
money = money % 5

nota1 = money // 1

print("=" * 30)
if nota50 > 0: 
    print(f"Você irá sacar {nota50} nota(s) de R$50,00")
if nota10 > 0:
    print(f"Você irá sacar {nota10} nota(s) de R$10,00")
if nota5 > 0:
    print(f"Você irá sacar {nota5} nota(s) de R$5,00")
if nota1 > 0:
    print(f"{nota1} nota(s) de R$1,00")
print("=" * 30)
print("Processo finalizado, rei.")
print("=" * 30)