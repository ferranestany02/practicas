while True:
    try:
        x = int(input("Porfavor entra un dato entero: "))
        y = int(input("Porfavor entra otro dato entero: "))
        print('Division =', (x/y))
        break
    except ValueError:
        print("oops, esto no es un entero, prueba otra vez")
    except ZeroDivisionError:
        print("oops, no puedo dividir entre 0")



