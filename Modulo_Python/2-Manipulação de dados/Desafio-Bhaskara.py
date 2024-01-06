import math

def calcular_bhaskara(a, b, c):
    # Calcular o discriminante
    delta = b**2 - 4*a*c
    
    # Verificar se há raízes reais
    if delta < 0:
        return None  # Sem raízes reais
    elif delta == 0:
        # Apenas uma raiz real
        raiz = -b / (2*a)
        return raiz,
    else:
        # Duas raízes reais
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2

# Entrada de dados
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Chamar a função e obter as raízes
raizes = calcular_bhaskara(a, b, c)

# Exibir as raízes
if raizes is None:
    print("A equação não possui raízes reais.")
elif len(raizes) == 1:
    print(f"A equação possui uma raiz real: {raizes[0]}")
else:
    print(f"A equação possui duas raízes reais: {raizes[0]} e {raizes[1]}")