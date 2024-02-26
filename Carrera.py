# -*- coding: utf-8 -*-
import os

def carga_datos(archivo):
    # Cargamos el fichero y lo pasamos a una lista
    ListCod = []
    with open(archivo, 'r') as f:
        for linea in f:
            d, h, m, s, c = linea.split(';')
            t = [int(h), int(m), int(s), int(c)]  # pasamos tiempo a entero
            c = [int(d), tp_ct(t)]  # creamos código equipo, tiempo  ej. [2,5435]
            ListCod.append(c)
    return ListCod


def tp_ct(t):
    # creamos un código de tiemo para calcular tiempos de paso
    # pasamos el tiempo en hh:mm:ss:cc a centésimas de segundo
    temps = t[0] * 360000 + t[1] * 6000 + t[2] * 100 + t[3]
    return temps


def ct_tp(c):  # pasamos centésimas de segundo a h,min,seg,cent
    ss, cc = divmod(c, 100)
    mm, ss = divmod(ss, 60)
    hh, mm = divmod(mm, 60)
    return '%02d:%02d:%02d,%02d' % (hh, mm, ss, cc)


def vuelta_rapida_veh(carr, d):
    tant = 0  # tiempo de inicio de la primera vuelta
    v = 0  # numero de vuelta
    volta = 0  # numero de vuelta rápida
    for c in carr:  # recorremos toda la secuencia
        if c[0] == d:  # si el dorsal coincide, vemos tiempo.
            v += 1  # aumentamos vuelta
            if v == 1:  # caso particular la primera vuelta.
                tmv = c[1]  # tiempo de la primera vuelta
                volta = 1  # asumimos que la primera vuelta es la rápida
                tant = c[1]  # guardamos tiempo para cálculo siguiente
            else:
                tdif = c[1] - tant  # cálculo del siguiente tiempo de vuelta
                if tdif < tmv:  # comparamos con la mejor
                    tmv = tdif  # asumimos nuevo tiempo
                    volta = v  # asumimos nueva vuelta
                tant = c[1]  # guardamos tiempo para cálculo siguiente
    return volta, tmv  # se retorna mejor tiempo y no. de vuelta


def vuelta_rapida_carrera(carr):
    # para cada equipo, veremos su vuelta rápida.
    # al mismo tiempo, nos quedamos con el que tenga el mejor tiempo.
    for i in range(1, 16):
        vo, te = vuelta_rapida_veh(carr, i)
        if i == 1:  # caso particular: el primer equipo
            mvc = i, vo, te  # es el mejor equipo, mejor vuelta y mejor tiempo
            mte = te  # es el mejor tiempo
        else:
            if te < mte:  # si el tiempo del equipo es mas bajo que el mejor
                mvc = i, vo, te  # es el mejor equipo, mejor vuelta y mejor tiempo
                mte = te  # es el mejor tiempo
    return mvc


def imprime_clas(lista):  # imprime la lista de clasificación
    print('Posicion Equipo Vueltas      Tiempo')
    print('---------------------------------------')
    for i in range(1, len(lista)):
        dorsal, vueltas, tiempo = lista[i][0], lista[i][1][0], lista[i][1][1]
        print('%4d %8s %7s %16s ' % (i, dorsal, vueltas, ct_tp(tiempo)))


def classificacio(carr):  # calcula la clasificacion
    # Crear lista de equipos
    clas = {}
    for c in carr:
        # añadir una vuelta al dorsal y guardar el último tiempo
        if c[0] not in clas:
            clas[c[0]] = [1, c[1]]
        else:
            clas[c[0]][0] += 1
            clas[c[0]][1] = c[1]
    # pasamos el diccionario a lista
    lista = list(clas.items())
    # ordenar la lista

    lista.sort(reverse=True, key=lambda l: str(l[1][0]) + str(c[1] - l[1][1]))
    return lista


def main():
    """
    Programa principal  
    llamada a las funciones creadas
    
    """
    carr = carga_datos('codigos.txt')
    ok = False
    while not ok:  # obligamos a que el numero entrado sea correcto
        try:
            eq = int(input('entra dorsal (1 a 15):'))
            ok = eq >= 1 and eq <= 15
        except ValueError:
            ok = False
    print('\nVuelta rápida equipo %d ' % eq, end=' --> ')
    vo, te = vuelta_rapida_veh(carr, eq)
    print('vuelta %s en %s' % (vo, ct_tp(te)))
    mvc = vuelta_rapida_carrera(carr)
    print('\nvuelta rápida carrera')
    print('dorsal %2d en la vuelta %2d con un tiempo de %s\n' % (mvc[0], mvc[1], ct_tp(mvc[2])))
    print('Clasificiacion final')
    l = classificacio(carr)
    imprime_clas(l)


if __name__ == "__main__":
    main()
