def e_par(numero):
    if numero == 0:
        return False

    return numero % 2 == 0

numero = input("insira um numero: ")
numero_convertido = 0.0

try:    
    numero_convertido = float(numero)
except ValueError as e:
    print(f"O valor inserido não é um número válid,o. Erro: {e}")

if e_par(numero_convertido):
    print(f"O número {numero_convertido} é par.")
else:
    print(f"O número {numero_convertido} é ímpar.")