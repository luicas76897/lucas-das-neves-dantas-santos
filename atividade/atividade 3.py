PALAVRA_COMPLETA = "PARALELEPIPEDO"
PALAVRA_IMCOMPLETA = "PAEALELE__PEDO"
SILABA_FALTANDO = "PI"

silabas_usadas = []

print(f"a palavra é: {PALAVRA_IMCOMPLETA}")
while True:
    silabas_inseridas = input("QUAL A SILABA?").upper()

    if silabas_inseridas == SILABA_FALTANDO:
        print("voce acertou a silaba")
        break
    elif silabas_inseridas in silabas_usadas:
        print("essa silaba esta INCORRETA e já foi tentada!")
    else:
        silabas_usadas.append(silabas_inseridas)
        print(F"SILABA_INCORRETA: {silabas_usadas}")



   
