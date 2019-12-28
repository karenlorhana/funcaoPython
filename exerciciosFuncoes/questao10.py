#peso ideal

def pesoIdeal(a):
   pesoI = (72.7*altura) - 58
   return pesoI

altura = float(input("digite a sua altura para saber seu peso ideal: "))
p = pesoIdeal(altura)
print("o seu peso ideal é: ", p)
