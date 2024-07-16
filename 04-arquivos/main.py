# abrir arquivo

# arquivo = open("dados.txt")
# TextIOWrapper (retorno do open)
#print(arquivo)
#print(arquivo.read()) # pega o aqruivo e retorna como string
#print(arquivo.read()) # não tem como ler de novo pois funciona como um ponteiro


# conteudo = arquivo.read() # devolve string 
# readlines() devolve uma lista:
#['BANANA VERDE', 'UVA VERDE']
#['BANANA VERDE', 'UVA VERDE']
# print(conteudo)

# linhas = []
# for linha in arquivo:
#    linhas.append(linha.strip().lower()) # strip: remove quebras de linha, o que está antes e depois da string. Tira o \n
# print(linhas)

# terminal volta: encerra sozinho
# no Flask não acontece isso. Se abrir um arquivo ele ocupa memoria até o servidor cair

# fechando o arquivo do open() - não é a melhor forma pois vc pode esquecer de fechar 
# arquivo.close()

# bloco with - melhor forma 
# (Quando a execução sair do bloco de contexto ela fecha por você)

# arquivo2 = open("dados.text")
# with open("dados.txt") as arquivo2:
#    conteudo = arquivo2.read()
#    print(conteudo)
# print("teste teste")
# print(arquivo2.read())
# --------------
# with open("dados.txt", "r") as arquivo2:
#    arquivo2.write("teste") # open sempre abre com o modo leitura e por isso não pode ditá-lo # abertura com o "r" # nao vai funcionar
#    conteudo = arquivo2.read()
#    print(conteudo)
# print("teste teste")
# print(arquivo2.read())

# "W" permite escrever mas trava
# with open("dados.txt", "w") as arquivo2:
#    arquivo2.write("frutaaas")

#"A" - adiconar uma nova linha (a = append)
# se quiser escrever em outra linha tem que colocar o \n
# with open("dados.txt", "a") as arquivo2:
#    arquivo2.write("\nfrutaaas")

# arquivo CSV (separados por virgula)

# ler o arquivo produtos.csv e carregar em memória lista na qual cada porduto é um dict

def linha_para_produtos(linha):
    # print(linha.strip().split(",")) # split  faz cada linha ser uma lista diferente 
        dados = linha.strip().split(",")
        return {
            "nome": dados[0],
            "descricao": dados[1],
            "preco": float(dados[2]),
            "imagem" : dados[3] 
        }
            

        # dados = linha.strip().split(",")
        # produto = {
        #    "nome": dados[0],
        #    "descricao": dados[1],
        #    "preco": float(dados[2]),
        #    "imagem": dados[3]
        # } essa parte da na função s.csv", "r") as arquivo_produtos:
    # quero pegar linha a linha (readlines ou for)
    # for linha in arquivo_produtos:
        # print(linha.strip().split(",")) # split  faz cada linha ser uma lista diferente 
        # dados = linha.strip().split(",")
        # produto = {
        #    "nome": dados[0],
        #    "descricao": dados[1],
        #    "preco": float(dados[2]),
        #    "imagem": dados[3]
        # } essa parte da na função 
    #    produto.append(produto)
    #print(produto)



def obter_produtos():
    with open("produtos.csv", "r") as arquivo_produtos:
        # quero pegar linha a linha (readlines ou for)
        produtos = []
        for linha in arquivo_produtos:
            produto = linha_para_produtos(linha)
            produtos.append(produto)
        #print(produtos) # não é legal dar print aqui por isso faça uma função...
        return produtos
    with open("produtos.csv", "r") as arquivo_produtos:
        # quero pegar linha a linha usa-se readlines ou for
        produtos = []
        for linha in arquivo_produtos:
            produto = linha_para_produtos(linha)
            produtos.append(produto)
        #print(produtos) # não é legal dar print aqui por isso faça uma função...
print(obter_produtos())




# passando dado a dado
def salvar_produto(nome, descricao, preco, imagem):
    texto = f"\n{nome}, {descricao}, {preco}, {imagem}"
    with open("produtos.csv", "a") as arquivo_produtos:
        arquivo_produtos.write(texto) 
     
salvar_produto("celular", "tira foto", "1500.00", "celular.jpg")
salvar_produto("skate", "te derruba igual a vida", "1600.00", "skate.jpg")



