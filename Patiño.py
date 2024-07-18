import csv
import math
import random

sueldos = {}

empleados = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
    "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

def asignar_sueldos():

    for empleado in empleados:
        sueldo = random.randint(300000, 2500000)
        sueldos[empleado] = sueldo

def clasificar_sueldos():

    clasificados = {
        "bajo_de_800k" : [],
        "entre_800k_y_2mill" : [],
        "arriba_de_2mill" : []
    }
    
    for empleado, sueldo in sueldos.items():
        if sueldo < 800000:
            clasificados["bajo_de_800k"].append((empleado, sueldo))
        elif 800000 <= sueldo <= 2000000:
            clasificados["entre_800k_y_2mill"].append((empleado, sueldo))
        else:
            clasificados["arriba_de_2mill"].append((empleado, sueldo))

    total_sueldos = 0

    for rango, lista in clasificados.items():
        total_sueldos += sum(sueldo for _,sueldo in lista)
        print("")
        if rango == 'bajo_de_800k':
            print('Sueldos bajo de $800.000: ')
            print("")
        else:
            
            if rango == 'entre_800k_y_2mill':
                print('Sueldos entre $800.000 y $2.000.000: ')
            else:
                print('Sueldos arriba de $2.000.000')
        
        print(f"Total de empleados en el rango: {len(lista)}")
        for empleado, sueldo in lista:
            
            print(f"{empleado}, sueldo: ${sueldo}")
    print("")
    print(f"Monto total de sueldos de todos los tranajadores: ${total_sueldos}")

def ver_estadisticas_de_sueldos():

    sueldos_valores = list(sueldos.values())
    sueldo_mas_alto = max(sueldos_valores)
    sueldo_mas_bajo = min(sueldos_valores)
    promedio_sueldos = sum(sueldos_valores) / len(sueldos_valores)
    medida_geometrica = math.exp(sum(math.log(sueldo)for sueldo in sueldos_valores) / len(sueldos_valores))

    print(f"Sueldo mas alto: ${sueldo_mas_alto}")
    print("")
    print(f"Sueldo mas bajo: ${sueldo_mas_bajo}")
    print("")
    print(f"Promedio total de sueldos entre todos los empleados: ${promedio_sueldos:.2f}")
    print("")
    print(f"Medida geometrica: ${medida_geometrica:.2f}")
    print("")

def informe_sueldos():

    with open('informe_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre completo","Sueldo bruto","Descuento salud","Descuento AFP", "Sueldo liquido"])

        for empleado, sueldo in sueldos.items():

            descuento_de_salud = sueldo * 0.7
            descuento_AFP = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_de_salud - descuento_AFP

            print(f"Nombre empleado: {empleado}")
            print(f"Sueldo bruto: ${sueldo}")
            print(f"Descuento salud: ${descuento_de_salud}")
            print(f"Descuento AFP: ${descuento_AFP}")
            print(f"Sueldo liquido: ${sueldo_liquido}")
            writer.writerow([empleado, sueldo, descuento_de_salud, descuento_AFP, sueldo_liquido])

def menu_principal():

    while True:

        print("")
        print("    ****Menu de gestion de empleados****    ")
        print("")
        print("1) Asignar sueldos aleatoriamente")
        print("2) Clasificar salarios")
        print("3) Ver estadisticas")
        print("4) Informe de sueldos")
        print("5) Salir del programa")
        print("")

        opcion = input("Seleccione una opción: ")
        print("")

        if opcion == '1':
            asignar_sueldos()
            print("Salarios asignados exitosamente")
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas_de_sueldos()
        elif opcion == '4':
            informe_sueldos()
        elif opcion == '5':
            print("Sesión cerrada con exito, cerrando el programa...")
            print("Desarrollado por Benjamin Patiño")
            print("RUT 21.675.999-0")
            break

if __name__ == "__main__":
    menu_principal()

