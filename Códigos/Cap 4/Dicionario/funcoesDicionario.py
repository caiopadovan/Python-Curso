
def perguntar():
    resposta = input("O que deseja realizar?" +
                  "   <I> - Para Inserir um usuário" +
                  "   <P> - Para Pesquisar um usuário" +
                  "   <E> - Para Excluir um usuário" +
                  "   <L> - Para Listar um usuário: ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o código de lançamento: ").upper()] = [input("Digite a última data de acesso: ").upper(),
                                          input("Qual a última estação acessada: ").upper(),
                                          input("Qual o horário de login: "),
                                          input("Digite o nível do usuário: ")]

def pesquisar (dicionario, chave):                         #dicionario = onde se pretende pesquisar , chave = o dado que será pesquisado
    lista=dicionario.get(chave)
    if lista!=None:
        print("Último acesso.........:" + lista[0])
        print("Última estação.........:" + lista[1])
        print("Último horário em que foi logado..........: "+ lista[2])
        print('Nível do usuário.........:'+ lista[3])

def excluir(dicionario, chave):                            # dicionario = onde o objeto será excluido, chave = chave do objeto que se deseja excluir
    if dicionario.get(chave) !=None:                       # É necessário verificar se a chave existe
        del dicionario[chave]
    print("Objeto eliminado")

def listar(dicionario):                                    # dicionario = contém os dados que devemos exibir
    for chave, valor in dicionario.items():                # Utilizamos dois valores(chave e valor) para dar uma saída mais "clean" para o usuário final
        print("Objeto......")
        print("Código de lançamento: ", chave)
        print("Dados: ", valor)