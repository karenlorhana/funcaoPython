#hein

def tinta (l):
   lata = (1 * area)/3
   quantidade = lata / 18

   preco = quantidade * 80.00
   print("serão compradas ", quantidade, " latas")
   return preco


area = float(input("digite quantos metros quadrados a área a ser pintada tem: "))

la = tinta(area)
print(la)