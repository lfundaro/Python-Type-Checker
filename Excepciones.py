#! /usr/bin/python

class AmbienteVacio(Exception):
    def __init__(self, messg):
        self.messg = messg

class UnifErr(Exception):
    def __init__(self, tipo1, tipo2):
        self.tipo1 = tipo1
        self.tipo2 = tipo2
