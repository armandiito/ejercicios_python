#armando sequen
#0901-19-1801

#Escribir un programa en Python que lea un entero m, este debe ser
#introducido por el usuario y después muestre en pantalla la suma de todos
#los enteros desde 1 hasta m. La suma de los primeros enteros negativos
#puede ser calculada de la siguiente forma:
#suma =
#𝑚(𝑚 + 1)
#   2

numero=(int(input("introdusca un numero entero: ")))
  
suma=0    
for i in range(1, numero+1):
    suma=suma+i
  
print(f"la suma de los valores de 1 hasta {numero} es de: ", suma)