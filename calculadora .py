numer_um = 10
numer_dois = 12
numero_tres = 13
numero_qutro = 14

def somar(*args):
     return sum (args)


def subtração(*args):
        valor = 1
        for n in args:
              valor -= int(n)
              return valor  


def divisão(*args):
      valor = 1
      for n in args:
            valor /= int(n)
            return valor

def mutiplicação(*args):
      valor = 1 
      for n in args:
            valor *= int(n)
            return valor 
      
while True:
    nome = input("qual operação você quer calcular ? : ")
                       
          
