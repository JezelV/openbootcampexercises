from Calculadora import Calculadora

miCalculadora = Calculadora.Calculadora(10, 5)

print("Primer número: ", miCalculadora.getPrimerNumero())
print("Segundo número: ", miCalculadora.getSegundoNumero())
print("Suma: ", miCalculadora.sumar())
print("Resta: ", miCalculadora.restar())
print("Multiplicación: ", miCalculadora.multiplicar())
print("División: ", int(miCalculadora.dividir()))
