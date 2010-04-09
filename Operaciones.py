#! /usr/bin/python 

from Tipos import *
from Expresiones import *
from Excepciones import *

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
    try:
        # tipo1 entre parentesis.
        if isinstance(tipo1, Tipo_parent): return unif(tipo1.T1,tipo2)
	
        # tipo2 entre parentesis.
        if isinstance(tipo2, Tipo_parent): return unif(tipo1,tipo2.T1)
    
        # tipo1 es variable.
        if isinstance(tipo1, Var_tipo):
            # tipo2 es una funcion.
            if isinstance(tipo2, Tipo_Funcion):
                if tipo1.valor == tipo2.T1.valor:
                    raise UnifErr(tipo1, tipo2)
                else:
                    return [(tipo1, tipo2)]
            # tipo2 es una variable.
            elif isinstance(tipo2, Var_tipo):
                if tipo1.valor == tipo2.valor:
                    return ()
                else:
                    return (tipo1, tipo2)

            # tipo2 es un entero o booleano.
            else: return [(tipo1,tipo2)]
        
        # tipo1 es un entero, unifica consigo mismo.
        if isinstance(tipo1,Int):
            if isinstance(tipo2,Int): return []
            else: 
                if isinstance(tipo2, Bool):
                    raise UnifErr(tipo1, tipo2)
                else:
                    return unif(tipo2, tipo1)
        
    
        # tipo1 es un booleano, unifica consigo mismo
        if isinstance(tipo1,Bool):
            if isinstance(tipo2,Bool): return []
            else: raise UnifErr(tipo1, tipo2)
        
        # tipo1 es una funcion y tipo2 es una funcion.
        if isinstance(tipo1, Tipo_Funcion): 
            if isinstance(tipo2, Tipo_Funcion):
                w = unif(tipo1.T1, tipo2.T1)
                resultado = componer([w], unif(sustituir([w], tipo1.T2), sustituir([w], tipo2.T2)))
                return resultado
            elif isinstance(tipo2, Var_tipo):
                return unif(tipo2, tipo1)
            elif isinstance(tipo2, Bool) or isinstance(tipo2,Int):
                return unif(tipo2,tipo1)

    except UnifErr, e:
        tipo1 = e.tipo1
        tipo2 = e.tipo2
        print 'Error de unificacion entre ' + str(tipo1) + ' y ' + str(tipo2)


def vacio():
    raise AmbienteVacio("Variable no encontrada")

Vacio = lambda x: vacio()
extender = lambda tupla,Amb: lambda x: x == tupla[0].valor and tupla[1] or Amb(x)

def asigTipo(Amb, E, T):
    if isinstance(E, Entero):
        return unif(T, Int())
    elif isinstance(E, Booleano):
        return unif(T, Bool())
    elif isinstance(E, Var):
        try:
            return unif(T, Amb(E.valor))
        except AmbienteVacio, e:
            print e.messg
    elif isinstance(E, Suma):
        s1 = asigTipo(Amb, E.Exp1, Int())
        s2 = componer(s1, asigTipo(Amb, E.Exp2, Int()))
        return componer(s2, unif(T, Int()))
    elif isinstance(E, Menor):
        s1 = asigTipo(Amb, E.Exp1, Int())
        s2 = componer(s1, asigTipo(Amb, E.Exp2, Int()))
        return componer(s2, unif(T, Bool()))
    elif isinstance(E, Conjuncion):
        s1 = asigTipo(Amb, E.Exp1, Bool())
        s2 = componer(s1, asigTipo(Amb, E.Exp2, Bool()))
        return componer(s2, unif(T, Bool()))
    elif isinstance(E, Lambda):
        Amb1 = extender((Var('x'), Var_tipo('a')), Amb)
        a = Var_tipo('a')
        b = Var_tipo('b')
        s1 = asigTipo(Amb1, E, b)
        return componer(s1, unif(T, sustituir(s1, Tipo_Funcion(Var_tipo('a'), Var_tipo('b')))))
    elif isinstance(E, Aplicar):
        a = Var_tipo('a')
        s1 = asigTipo(Amb, E.Exp2, a)
        return componer(s1, asigTipo(Amb, E.Exp1, sustituir(s1, Tipo_Funcion(a, T))))

