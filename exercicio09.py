cont = 0
num = [0]*3
tam = len(num)
for x in range(tam):
    num[x] = int(input("Digite um número: "))
n2 = int(input("Digite OUTRO número: "))
#for y in range(tam):
#    if n2 == num [y]:
#        cont +=1
#if cont != 1:
 #   print(f"O número {n2} apareceu {cont} vezes.")
#else:
#    print(f"O número {n2} apareceu {cont} vez.")
print(num.count(n2))