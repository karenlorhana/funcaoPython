#calcular área de um retângulo

def areaRetangulo (a, b):
   area = base * altura
   return area

base = float(input("digite a base: "))
altura = float(input("digite a altura: "))

x = areaRetangulo(base, altura)

print("a área do seu retângulo é: ", x)