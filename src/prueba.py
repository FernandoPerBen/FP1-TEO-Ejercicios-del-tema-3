alf = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

def letra_a_posicion(letra):
    posicion = 0
    if letra in alf:
        posicion = alf.find(letra)
    else:
        return None
    return posicion

print(letra_a_posicion("h"))

def posicion_a_letra(pos):
    if pos >= 0 and pos <= len(alf):
        res = ""
        res = alf[pos]
    else:
        return None
    return res

print(posicion_a_letra(-1))