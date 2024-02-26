def libro_visitas(archivo):
    archivo = 'libro_visitas.txt'
    with open(archivo, 'a') as file:
        while True:
            nombre = input("Introduzca el nombre: ")
            if nombre == '':
                print("Saliendo del programa..")
                break
            else:
                print(f"Bienvenido, {nombre}!")
                file.write(nombre + '\n')

if __name__ == '__main__':
    from consulta import consulta_lines as listado
    file = 'libro_firmas.txt'
    libro_visitas(file)
    listado(file)


