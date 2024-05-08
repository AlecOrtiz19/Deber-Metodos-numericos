import numpy as np


"""

k. Utilice un código de programación de Python para realizar los ejercicios g, h. 
Como resultado coloque el código, si no se ve bien, se puede colocar como imagen. 
Además, mostrar una gráfica en donde se pueda ver la gráfica original y la interpolación que obtuvieron. 
Agregar el cálculo del error relativo en el código.  

Ejercicio G
"""

x_datos = np.array([1, 2, 3, 4, 5])  
y_datos = np.array([1, 8, 27, 64, 125])  

def interpolacion_inversa_newton_tercer_grado(x_datos, y_datos, valor_deseado):
    n = len(x_datos)
    coeficientes = np.zeros(n)
    
    for i in range(n):
        coeficientes[i] = y_datos[i]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coeficientes[i] = (coeficientes[i] - coeficientes[i-1]) / (x_datos[i] - x_datos[i-j])

    resultado = coeficientes[-1]
    for i in range(n-2, -1, -1):
        resultado = resultado * (valor_deseado - x_datos[i]) + coeficientes[i]
    return resultado

valor_deseado = 2.25


x_estimado = interpolacion_inversa_newton_tercer_grado(y_datos, x_datos, valor_deseado)
print("Valor de x cuando f(x) =", valor_deseado, "es:", x_estimado)


f_x_real = np.interp(x_estimado, x_datos, y_datos)

error_relativo = abs((f_x_real - valor_deseado) / valor_deseado) * 100
print("Error relativo:", error_relativo, "%")
