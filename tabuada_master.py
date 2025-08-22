print("-" * 5, "Tabuada Master", "-" *5)

while True:
    num = int(input("Digite o número que você quer ver a tabuada: "))
    
    if num <= 0:
        break
    
    else:
        print("-" * 15)
        
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

    print("-" * 15)

print("Número negativo detectado. Processo finalizado.")