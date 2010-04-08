#! /usr/bin/python 

from Tipos import *
from Expresiones import *

def sustituir(lista,T):
    for i in lista:
        T = sustituir_aux(i, T)
    return T

def sustituir_aux(par, T):
    if isinstance(T, Var_tipo):
        if match(par[0].valor, T.valor):
            if isinstance(par[1], Tipo_Funcion):
                return Tipo_parent(par[1])
            else:
                return par[1]
        else:
            return T
    elif isinstance(T, Tipo_Funcion):
        A = sustituir_aux(par, T.T1)
        B = sustituir_aux(par, T.T2)
        return Tipo_Funcion(A,B)
    elif isinstance(T, Tipo_parent):
        A = sustituir_aux(par, T.T1)
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

def componer(s1, s2):
    resultado = []
    # Por cada par (x1,T1) de s1
    # se hace (x1, sustituir(s2,T1)
    for par in s1:
        resultado.append((par[0], sustituir(s2, par[1])))

    # Se agregan los pares (x2,T2) tal que no este en s2
    for par in s2:
        if not_member(par[0], s1):
            resultado.append((par[0], par[1]))

    return resultado

def unif(tipo1, tipo2):
    if isinstance(tipo1, Tipo_Funcion) and isinstance(tipo2, Tipo_Funcion):
        w = unif(tipo1.T1, tipo2.T1)
        resultado = componer([w], unif(sustituir([w], tipo1.T2), sustituir([w], tipo2.T2)))
        return resultado

    elif isinstance(tipo1, Tipo_Funcion) and isinstance(tipo2, Var_tipo):
        return unif(tipo2, tipo1)

    elif isinstance(tipo1, Var_tipo): 
        if isinstance(tipo2, Tipo_Funcion):
            if tipo1.valor == tipo2.T1.valor:
                return 'Error'
            else:
                return [(tipo1, tipo2)]
        elif isinstance(tipo2, Var_tipo):
            if tipo1.valor == tipo2.valor:
                return ()
            else:
                return (tipo1, tipo2)
        elif isinstance(tipo2, Int):
            return [(tipo1, tipo2)]
        elif isinstance(tipo2, Bool):
            return [(tipo1, tipo2)]
        elif isinstance(tipo2, Tipo_parent):
            return unif(tipo1, tipo2.T1)

    elif isinstance(tipo1, Int):
        if isinstance(tipo2, Int):
            return [(tipo1,tipo2)]


def lookup(lista, elem):
    for i in lista:
        if i[0].valor == elem:
            return i[1]

    return 'Ambiente vacio'


def asigTipo(Amb, E, T):
    if isinstance(E, Entero):
        return unif(T, Int())
    elif isinstance(E, Booleano):
        return unif(T, Bool())
    elif isinstance(E, Var):
        print 'hola'
        r = lookup(Amb,E)
        return unif(T, r)
    elif isinstance(E, Suma):
        s1 = asigTipo(Amb, E.Exp1, Int())
        print s1
        return ''
#        s2 = componer(s1, asigTipo(Amb, E.Exp2, Int()))
 #       return componer(s2, unif(T, int()))

            
        
        
    


