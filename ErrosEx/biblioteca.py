def gravar(nome):
    with open("Nomes.text", "a") as arquivo:
        arquivo.write(f"{nome}\n")

def mostrar():
    with open("Nomes.text", "r") as arquivo2:
        print(arquivo2.read())

def pesquisar(texto):
    cont = 0
    with open("Nomes.text", "r") as pesq:
       for texto in pesq:
           cont+=1
    print(f"{cont}")
