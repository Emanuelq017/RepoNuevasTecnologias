#Inicio Emmanuel


libros=[]

def menu():
    i = 1
    while i == 1:
        print("__________BIBLIOTECA__________")
        print("digite 1 para añadir un libro")
        print("digite 2 para mostrar los libros")
        print("digite 3 para salir")
        opcion = input("---> ")
        if opcion == "1":
            RegistroLibros()
        elif opcion == "2":
            print("Coco")
        elif opcion == "3":
            i=0

def llamar():
    RegistroLibros()

def RegistroLibros():
    nombre = input("Nombre del libro: ")
    autor = input("Autor del libro: ")
    genero = input("Genero del libro: ")

    nuevoLibro=[nombre,autor,genero]
    libros.append(nuevoLibro)
    print("Libro agrgado satisfactoriamente")
    continu = ""
    continu = input("Desea agregar otro libro (S/N) ")
    if continu == "S" or "s":
        llamar()
    elif continu == "N" or "n":
        menu() 



menu()


#Final Emmanuel