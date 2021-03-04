#armando sequen
#0901-19-1801

#Una empresa de tecnologías vende memorias RAM a US$20.00 cada una. La
#memoria usada tiene un descuento del 60%. Escribir un programa que
#comience leyendo el número de Memorias RAM vendidas que no son nuevas.
#Después el programa debe mostrar el precio habitual de una memoria RAM
#nueva, el descuento que se le hace por no ser nueva y el coste final total

ram=int(input("memorias Ram compradas: "))
calculo=((60*20)/100)
descuento=ram*calculo
compra=ram*20

print("Presio de la Ram nueva es de Q.",20," por unidad")
print("precio de la Ram usada es de: Q.",calculo,"por unidad")
print("memorias Ram usadas y compradas",ram," unidades", "con un presio de Q.",descuento)
