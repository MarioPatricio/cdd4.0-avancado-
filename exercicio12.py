list = [""]*5
tam = len(list)
for x in range(tam):
    list[x] = input("Digite um nome: ")
for y in range(4, -1, -1):
    print(list[y])
print(list.reverse(x))