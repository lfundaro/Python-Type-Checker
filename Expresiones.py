#! /usr/bin/python 


###############################################
# Clase Expresiones de la cual herendan las   #
# expresiones del lenguaje, como: entero,     #
# booleano, var, etc                          #
###############################################
class Expresiones(object):
    def __init__(self):
        self.nombre = 'Expresion'

class Entero(Expresiones):
    def __init__(self):
        super(Entero, self).__init__()
        self.tipo = 'entero'

class Booleano(Expresiones):
    def __init__(self):
        super(Booleano, self).__init__()
        self.tipo = 'booleano'

class Var(Expresiones):
    def __init__(self):
        super(Var, self).__init__()
        self.tipo = 'var'

class Suma(Expresiones):
    def __init__(self, Exp1, Exp2):
        super(Suma, self).__init__(), 
        self.tipo = 'suma' 
        self.Exp1 = Exp1
        self.Exp2 = Exp2

class Menor(Expresiones):
    def __init__(self, Exp1, Exp2):
        super(Menor, self).__init__()
        self.tipo = 'menor' 
        self.Exp1 = Exp1
        self.Exp2 = Exp2
        
class Conjuncion(Expresiones):
    def __init__(self, Exp1, Exp2):
        super(Conjuncion, self).__init__()
        self.tipo = 'conjuncion' 
        self.Exp1 = Exp1
        self.Exp2 = Exp2

class Aplicar(Expresiones):
    def __init__(self, Exp1, Exp2):
        super(Aplicar, self).__init__()
        self.tipo = 'aplicar'
        self.Exp1 = Exp1
        self.Exp2 = Exp2

class Lambda(Expresiones):
    def __init__(self, var, Exp1):
        super(Lambda, self).__init__()
        self.tipo = 'lambda'
        self.var = var
        self.Exp1 = Exp1

class Expr_parent(Expresiones):
    def __init__(self, Exp1):
        super(Expr_parent, self).__init__()
        self.tipo = 'Expresion parentizada'
        self.Exp1 = Exp1



