print("Ejemplos funciones")

def hola():
    print("Alguien habla")
def chat(msg):
    print(f"Chat el: {msg}")
def ellacontesta(msg):
    print(f"Chat ella: {msg}")
def escribenombre(ap, n):
    print(f"Tu nombre completo es: {n} {ap}")
def suma(a,b):
    s = a + b
    return s
def resta(a,b):
    s = a - b
    return s
def multiplicacion(a,b):
    s = a * b
    return s
def division(a,b):
    s = a / b
    return s 

hola()
chat("Que bonita estas")
ellacontesta("Gracias")
escribenombre("Flores Rodríguez", "Jesús Daniel")
print("Operaciones basicas")

c1 = int(input("Ingresa un numero: "))
c2 = int(input("Ingresa otro numero: "))
damesuma = suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

c3 = int(input("Ingresa un numero: "))
c4 = int(input("Ingresa otro numero: "))
dameresta = resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")

c5 = int(input("Ingresa un numero: "))
c6 = int(input("Ingresa otro numero: "))
damemultiplicacion = multiplicacion(c5,c6)
print(f"La multiplicacion de {c5} x {c6} = {damemultiplicacion}")

c7 = float(input("Ingresa un numero: "))
c8 = float(input("Ingresa otro numero: "))
damedivision = division(c7,c8)
print(f"La division de {c7} / {c8} = {damedivision}")