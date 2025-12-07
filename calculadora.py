# Calculadora Simple 
# Programa de ejemplo para Git 
def sumar(a, b): 
return a + b 
def restar(a, b): 
return a - b 
def multiplicar(a, b): 
return a * b 
def dividir(a, b): 
if b != 0: 
return a / b 
else: 
return "Error: División por cero" 
# Pruebas 
print("Suma: 5 + 3 =", sumar(5, 3)) 
print("Resta: 5 - 3 =", restar(5, 3)) 
print("Multiplicación: 5 * 3 =", multiplicar(5, 3))
print("División: 5 / 3 =", dividir(5, 3))