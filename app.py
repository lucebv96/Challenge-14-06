# Solicitamos al usuario que ingrese los números
numeros = input("Ingrese una lista de números separados por comas: ")

# Convertimos la cadena de entrada en una lista de enteros
numeros_lista = [int(num) for num in numeros.split(",")]  #Usamos el método split(",") para dividir la cadena en una lista

# Ordenamos la lista en orden ascendente
numeros_lista.sort()  # Usamos el método sort()  para ordenar numeros_lista en orden ascendente.

# Mostramos la lista ordenada
print("Lista de números ordenada en orden ascendente:", numeros_lista)