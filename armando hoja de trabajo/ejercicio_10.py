# armando sequen
# 0901-19-1801

# Una ferretería tiene mucho éxito en dos de sus productos: barrenos y sierras
# eléctricas. Suele hacer venta por correo y la empresa de logística les cobra
# por peso de cada paquete así que deben calcular el peso de los barrenos y
# sierras que saldrán en cada paquete a demanda. Cada barreno pesa 112kg y
# cada sierra 75kg. Escribir un programa que lea el número de barrenos y
# sierras vendidos en el último pedido y calcule el peso total del paquete que
# será enviado.

opc1 = input("compro un barreno? (s/n): ")
if opc1 == "s":
    barreno = int(input("cuantos a adquirido: "))
else:
    barreno = 0

opc2 = input("compro una sierra? (s/n): ")
if opc2 == "s":
    sierra = int(input("cuantas a adquirido: "))
else:
    sierra = 0

peso_barreno = barreno*112
peso_sierra = sierra*75
total = peso_barreno+peso_sierra

print("la cantidad de barrenos es: ", barreno, " con un peso total de: ", peso_barreno, " kilogramos")
print("la cantidad de sierras es de: ", sierra," con un pero total de: ", peso_sierra, " kilogramos")
print("el total del paquete es de: ", total)
