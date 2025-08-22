num = int(input("Digite quantos números você quer na sequência: "))
a = 0
b = 1
c = 0

for i in range(0, num+1):
    c = a + b
    a = b
    b = c
    

    print(a, end=' ')
