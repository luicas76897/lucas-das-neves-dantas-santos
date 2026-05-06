"""
Operadores:
    - São símbolos que realizam operações em variáveis e valores.
    - Exemplos de operadores:
        - Aritméticos: +, -, *, /, // (divisão inteira), % (módulo), ** (exponenciação)
        - Relacionais: (==, !=, >, <, >=, <=) -> Sempre vai retornar um valor booleano (True ou False)
        - Lógicos: and, or, not
"""

variavel_1 = int(input("digite o primeiro numero" ))
variavel_2 = int(input("digite o segundo numero" ))
variavel_3 = int(input("digite o terceiro numero" ))
variavel_4 = int(input("digite o quarto numero" ))

if variavel_1 < variavel_2 or variavel_3 > variavel_2:
    print("valor 1 menor do que valor dois ou valor 3 maior que dois ")
    input("Aperte enter pra continuar...")

if variavel_2 == variavel_3 and variavel_3 > variavel_2:
    print("valor 2 igual a 3 e valor 3 menor que vaor 2 ")
    input("Aperte enter pra continuar...")

if variavel_3 > variavel_2 or variavel_3 == variavel_1:
    print("valor 3 maior que valro 2 ou valor 3 igual a vlor 1")
    input("Aperte enter pra continuar...")

if variavel_4 > variavel_1 and variavel_1 < variavel_3:
    print("valor 4 mairo que valor 1 e valor 1 menor que valor 3 ")
    input("Aperte enter pra continuar...")
