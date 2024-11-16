
import math

def binProbability(n,k,P):
    """Devuelve una probabilidad binomial dados el total de ensayos, casos de exito y probabilidad de exito"""
    if not(P>=0 and P<=1):
        raise ValueError # 0 <= P <= 1
    # Operaciones
    Q = (1-P) # Probabilidad de fracaso
    combnk = math.comb(n,k)
    result = combnk*(P**k)*(Q**(n-k))
    return result

def binProbAcc(n,x,P):
    result = 0
    for k in range(x+1):
        result += binProbability(n,k,P)
        
    return result