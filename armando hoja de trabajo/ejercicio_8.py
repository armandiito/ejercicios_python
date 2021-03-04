#armando sequen
#0901-19-1801

#Escribir un programa en Python que pida al usuario dos números flotantes y
#muestre por pantalla la <a> entre <b> da un cociente <c> y un resto <d>
#donde <a> y <b> son los números introducidos por el usuario, y <c> y <d>
#son el cociente y el resto de la división entera respectivamente.
import math

num1=float(input("ingrese el primer numero flotante: "))
num2=float(input("ingrese el segundo numero flotante: "))

resto=num1%num2
cociente=num1/num2

redondeo_resto=round(resto,2)
redondeo_cociente=round(cociente,2)

print("el resto de la division es: ",redondeo_resto)
print("el cociente de la division es: ",redondeo_cociente)
