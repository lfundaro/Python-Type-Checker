#! /usr/bin/python 

from Tipos import *
from Expresiones import *

def sustitucion(lista,T):
    for i in lista:
        T = sustituir(i, T)
    return T

def sustituir(par, T):
    if isinstance(T, Var_tipo):
        if match(par[0].valor, T.valor):
            if isinstance(par[1], Tipo_Funcion):
                return Tipo_parent(par[1])
            else:
                return par[1]
        else:
            return T
    elif isinstance(T, Tipo_Funcion):
        A = sustituir(par, T.T1)
        B = sustituir(par, T.T2)
        return Tipo_Funcion(A,B)
    elif isinstance(T, Tipo_parent):
        A = sustituir(par, T.T1)
        return Tipo_parent(A)
    else:
        return T

def match(val1, val2):
    return val1 == val2

def not_member(var_tipo, s1):
    for par in s1:
        if var_tipo == par[0]:
            return False
        
    return True

def composicion(s1, s2):
    resultado = []
    # Por cada par (x1,T1) de s1
    # se hace (x1, sustitucion(s2,T1)
    for par in s1:
        resultado.append((par[0], sustitucion(s2, par[1])))

    # Se agregan los pares (x2,T2) tal que no este en s2
    for par in s2:
        if not_member(par[0], s1):
            resultado.append((par[0], par[1]))

    return resultado



            
        
        
    


