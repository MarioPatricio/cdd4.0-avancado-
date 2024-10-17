from classes import *
a1 = Gato("Garfield", "laranja", 4)
print(a1.nome, a1.cor)
a2 = Vaca("Mimosa", "Marrom")
print(a2.nome, a2.cor)

y=0
x=1
while x==1:
    a2.muge()
    y+=1
    if y ==10:
        break