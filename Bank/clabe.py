
def generaClabe(casfim:str,region:str,acctNo:str,mode:bool) -> str:
    """Funcion que devuelve una cuenta clabe de 18 digitos"""
    clabe   = "" 
    clabe17 = casfim[2] + casfim[3] + casfim[4] + region + acctNo

    weights = (3,7,1) # Pesos definidos por Banxico
    total   = 0
    pos     = 0

    for cnt in range(0,len(clabe17)):
        if pos == 3:
            pos = 0
        result = int(clabe17[cnt]) * int(weights[pos]) # Se multiplica cada elemento de la clabe17 por 3,7,1,3,7,1...
        lastDigit = result % 10 # Se obtiene el residuo (modulo) de dividir entre 10
        total += lastDigit
        pos += 1

    verfyDigit = (10 - (total % 10)) % 10 # Formula Banxico
    clabe = str(clabe17) + str(verfyDigit) # Se agrega el dígito verificador

    if mode == False: # Cuenta invalida
        falseClabe = clabe[:6] + "9" + clabe[6 + 1:] # Se conservan los digitos del 0 al 5, se agrega 9 y se agrega el resto
        clabe = falseClabe

    return clabe
