#Procesador de Números.

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")
    
#Código mejorado
line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0

for substr in strings:
    try:
        total += float(substr)
    except ValueError:
        print(substr, "no es un número válido y será ignorado.")

print("El total es:", total)