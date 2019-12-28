#converter uma temperatura em celcius para farenheit

def celcius (c):
   f = (c * 9/5) + 32
   return f

c = float(input("digite a temperatura em celcius: "))
print("a temperatura em farenheit é ", celcius(c))