nome = "samuel"
idade = 28
preco = 12.3
#Esse tipo de print não se utiliza mais.
print(f"meu nome é: {nome}\nMinha idade é: {idade} anos\nTenho na carteira: {preco:.2f} reais".format(nome, idade, preco))

#Esse formato de print , que é o mais utilizado atualmente.
print(f"meu nome é: {nome}\nMinha idade é:{idade} anos\nTenho na carteira: {preco:.2f} reais")

#Boas praticas , quebrar a linha com \n dando um enter após o \n.
print(f"meu nome é: {nome}\n"
      f"Minha idade é: {idade}anos\n"
      f"Tenho na carteira: {preco:.2f}")



