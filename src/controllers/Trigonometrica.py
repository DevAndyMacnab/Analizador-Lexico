from controllers.abstract import Expression
from math import *

class Trigonometricas(Expression):
    def __init__ (self,left,tipo,fila,columna):
        self.left=left
        self.tipo=tipo
        super().__init__(fila,columna)
        
    def operar(self,arbol):
        leftValue=""
        if self.left!=None:
            leftValue=self.left.operar(arbol)
            
        if self.tipo.operar(arbol)=="Seno":
            return sin(leftValue)
        elif self.tipo.operar(arbol)=="Coseno":
            return cos(leftValue)
        elif self.tipo.operar(arbol)=="Tangente":
            return tan(leftValue)
        else:
            return 0
    
    def getColumna(self):
        return super().getColumna()
    
    def getFila(self):
        return super().getFila()