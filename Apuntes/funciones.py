
#Esto es definir la función

def saludar():
    print("Hola")

#Luego hacemos el llamado de la función

saludar()

# Funciones que reciben parametros

def saludar2(name):
    print(f"Hola {name}")

#Hacemos el llamado a la función

saludar2("María")

#Cuando no conocemos el número de argumentos que requiere la función 

def VariosParametros(*args):
    print(f"Bienvenidos {args}")


VariosParametros("Pepito", "Luis", "Maria")




#Funciones con retorno:

def sumar(num1, num2):
    return num1 + num2

resultSuma = sumar(5,5)

print(resultSuma)



#Listas como argumentos

labels = {"Id", "Name", "List_Name", "email", "password"}
usuario = {"1","Pepito", "Perez", "pepito@gmail.com","xyz456789"}

def imprimirListas(lista):
    for i in range(len(lista)):
        print(lista[i])

imprimirListas(usuario)
imprimirListas(labels)