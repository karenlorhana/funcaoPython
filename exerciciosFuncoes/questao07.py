#converter uma temperatura em farenheit para celcius

def farenheit (f):
   c = (5 * (f-32) / 9)
   return c

f = float(input("digite a temperatura em farenheit: "))
print("a temperatura em grau celcius é ", farenheit(f))

