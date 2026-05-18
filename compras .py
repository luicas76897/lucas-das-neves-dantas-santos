lista_de_compras = []
while True:
    item = input("Digite o nome do item que deseja adicionar a lista de compras : ")
    lista_de_compras.append(item)
    continuar = input("Deseja adicionar outro item? remover um item? ou finalizar a lista? "
    "(adicionar/remover/finalizar) ").lower()
    if continuar == "adicionar":
        continue
    elif continuar == "remover":
        item_remover = input("Digite o nome do item que deseja remover da lista de compras ")
        if item_remover in lista_de_compras:
            lista_de_compras.remove(item_remover)
            print(f"{item_remover} foi removido da lista de compras.")
        else:
            print(f"{item_remover} não encontrado na lista de compras.")
    elif continuar == "finalizar":
        print("Lista de compras finalizada:")
        for item in lista_de_compras:
            print(f"- {item}")
        break
    else:
        print("Opção inválida. Por favor, escolha 'adicionar', 'remover' ou 'finalizar'.")
    
   
