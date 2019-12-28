#calcular salário mensal de um funcionário

def trabalho (a, b):
   tsal = hsal * htrab
   return tsal

hsal = float(input("digite quanto você ganha por hora: "))
htrab = float(input("digite quantas horas você trabalha por mês: "))


print("o seu salário total no mês é: ", trabalho(hsal,htrab))
