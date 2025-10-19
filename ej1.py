# funcion para comparar cadenas de texto, ignorando mayúsculas/minúsculas
def comparar_cadenas(cadena1, cadena2):
    if cadena1.lower() == cadena2.lower():
        return "Las cadenas son iguales"
    else:
        return "Las cadenas son diferentes"

# función para contar cuántas veces aparece una palabra en una cadena
def contar_palabra(cadena, palabra):
    return cadena.lower().split().count(palabra.lower())

# ejemplo de uso
cadena_a = "Hola hola mundo hola"
palabra = "hola"
resultado_comparacion = comparar_cadenas("Hola", "hola")
resultado_cuenta = contar_palabra(cadena_a, palabra)

print(resultado_comparacion)
print(f'La palabra "{palabra}" aparece {resultado_cuenta} veces en la cadena.')
print(comparar_cadenas("Python", "python"))
