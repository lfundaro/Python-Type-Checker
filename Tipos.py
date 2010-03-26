#! /usr/bin/python

class Tipo(object):
    def __init__(self):
        self.nombre = 'Tipo'

class Int(Tipo):
    def __init__(self):
        super(Int, self).__init__()
        self.tipo = 'Int'

    def __str__(self):
        return 'Int'

class Bool(Tipo):
    def __init__(self):
        super(Bool, self).__init__()
        self.tipo = 'Bool'

    def __str__(self):
        return 'Bool'

class Var_tipo(Tipo):
    def __init__(self, valor):
        super(Var_tipo, self).__init__()
        self.tipo = 'variable de tipo'
        self.valor = valor

    def __str__(self):
        return self.valor
        
class Tipo_Funcion(Tipo):
    def __init__(self, T1, T2):
        super(Tipo_Funcion, self).__init__()
        self.T1 = T1
        self.T2 = T2
        self.tipo = 'tipo de funcion'

    def __str__(self):
        return str(self.T1) + ' --> ' + str(self.T2)

class Tipo_parent(Tipo):
    def __init__(self, T1):
        super(Tipo_parent, self).__init__()
        self.T1 = T1
        self.tipo = 'tipo parentizado'

    def __str__(self):
        return '(' + str(self.T1) + ')'


        
