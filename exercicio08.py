nome = [0]*2
senha = [0]*2
tamanho = len(nome)
for x in range(tamanho):
    nome[x] = input("Digite um nome: ")
    senha[x] = input("Digite uma senha: ")
for y in range(tamanho):
    print(f"O usuário {nome[y]} tem senha {senha[y]}, na posição {y}.")