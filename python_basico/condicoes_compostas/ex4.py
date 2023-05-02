#condição composta.
nome = str(input("Digite seu nome: "))
valor = float(input("Qual valor você possui: "))

if valor <= 50:
        print(f"Olá {nome} Você tem: R${valor:.2f} Você está pobre.")
elif valor <= 100:
        print(f"Olá {nome} Você tem: R$ {valor:.2f} AgOra Você está me convencendo.")
elif valor <= 250:
        print(f"Olá {nome} Você tem: R$ {valor:.2f} Gostei de ver!")
else:
        print(f"Olá {nome} Você tem: R$ {valor:.2f} Muito bom Você é uma pessoa bem sucedida!")

