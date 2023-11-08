usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Digite um e-mail: ").lower())
    resp=input("Digite <S> para continuar: ").upper()

tupla = list(enumerate(emails))         # Estamos enumerando cada item na lista "e-mail" e gerando uma tupla com cada elemento
for chave in range(0,len(tupla)):       # A função range() controla o laço "for" de zero até a quantidade de elementos encontrados na "tupla"
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome: "), input("Digite o nível: ")]

print()

for chave,dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...:", chave[1])
    print("Nome....:", dado[0])
    print("Nível...:", dado[1])