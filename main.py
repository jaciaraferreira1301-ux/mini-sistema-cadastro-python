def mostrar_menu():
    print("\n=== Mini Sistema ===")
    print("1 - Mostrar nome")
    print("2 - Mostrar idade")
    print("3 - Somar dois números")
    print("0 - Sair")


def opcao_nome():
    nome = input("Digite seu nome: ").strip()
    if nome == "":
        print("Você não digitou um nome.")
    else:
        print(f"Olá, {nome}!")


def ler_int(mensagem):
    while True:
        valor = input(mensagem).strip()
        try:
            return int(valor)
        except ValueError:
            print("Digite um número inteiro válido (ex: 23).")


def ler_float(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Digite um número válido (ex: 10 ou 10.5).")


def opcao_idade():
    idade = ler_int("Digite sua idade: ")
    if idade < 0:
        print("Idade não pode ser negativa.")
    else:
        print(f"Você tem {idade} anos.")


def opcao_somar():
    n1 = ler_float("Digite o primeiro número: ")
    n2 = ler_float("Digite o segundo número: ")
    print(f"Resultado: {n1} + {n2} = {n1 + n2}")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            opcao_nome()
        elif opcao == "2":
            opcao_idade()
        elif opcao == "3":
            opcao_somar()
        elif opcao == "0":
            print("Saindo do sistema... até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()
