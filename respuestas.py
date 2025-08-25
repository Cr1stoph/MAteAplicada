#Respuestas de la guia 1
import matplotlib.pyplot as plt
import numpy as np

def T(t):
    return -0.5 * t**2 + 3 * t + 20

x = np.arange(0,9,0.1) #esto define el rango, como vimos en el dominio de 0 a 9, lo mismo aqui
plt.plot(x,T(x), label = 'T(t)', color = 'purple') #label para el nombre de la funcion que en este caso es de T(t)
plt.title('Temperatura del servidor en funcion del iempo')
plt.xlabel('Tiempo (horas)') #independiente
plt.ylabel('Temperatura (°C)') #dependiente
plt.grid()
plt.legend()
#modificador de spines
ax = plt.gca()
ax.spines[['left','bottom']].set_position(('data',0))
ax.spines[['right', 'top']].set_visible(False)
plt.show()
