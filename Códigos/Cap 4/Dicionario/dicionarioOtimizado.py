from funcoesDicionario import *
usuarios={}

opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    if opcao=="P":
        pesquisar(usuarios,input("Qual código de lançamento deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios,input("Qual código de lançamento deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()