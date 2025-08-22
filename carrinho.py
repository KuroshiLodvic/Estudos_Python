print("=" * 5, "Lojonha", "=" * 5)
soma = produto_caro = menor = cont = 0
barato = None

while True:
    produto = input("O que você comprou?\n")
    valor = float(input("Digite o valor do produto: R$"))
    soma += valor
    cont += 1

    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    if valor >= 1000:
        produto_caro += 1

    continuar = input("Você quer continuar? [S/N]\n").upper()
    if continuar in "S":
        continue
    else:
        break

print(f"Você gastou R${soma:.2f} no total.")
print(f"Você comprou {produto_caro} produtos acima de R$1000,00")
print(f"O produto mais barato foi {barato} e custa R${menos:.2f}")