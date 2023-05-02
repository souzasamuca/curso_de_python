"""
Criando um algoritmo que ,
verifica a idade de cada candidato ,
e diz se ele estar apto a servir no quartel.
"""

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if idade <= 18:
    print(f"Você tem apenas {idade} anos de idade.\n"
          f"você ainda não pode se alistar {nome}")
elif idade >= 18 <= 21:
    print(f"Você tem {idade} anos de idade.\n"
          f"você ja pode se alistar {nome}")
else:
    print(f"Você tem {idade} anos de idade.\n"
          f"Seu tempo de se alistar ja passou {nome} ")


