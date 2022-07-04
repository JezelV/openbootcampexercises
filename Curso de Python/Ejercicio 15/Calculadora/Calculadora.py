# *En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

class Calculadora:

    # Constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Getters
    def getPrimerNumero(self):
        return self.num1
    
    def getSegundoNumero(self):
        return self.num2
    
    # Methods
    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        return self.num1 / self.num2
