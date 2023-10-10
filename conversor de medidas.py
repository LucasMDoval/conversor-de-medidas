# Solicitar al usuario ingresar un valor numérico
valor = float(input("Ingrese un valor a convertir: "))

# Funciones para realizar las conversiones de unidades de longitud
def metros_a_pies(metros):
    resultado_pies = metros * 3.281
    return resultado_pies

def centimetros_a_pulgadas(centimetros):
    resultado_pulgadas = centimetros * 0.394
    return resultado_pulgadas

def kilometros_a_millas(kilometros):
    resultado_millas = kilometros * 0.621
    return resultado_millas

# Función para mostrar las opciones de conversión y realizar la conversión
def menu_de_conversion():
    print("Seleccione una opción de conversión:")
    print("1. Metros a Pies")
    print("2. Centímetros a Pulgadas")
    print("3. Kilómetros a Millas")
    opcion = input("Ingrese el número de la opción deseada: ")
    
    if opcion == "1":
        resultado = metros_a_pies(valor)
        print(f"{valor} metros son aproximadamente {resultado} pies.")
    elif opcion == "2":
        resultado = centimetros_a_pulgadas(valor)
        print(f"{valor} centímetros son aproximadamente {resultado} pulgadas.")
    elif opcion == "3":
        resultado = kilometros_a_millas(valor)
        print(f"{valor} kilómetros son aproximadamente {resultado} millas.")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

# Llamar a la función para mostrar el menú de conversión y realizar la conversión
menu_de_conversion()
