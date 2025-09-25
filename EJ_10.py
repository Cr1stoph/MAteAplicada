print("------------Pregunta 1----------------")
import numpy as np

vi = [1, 6]
vd = [2600, 15600]
m1, n1 = np.polyfit(vi, vd, 1)
m = round(m1)
n = round(n1)
print(f"La forma algebraica de la funcion es: I(x) = {m}x + {n}")

vin = [5, 8]
vdep = [7900, 10600]
m2, n2 = np.polyfit(vin, vdep, 1)

m1 = round(m2)
n2 = round(n2)
print(f"la funcion es: C(x): {m1}x + {n2} ")
def C(x): #Calcula el costo
    return 900 * x + 3400
def I(x): #calcula el ingreso
    return 2600 * x

print(C(63)) #Costo
print(I(1000)) #Ingreso
