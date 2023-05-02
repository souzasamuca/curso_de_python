print('''
[1] - soma,
[2] - subtração,
[3] - multiplicação,
[4] - divisão,
[5] - sair
''')

opc = int(input("Escolha uma opção: "))
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

while opc != 5:

    if opc == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} e {n2} é igual a {soma}")

    elif opc == 2:
        subtracao = n1 - n2
        print(f"A subtração entre {n1} e {n2} é igual a {subtracao}")

    elif opc == 3:
        multiplicacao = n1 * n2
        print(f"A multiplicação entre {n1} e {n2} é igual a {multiplicacao}")

    elif opc == 4:
        divisao = n1 / n2
        print(f"A divisão entre {n1} e {n2} é igual a {divisao}")

    elif opc == 5:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")

