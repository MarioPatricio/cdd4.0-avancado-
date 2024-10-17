from biblioteca import *
while True:
    from biblioteca import *
    print(f"1 --> Gravar.\n"
          f"2 --> Mostrar.\n"
          f"3 --> Pesquisar.\n"
          f"4 --> Sair.")
    opcao = int(input("Escolha um valor: "))
    #while opcao < 1 or opcao > 4:
     #   opcao = int(input("Escolha um valor: "))
    match opcao:
        case 1:
            gravar(input("Digite o texto: "))
        case 2:
            mostrar()
        case 3:
            pesquisar(input("Digite o texto: "))
        case 4:
            break
        case _:
            print("Opção inválida.")