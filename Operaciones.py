#! /usr/bin/python 

from Tipos import *
from Expresiones import *
from Excepciones import *

# Funcion que recibe una lista de tuplas
# [(var de tipo, tipo),...] y un tipo T 
# y devuelve un tipo.
def sustituir(lista,T):
    for i in lista:
        T = sustituir_aux(i, T)
        return T
    

# Funcion auxiliar que se utiliza para sustituir
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

# Funcion que se utiliza para hacer match entre dos
# valores
def match(val1, val2):
    return val1 == val2

# Funcion que se utiliza para hacer la verificacion
# de que para todo par (x2, T2) de s2, x2 no ocurre 
# no ocurre en la parte izquierda de un par de s1. 
def not_member(var_tipo, s1):
    for par in s1:
        if var_tipo == par[0]:
            return False
        
    return True

# Hace la composicion de dos entre dos sustituciones
def componer(s1, s2):
    resultado = []
    # Por cada par (x1,T1) de s1
    # se hace (x1, sustituir(s2,T1)
    try:
        for par in s1:
            resultado.append((par[0], sustituir(s2, par[1])))

    # Se agregan los pares (x2,T2) tal que no este en s2
        for par in s2:
            if not_member(par[0], s1):
                resultado.append((par[0], par[1]))

        return resultado
    except TypeError:
        print "Error de Tipos"

# Se hace un chequeo de tipos para determinar 
# la regla de unificacion que se debe 
# utilizar para ciertos tipos.
def unif(tipo1, tipo2):
    try:
        # tipo1 entre parentesis.
        if isinstance(tipo1, Tipo_parent): return unif(tipo1.T1,tipo2)
	
        # tipo2 entre parentesis.
        if isinstance(tipo2, Tipo_parent): return unif(tipo1,tipo2.T1)
    
        # tipo1 es variable.
        if isinstance(tipo1, Var_tipo): return[(tipo1,tipo2)]
        
        # tipo1 es un entero, unifica consigo mismo.
        if isinstance(tipo1,Int):
            if isinstance(tipo2,Int): return [()]
            else: 
                if isinstance(tipo2, Bool):
                    raise UnifErr(tipo1, tipo2)
                else:
                    return unif(tipo2, tipo1)
        
    
        # tipo1 es un booleano, unifica consigo mismo
        if isinstance(tipo1,Bool):
            if isinstance(tipo2,Bool): return [()]
            else: 
                if isinstance(tipo2,Int):
                    raise UnifErr(tipo1, tipo2)
                else:
                    return unif(tipo2,tipo1)
					
        # tipo1 es una funcion y tipo2 es una funcion.
        if isinstance(tipo1, Tipo_Funcion): 
            if isinstance(tipo2, Tipo_Funcion):
                w = unif(tipo1.T1, tipo2.T1)
                resultado = componer(w, unif(sustituir(w, tipo1.T2), sustituir(w, tipo2.T2)))
                return resultado
            elif isinstance(tipo2, Var_tipo):
                return unif(tipo2, tipo1)
            elif isinstance(tipo2, Bool) or isinstance(tipo2,Int):
                return unif(tipo2,tipo1)
            
    except UnifErr, e:
        tipo1 = e.tipo1
        tipo2 = e.tipo2
        print 'Error de unificacion entre ' + str(tipo1) + ' y ' + str(tipo2)


# Funcion que se utiliza para levantar una excepcion 
# dentro de un lambda
def vacio():
    raise AmbienteVacio("Variable no encontrada")

# Ambiente Vacio
Vacio = lambda x: vacio()

# Operacion para extender un Ambiente
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
        return componer(s1, asigTipo(Amb, E.Exp1, Tipo_Funcion(sustituir(s1, a),T)))

def imprimir(lista):
    acorchete = '['
    ccorchete = ']'
    apar = '('
    cpar = ')'
    resultado = ''
    for i in lista:
        resultado = resultado + apar + str(i[0]) + ',' + str(i[1])+ cpar
    resultado = acorchete + resultado + ccorchete
    return resultado
        
