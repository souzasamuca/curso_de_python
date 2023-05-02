idade = int(input("Digite sua idade: "))

if idade <=18:
        print(f"Sua idade é: {idade} Anos , \nVocê ainda não pode se alistar. ")

elif idade <= 21:
        print(f"Sua idade é: {idade} Anos , \nVocê ja pode se alistar.")
else:
        print(f"Sua idade é: {idade} Anos , \nSeu praso de se alistar ja passou.")
