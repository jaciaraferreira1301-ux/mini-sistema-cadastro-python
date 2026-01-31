
print("=== Mini Sistema ===")

while True:
    print("\n1 - Mostrar nome")
    print("2 - Mostrar idade")
    print("3 - Somar dois números")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite seu nome: ")
        print(f"Olá, {nome}")

    elif opcao == "2":
        idade = input("Digite sua idade: ")
        print(f"Você tem {idade} anos")

    elif opcao == "3":
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        soma = n1 + n2
        print(f"A soma é: {soma}")

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, tente novamente.")
