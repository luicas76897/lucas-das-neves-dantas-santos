lista_cadastro = []
while True:
    print(lista_cadastro)

    nome = input("digite um nome")
    idade = int(input("digite a idade"))

    dicionario_base = {
      "nome" : nome,
      "idade": idade,
    }

    if dicionario_base in lista_cadastro:
      print("pessoa já cadastrada")
    else:
      lista_cadastro.append(dicionario_base)

      pergunta = input("quer continuar a cadastro ?")
      if pergunta not in ["sim", "sim","SIM", "S","s", "YES", "yes", "Y", "y"]:
        break