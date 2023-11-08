def perguntas():
    escolha = int(input("Digite sua escolha: "
    "<1> criar conta"
    " <2> para criar o arquivo"
    " <3> ver as contas: "))
    return escolha


def criacao(dicionario):
    resp = "S"
    while resp=="S":
        dicionario[input("Digite o seu usuario: ")] = [
            input("Digite o nome: "),
            input("Digite o sexo: "),
            input("Digite a idade: ")]
        resp = input("Digite S se quiser continuar: ")

def arquivo(dicionario):
    with open("contas.csv","a") as cont:
        for chave, valor in dicionario.items():
            cont.write(chave + ";" + valor[0] + ";"
            + valor[1] + ";" + valor[2] + ";")
    return "Arquivo criado com sucesso"

def exibir():
    with open("contas.json","r") as cont:
        linhas=cont.readlines()
    return linhas