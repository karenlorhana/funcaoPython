#???????

def que1(a,b):
   a = n1 * 2
   b = n2 / 2
   c = a + b
   return c

def que2 (c, d):
   d = n1 * 3
   e = d + n3
   return e
def que3 (e):
   f = n3 **3
   return f

n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = float(input("n3: "))

print("o produto do dobro do primeiro com metade do segundo: ", que1(n1,n2))
print("a soma do triplo do primeiro com o terceiro: ", que2(n1, n3))
print("o terceiro elevado ao cubo: ", que3(3))
