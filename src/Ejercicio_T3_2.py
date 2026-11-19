from Ejercicio_T3_1 import invertir_string

def es_palindromo():
    texto = input("Escribe un palindromo: ").lower().replace(" ","")
    return texto == invertir_string(texto)

print(es_palindromo())

# def es_palindromo():
#     texto = input("Escribe un palindromo: ").lower().replace(" ","")
#     return texto == texto[::-1]

# print(es_palindromo())
