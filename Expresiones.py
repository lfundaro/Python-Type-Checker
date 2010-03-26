#! /usr/bin/python 


###############################################
# Clase Expresiones de la cual herendan las   #
# expresiones del lenguaje, como: entero,     #
# booleano, var, etc                          #
###############################################
class Expresion(object):
    def __init__(self):
        self.nombre = 'expresion'

class Entero(Expresion):
    def __init__(self, valor):
        super(Entero, self).__init__()
        self.tipo = 'entero'
        self.valor = valor

class Booleano(Expresion):
    def __init__(self, valor):
        super(Booleano, self).__init__()
        self.tipo = 'booleano'
        self.valor = valor

class Var(Expresion):
    def __init__(self, valor):
        super(Var, self).__init__()
        self.tipo = 'var'
        self.valor = valor

class Suma(Expresion):
    def __init__(self, Exp1, Exp2):
        super(Suma, self).__init__(), 
        self.tipo = 'suma' 
        self.Exp1 = Exp1
        self.Exp2 = Exp2

class Menor(Expresion):
    def __init__(self, Exp1, Exp2):
        super(Menor, self).__init__()
        self.tipo = 'menor' 
        self.Exp1 = Exp1
        self.Exp2 = Exp2
        
class Conjuncion(Expresion):
    def __init__(self, Exp1, Exp2):
        super(Conjuncion, self).__init__()
        self.tipo = 'conjuncion' 
        self.Exp1 = Exp1
        self.Exp2 = Exp2

class Aplicar(Expresion):
    def __init__(self, Exp1, Exp2):
        super(Aplicar, self).__init__()
        self.tipo = 'aplicar'
        self.Exp1 = Exp1
        self.Exp2 = Exp2

class Lambda(Expresion):
    def __init__(self, var, Exp1):
        super(Lambda, self).__init__()
        self.tipo = 'lambda'
        self.var = var
        self.Exp1 = Exp1

class Expr_parent(Expresion):
    def __init__(self, Exp1):
        super(Expr_parent, self).__init__()
        self.tipo = 'Expresion parentizada'
        self.Exp1 = Exp1



