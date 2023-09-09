# Las listas son estructuras de datos lineales
# Se cren usando bkackes ej: my_list = [1,2]
# Las listas son ordenadas, esto quiere decir que el ultimo dato ingresado ocupará la ultima posisicón
# Emplea métodos para manipular los items de la misma.
# Como los array, la primera posición inicia en 0
# Permite items duplicados
# Las listas son mutables, es deceir podemos agregar, actualizar o remover items
# Puede contener distintos tipos de datos

nombres = ["Luis", "Andres", "Juan", "Maria", "Pedro"]
edad = [25,19,21,33,40]
estatura = [1.80, 1.65, 1.74, 1.66, 1.54]
casado = [False,False,False,True,True]
usuario = ["Pepito",25,1.80,False]


print(len(edad))

print(type(nombres))
print(type(edad))
print(type(estatura))
print(type(casado))
print(type(usuario))


#Slice
print(usuario[0:3])


#Validar si existe en la lista alguún elemento

if "Pepito" in nombres:
    print(f"El nombre {nombres[0]} esta en la lista")
else:
    print("No se encontro el nombre buscado")

nombres[0: 3] = "Luis", "Pablo", "Pipe"    
print(nombres[0:5])


#Queremos insertar un item en una posición especifica => insert(i,value)
nombres.insert(0,"Pepito")


#Podemos agregar items al final de la lista con .append()
nombres.append("Laura")
print(nombres[0: ])


nombres2 = ["Luis", "Ana"]

listapureba = nombres.extend(nombres2)
print(nombres[0:])
print(type(listapureba))

nombres.remove("Lis")
print(nombres[0:])

nombres.pop(4)
print(nombres[0:])

del nombres[1]
print(nombres[0:])

nombres.clear()
print(nombres[0:])

# Recorrer Listas

for i in edad:
    print(i)

# Iterar en los index

for i in range(len(estatura)):
    print(estatura[i])

# Iterar la lista  usando While

i = 0

while i < len(usuario):
    print(usuario[i])
    i += 1

# List Comprenhensions

print("---------------------")
[print(x) for x in usuario]
print("---------------------")
for i, edades in enumerate(edad):
    print(i, edades)