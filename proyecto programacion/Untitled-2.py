import json
import os


class _main:

    ruta_datos = "C:/Users/ctand/OneDrive/Documentos/ArchivosPython/proyecto programacion/datos.json"



    def leer_datos():
        try:
            with open(ruta_datos, 'r') as archivo:
                lista_paisesMedalleros = json.load(archivo)
                return lista_paisesMedalleros
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def agregar_paisMedallero(pais, disciplina, medalla):

        medalleros =leer_datos()
        pais_medalla = {'pais': pais, 'disciplina': disciplina, 'medalla': medalla}
        medalleros.append(pais_medalla)
        escribir_datos(medalleros)

    def escribir_datos(medalleros):
        with open(ruta_datos, 'w') as archivo:
            json.dump(medalleros,archivo,indent=4)

    def mostrar_paisesMedalleros():
        paises = leer_datos()
        for pais in paises:
            print(f"País: {pais['pais']}, Disciplina: {pais['disciplina']}, Medalla: {pais['medalla']}")

    def menu():
        print("")
        print("Menú:")
        print("1. Mostrar un pais y sus medallas")
        print("2. Agregar pais medallero")
        print("3. Salir")
        
    # Crear el directorio si no existe
    directorio = os.path.dirname(ruta_datos)
    if not os.path.exists(directorio):
        os.makedirs(directorio)
        
        
        
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
            
        if opcion == "1":
            mostrar_paisesMedalleros()
        elif opcion == "2":
            pais = str(input("Ingrese el pais: "))
            disciplina = str(input("Ingrese la disciplina: "))
            medalla = str(input("Ingrese la medalla: "))
            agregar_paisMedallero(pais, disciplina, medalla)

        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            
            
            
