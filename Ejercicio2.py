diccionario = {}
while True:
    opciones = int(input('Seleccione una de las siguientes opciones:\n'
                         '(1) Añadir alumno/a\n'
                         '(2) Número de aprobados\n'
                         '(3) Mostrar todo el alumnado\n'))
    if opciones == 1:
        nombrealumno = input("Nombre del alumno: ")
        aprobado = bool(int(input("Escribe 0 si el alumno ha suspendido, 1 si"
                                  " ha aprobado: \n")))
        diccionario[nombrealumno] = aprobado

    elif opciones == 2:
        aprobados = 0
        for aprobado in diccionario.values():
            if aprobado:
                aprobados += 1
        print("El número de aprobados es: " + str(aprobados) +"\n")
    elif opciones == 3:
        print(diccionario.keys())
    else:
        print("Ha marcado una opción inexistente\n")