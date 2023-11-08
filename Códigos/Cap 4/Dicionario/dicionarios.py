usuarios={}
usuarios={
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
    }

#Na primeira linha, estamos criando o dicionário de dados. Repare que em vez de colchetes(como fizemos em lista)
#usamos as chaves "{}", essa é a representação de um dicionário de dados

#Também podemos adicionar itens do dicionário da seguinte forma:

usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]

#Se tentar usar a "mesma chave", o código não irá gerar erros ou exceções, mas o objeto que estiver na segunda linha
#irá sobreescrever o objeto que estava na primeira linha.

#Segue abaixo um código para exemplificar:

usuarios={}
usuarios={
    "Chaves":["Chaves Silva","17/06/1975","Recep_01"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_02"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_03"]
    }
usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"]=["Florinda Flores", "26/11/2016", "Recep_01"]

#Veremos agora como podemos retornar os dados de um objeto da lista

print(usuarios)
print("##############========#########")
print("Dados: ",usuarios.get("Chaves"))

#Se alterar dentro do get(), o valor de "Chaves" para "Chapolim", será retornado o valor "None"