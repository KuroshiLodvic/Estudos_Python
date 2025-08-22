print("=" * 5, "Cadastro", "=" * 5)

maior = homens = mulher_menos_20 = 0

while True:
    sexo = input("Digite seu sexo: [H/M/O] ").upper()
    while sexo not in ["H", "M", "O"]:
        sexo = input("Digite seu sexo: [H/M/O] ").upper()
    
    idade = int(input("Digite quantos anos você tem: "))
    
    continuar = input("Você quer continuar? [S/N] ").upper()
    while continuar not in ["S", "N"]:
        continuar = input("Você quer continuar? [S/N] ").upper()

    if idade >= 18:
        maior += 1

    if sexo in "H":
        homens += 1
    
    if sexo in "M" and idade < 20:
        mulher_menos_20 += 1
   
    if continuar in "S":
        continue
    else:
        break

print(f"""Foram cadastrados:
{maior} pessoas com mais de 18 anos;
{homens} homem(s);
e {mulher_menos_20} mulher(es) com menos de 20 anos.
""")