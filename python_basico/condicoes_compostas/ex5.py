#Criando um algoritmo que calcula a média de um aluno.
#Utilizando condiçôes compostas.

aluno = str(input("digite o nome do aluno: "))
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = (nota1+ nota2+ nota3) / 3
print("Amédia final é:", media)

print(f"Digite o nome do aluno: {aluno}\n"
      f"Digite a primeira nota: {nota1}\n"
      f"Digite a segunda nota: {nota2}\n"
      f"Digite a terceira nota: {nota3}\n"
      f"A média final é: {media:.1f}")

if media >= 7:
    print(f"O aluno:", aluno, "foi aprovado!")
else:
    print(f"O aluno:", aluno, "foi reprovado!")

'''
Esse é um tipo de comentario 
em broco.
'''







