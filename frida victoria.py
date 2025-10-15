# grafico polinomial grado 4
#######################################################

import numpy as np
import matplotlib.pyplot as plt

# Definir el polinomio: P(x) = a*x^4 + b*x^3 + c*x^2 + d*x + e
def P(x, a, b, c, d, e):
    return a*x*4 + b*x3 + c*x*2 + d*x + e

# Coeficientes del polinomio (puedes cambiarlos)
a, b, c, d, e = 1, -3, 2, 5, -4

# Rango de valores de x
x_vals = np.linspace(-5, 5, 400)

# Evaluar el polinomio en cada x
y_vals = P(x_vals, a, b, c, d, e)

# Crear la gráfica
plt.plot(x_vals, y_vals, label=f'P(x) = ({a})x^4 + ({b})x^3 + ({c})x^2 + ({d})x + ({e})')
plt.axhline(0, color='black', linewidth=1) # Linea horizontal en y=0
plt.axvline(0, color='black', linewidth=1) # Linea vertical en x=0
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Grafico del polinomio de grado 4")
plt.show()