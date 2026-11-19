def invertir_string(cadena: str) -> str:
    reves = ""
    for i in cadena:
        reves = i + reves
    return reves

print(invertir_string("Hola"))