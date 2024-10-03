print("Digite\n"
          f"1 --> Soma\n"
          f"2 --> Subtração\n"
          f"3 --> Multiplicação\n")
opcao = int(input("Qual operação você deseja realizar? "))
while opcao < 1 or opcao > 6:
        opcao = int(input("Opção inválida, digite novamente:  "))
match opcao:
        case 1: