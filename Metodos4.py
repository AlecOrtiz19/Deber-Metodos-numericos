import numpy as np
import matplotlib.pyplot as plt

x_datos = np.array([2,3, 4, 5])  
y_datos = np.array([1.90, 1.90, 2.40, 2.79])  

"""
Utilice un código de programación de Python para realizar los ejercicios b, c, d, e. 
Como resultado coloque el código, si no se ve bien, se puede colocar como imagen. Además, 

Ejercicio E

"""

y_real = 2.0 

def lagrange_tercer_grado(x, x_datos, y_datos):
    n = len(x_datos)
    resultado = 0
    for i in range(n):
        termino = y_datos[i]
        for j in range(n):
            if i != j:
                numerador = x - x_datos[j]
                denominador = x_datos[i] - x_datos[j]
                termino *= numerador / denominador
        resultado += termino
    return resultado

x_estimado = 3.3
y_estimado = lagrange_tercer_grado(x_estimado, x_datos, y_datos)
print("Estimación para x = 3.3:", y_estimado)
error_relativo = abs((y_real - y_estimado) / y_real) * 100

print("Error relativo:", error_relativo, "%")

x_valores = np.linspace(min(x_datos), max(x_datos), 100)
y_valores = lagrange_tercer_grado(x_valores, x_datos, y_datos)

plt.plot(x_valores, y_valores, label='Polinomio de interpolación de Lagrange')
plt.scatter(x_datos, y_datos, color='red', label='Datos conocidos')
plt.scatter(x_estimado, y_estimado, color='green', label=f'Estimación para x={x_estimado}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de Lagrange de tercer grado')
plt.legend()
plt.grid(True)
plt.show()
