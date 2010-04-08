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

def unif(t1,t2):
	if isinstace(t1, Valor_tipo) and isinstance(t2,Valor_tipo):
		A = t1.valor
		B = t2.valor
		if A == B return True
		return False 
		
		
	