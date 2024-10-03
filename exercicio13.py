list = [0]*3
len(list)
for x in range(len(list)):
    list[x] = int(input("Digite um número: "))
menor = list[0] # ou o contrário
maior = 0
for y in range(len(list)):
    if list[y] % 2 == 0:
        print(f"O número {list[y]} é par.")
    if list[y] > maior:
        maior = list[y]
    if list[y] < menor:
        menor = list[y]
print(f"Menor número é {menor}.")
print(f"Maior número é {maior}.")