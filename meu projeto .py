nomes = []

while True:
    nome = input("digite um nome (ou 'sair')): ")
    
    if nome == "sair":
        break

    nomes.append(nome)
    print("nome cadastro!")

print("\nlista de nomes:")
for n in nomes:
    print(n)