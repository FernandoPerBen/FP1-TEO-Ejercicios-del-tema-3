alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"


def letra_a_posicion(letra: str):
    if letra in alfabeto:
        return alfabeto.find(letra)
    else:
        return None


def posicion_a_letra(posicion: int):
    if posicion >= 0 and posicion < len(alfabeto):
        return alfabeto[posicion]
    else:
        return None



def cifra_cesar(texto: str, clave: int) -> str:
    resultado = "" 

    for i in texto:
        pos = letra_a_posicion(i)

        if pos is not None:
            nueva_pos = (pos + clave) % len(alfabeto)
            resultado += posicion_a_letra(nueva_pos)
        else:
            resultado += i
    return resultado
