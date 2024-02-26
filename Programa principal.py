def Consulta_raw(archivo):
    a = open(archivo, 'r')
    print(a.read())
    a.close()
def Consulta_lines(archivo):
    a = open(archivo)
    for line in a:
        print(line)
    a.close()
def Consulta_lines_with(archivo):
    with open(archivo) as file_object:
        s = file_object.readlines()
        l = []
        for line in s:
            l.append(line)

    print(l)

if __name__ == '__main__':
    # leyendo el fichero de manera completa
    file = 'consulta.txt'
    consulta_raw(file)
    print('*' * 75)
    consulta_lines(file)
    print('*' * 75)
    consulta_lines_with(file)
    print('*' * 75)

