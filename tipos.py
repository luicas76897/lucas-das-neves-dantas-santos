# strigue=texto
# int = = numeros inteiros (1,2,3,4,5,)
# float= numeros de ponto flutuantes 
# list = lista
# dict = dicionario
#tupla =  
# sts = conjutos
# datetime
# bool = boleano
'''
type() - validar tipos, assim verificando se tipo corresponde ao pedido do codigo
'''

# texto= 'aula'
# numero="100"
# print('essa é a varivel texto: ', texto)
# print("essa variavel é do tipo:  ", type(texto))

# print(type(type(texto) == type(numero)))

ponto_flutuante = 1.2
# inteiro 
complex = 10 + 3j
# f - strin é um texto que recebe variaveis em chave  
# print(f"a soma de {inteiro} mais {ponto_flutuante}é: {intero+ponto_flutuante}")
# while True:
#     recebido = input("digite um numero: ")
#     try:
#         recebido = int(recebido)
#     except ValueError:
#         try:
#             recebido = float(recebido)
#         except ValueError:
#             pass

#     print(bool(recebido))

# if type(recebido) == int:
#     print("esse numero é inteiro")
# else: 
#     print("esse numero não é um inteiro")
dicionario={
    "chave":10,
    "chave2": "10" 
}
lista = {1,2,3,}

chave = dicionario["chave"]
chave2 = dicionario["chave2"]
# print(f"o valor da chave é {chave}")
# print(f"o valor da chave2 é{chave}")
# print(dicionario.keys())
# print(dicionario.values())
print(dicionario)
dicionario["chave2"]="lucas"
print(dicionario)