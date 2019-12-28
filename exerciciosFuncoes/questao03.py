#calcular quantidade máxima de dados que um canal pode transmitir

def qdMax (v,a,d, c):
   qdmax = ((tvideo*5.2) + (taudio*3.4) + (tdados*1.5))/capacidade
   return qdmax

tvideo = float(input("digite a taxa de transmissão máxima de vídeo: "))
taudio = float(input("digite a taxa de transmissão máxima de audio: "))
tdados = float(input("digite a taxa de transmissão máxima de dados: "))
capacidade = float(input("digite a capacidade do canal controlado: "))


x = qdMax(tvideo, taudio, tdados, capacidade)
print("a quantidade máxima de dados a ser transmitida é: ", x)

