lista_de_compras = []
while True:
    lista = input("quer adionar um item a lista de compras ? ")
    lista_de_compras.append("item")
    print("intem adiconado!")
    print(lista_de_compras) 
    if lista == "nao":
        print("ok, lista de compras finalizada!")
        break
    