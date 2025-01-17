def OrdenarLista():
    '''Esta función crea un fichero llamado 'ListaOrdenada.txt' donde recibe y
    posteriormente escribe la lista de números que recibe, ordenada de mayor
    a menor'''
    lista = [3, 2, 4]
    fichero = open('ListaOrdenada.txt', 'w')
    fichero.write(lista)
    for numero in lista:
        lista.
    lista.sort()

def NumeroPar():
    '''Esta función abre un fichero que contiene una lista ordenada de números,
    los lee y los escribe en otro fichero 'ListaDePares.txt' solo los números
    pares del primer fichero'''
    