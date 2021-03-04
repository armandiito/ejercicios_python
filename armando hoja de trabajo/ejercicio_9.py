#armando sequen
#0901-19-1801

#Escribir un programa en Python que pregunte al usuario un monto a invertir,
#el interés anual y el número de años, y muestre por pantalla el capital
#obtenido en la inversión.

inversion=float(input("ingrese el monto a invertir: "))
anio=float(input("ingrese cuantos anios va invertir: "))

if inversion<=5000:
    porcentaje=1
    calculo=((inversion*porcentaje)/100)
    
    print("el interes por anio es de: ",calculo)
    print("la inversion de Q.",inversion," sus ganancias seran Q.",(calculo*anio)," durante", anio," anios")
    
if inversion>5000:
    porcentajet=2.5
    calculo=((inversion*porcentaje)/100)    
    
    print("el interes por anio es de: ",calculo)
    print("la inversion de Q.",inversion," sus ganancias seran Q.",(calculo(anio)," durante", anio," anios"))
    
