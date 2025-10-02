# funcion para comparar cadenas de texto
def comparar_cadenas(cadena1, cadena2):
    if cadena1 == cadena2:
        return "Las cadenas son iguales"
    else:
        return "Las cadenas son diferentes"

# ejemplo de uso
cadena_a = "Hola"
cadena_b = "Hola"
resultado = comparar_cadenas(cadena_a, cadena_b)
print(resultado)  # Salida: Las cadenas son iguales