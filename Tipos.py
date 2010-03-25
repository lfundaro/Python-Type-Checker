#! /usr/bin/python

class Tipos(object):
    def __init__(self):
        self.nombre = 'Tipo'

class Int(Tipos):
    def __init__(self):
        super(Int, self).__init__()
        self.tipo = 'Int'

class Bool(Tipos):
    def __init__(self):
        super(Bool, self).__init__()
        self.tipo = 'Bool'

class a(Tipos):
    def __init__(self):
        super(a, self).__init__()
        self.tipo = 'variable de tipo'

class Tipo_Funcion(Tipos):
    def __init__(self, T1, T2):
        super(Tipo_Funcion, self).__init__()
        self.T1 = T1
        self.T2 = T2
        self.tipo = 'tipo de funcion'

class Tipo_parent(Tipos):
    def __init__(self, T1):
        super(Tipo_parent, self).__init__()
        self.T1 = T1
        self.tipo = 'Tipo parentizado'



        
