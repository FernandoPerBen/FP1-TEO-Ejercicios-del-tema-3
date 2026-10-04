def estiliza_mensaje(texto:str, alterna_may_min:bool = True, usa_dieresis:bool=False, sustituye_espacios:str=""):
    """
    Alternar entre minuscula y mayuscula
    """
    resultado = ""
    hacer_mayuscula = True
    if alterna_may_min == True:
        for i in texto:
            if i.isalpha():
                if hacer_mayuscula:
                    resultado += i.upper()
                else:
                    resultado += i.lower()
                hacer_mayuscula = not hacer_mayuscula
            else:
                resultado += i

    """
    Usar dieresis en todas las vocales
    """        
    vocales = "aeiou"
    texto_dieresis = ""
    for i in texto:
        i = i.lower()
        for j in vocales:
            j = j.lower()
            if i == j:
                texto_dieresis = texto.replace("a","ä").replace("e","ë").replace("i","ï").replace("o","ö").replace("u","ü")
    """
    Cambiar espacios por *
    """
    texto_asteriscos = texto.replace(" ",sustituye_espacios)


    return resultado, texto_dieresis, texto_asteriscos
    

print(estiliza_mensaje("Hola mundo hay un murciélago", alterna_may_min=True, usa_dieresis=True, sustituye_espacios="*"))