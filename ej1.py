# funcion para comparar cadenas de texto, ignorando mayúsculas/minúsculas
def comparar_cadenas(cadena1, cadena2):
    if cadena1.lower() == cadena2.lower():
        return "Las cadenas son iguales"
    else:
        return "Las cadenas son diferentes"

# ejemplo de uso
cadena_a = "Hola"
cadena_b = "hola"
resultado = comparar_cadenas(cadena_a, cadena_b)
print(resultado)
