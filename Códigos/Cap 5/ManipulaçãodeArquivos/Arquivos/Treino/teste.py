from funcoes import *

contas = {}
opcao = perguntas()
while opcao >0 and opcao < 3:
    if opcao == 1:
        criacao(contas)
    elif opcao ==2:
        arquivo(contas)
    elif opcao ==3:
        resultado = exibir()
        for linha in resultado:
            lista=linha.split(";")
            print("Nome....:", lista[0])
            print("Sexo....:", lista[1])
            print("Idade...:", lista[2])
opcao = perguntas()