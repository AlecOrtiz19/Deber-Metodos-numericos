import numpy as np
import matplotlib.pyplot as plt


x_datos = np.array([1, 2, 3, 4, 5])  
y_datos = np.array([1, 8, 27, 64, 125])  

"""

k. Utilice un código de programación de Python para realizar los ejercicios g, h. 
Como resultado coloque el código, si no se ve bien, se puede colocar como imagen. 
Además, mostrar una gráfica en donde se pueda ver la gráfica original y la interpolación que obtuvieron. 
Agregar el cálculo del error relativo en el código.  

Ejercicio H

"""

def interpolacion_inversa_lagrange_tercer_grado(x_datos, y_datos, valor_deseado):
    n = len(x_datos)
    resultado = 0
    
    for i in range(n):
        termino = y_datos[i]
        for j in range(n):
            if i != j:
                numerador = valor_deseado - x_datos[j]
                denominador = x_datos[i] - x_datos[j]
                termino *= numerador / denominador
        resultado += termino
    return resultado

valor_deseado = 2.25

x_estimado = interpolacion_inversa_lagrange_tercer_grado(y_datos, x_datos, valor_deseado)
print("Valor de x cuando f(x) =", valor_deseado, "es:", x_estimado)

f_x_real = np.interp(x_estimado, y_datos, x_datos)

error_relativo = abs((f_x_real - valor_deseado) / valor_deseado) * 100
print("Error relativo:", error_relativo, "%")

plt.plot(x_datos, y_datos, 'bo-', label='Datos originales')
plt.plot(x_estimado, valor_deseado, 'ro', label='Interpolación')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación Inversa de Lagrange de Tercer Grado')
plt.legend()
plt.grid(True)
plt.show()
