# Ejercicio 1
# Escribe un programa que pregunte al usuario su edad y diga si es mayor o menor de
# edad (18 años). Puedes usar input(“Inserta algo: ”) para pedir al usuario datos.

# edad = int(input("Por favor, introduce tu edad: "))
#
# if edad >= 18:
#        print("Eres mayor de edad:")
# else:
#        print("Eres menor de edad.")


#Ejercicio 2
# Escribe un programa que pregunte al usuario su número de teléfono. Si contiene 9
# caracteres saldrá un mensaje de que está bien, si no saldrá un mensaje de error

# telefono =input("Por favor, introduce tu número de teléfono: ")
# if len(telefono) ==9:
#        print("El número de teléfono está bien.")
# else:
#        print("Error: El número de teléfono debe contener exactamente 9 caracteres.")

#Ejercicio 4
# Escribe un programa que le pregunte al usuario los grados Celsius que hace
# actualmente. Después hay que convertir los Celsius a Fahrenheit.
# Por último, si los grados Fahrenheit son más de 77.1 debe salir un mensaje diciendo que
# calor hace, si está entre 65 y 73.3 saldrá un mensaje diciendo que hace buena
# temperatura, y si es menor de 65 un mensaje que diga que hace frío.

# celsius =float(input("Dime los grados celsius por favor: "))
# fahrenheit = (celsius * 9/5) + 32
#
# print((f"La temperatura Fahrenheit es: {fahrenheit:.1f}ºF"))
#
# if fahrenheit > 77.1:
#        print("Qué calor hace!")
# elif 65 <= fahrenheit <= 73.3:
#        print("Hace buena temperatura.")
# else:
#        print("Hace frío.")

#FOR
# Ejercicio 1
# Escribe un programa que cuente números del 1 al 1000 (puedes usar range(1,1001))

# for numero in range(1, 1001):
#     print(numero)


# Ejercicio 2
# Escribe un programa que pida al usuario un número y saque el factorial de ese número

# número = int(input("Ingresa un número para calcular su factorial: "))
# factorial = 1
# for i in range(1, número + 1):
#     factorial *= i
#
# print(f"El factorial de {número} es {factorial}")

# Ejercicio 3
# Escribe un programa que pida al usuario 5 nombres, los guarde en una lista y luego los
# imprima por pantalla (puedes usar lista.append(“Pepe”))

# Crear una lista vacía para almacenar los nombres
 nombres = []

 for i in range(5):
     nombre = input(f"Introduce el nombre {i + 1}: ")
     nombres.append(nombre)  # Agregar el nombre a la lista

 print("\nLos nombres introducidos son:")
 for nombre in nombres:
     print(nombre)

# Ejercicio 5
# Por último, añádele al programa anterior que cuente las letras que tiene, luego imprimirá
# un mensaje diciendo si el nombre es par o impar. Ej:
# El nombre: Javi – Contiene 4 letras y es par
# El nombre: Leire – Contiene 5 letras y es impar



























