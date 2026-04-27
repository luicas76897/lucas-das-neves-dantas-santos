import random

palavras  = ["casa","carro","mouse","cachorro"]
palavra = random.choice(palavras)
letras_descoberta=["_"]*len(palavra)
erros = 0
max_erros = 5

print("jogo da forca")

while erros < max_erros and "_" in letras_descoberta:
    print("\npalvra:", " ".join(letras_descoberta))
    
    letra=input("digite uma letra.").lower()
    
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descoberta[i] = letra
        print("acertou!")
    else:
        erros += 1
        print("errou! restam",max_erros-erros,"tentativas")

    if erros == max_erros:
        print("\nVocê perdeu! a palavra era:",palavra)
        break

        