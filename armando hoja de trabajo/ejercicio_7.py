#armando sequen
#0901-19-1801

#Escribir un programa en Python que pida al usuario su peso (en libras) y
#estatura (en metros), calcule el índice de masa corporal y lo almacene en una
#variable, y muestre por consola la frase Tu índice de masa corporal es <imc>
#donde <imc> es el índice de masa corporal calculado redondeado con dos
#decimales

import math

lbs=(int(input("introdusca su peso en libras: ")))
altura=(float(input("introdusca su altura en metros: ")))

constante=2.2046
kg=lbs/constante

imc=kg/(altura*altura)
redondeado=round(imc, 2)

print("Tu indice de masa corporal es de: ",redondeado)