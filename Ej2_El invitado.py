def invitados(archivo, modo):
    archivo = 'invitados.txt'
    with open(archivo, mode = modo) as file:
        b = str(input("introduzca nombre: "))
        print("hola que tal "+b)
        file.write(b+'\n')
    print(b)


if __name__ == '__main__':
    # Crea un archivo nuevo con un nombre
    file = 'invitados.txt'
    invitados(file,'w')
    invitados(file,'x')
    invitados(file,'a')


