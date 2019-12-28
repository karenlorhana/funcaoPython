#calcular IMC

def IMC(p, a):
   imc = (peso)/(altura**2)
   return imc

peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

print("seu imc é", IMC(peso, altura))