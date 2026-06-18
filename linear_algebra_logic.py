import numpy as np

# Function that returns the polinomial coeficents

column = []


def coef(x, y, degree):
    for i in range(degree + 1):
        nova_column = x ** i
        column.append(nova_column)

    # Definindo a matriz x
    matriz_x = np.array(column).T
    matriz_y = y.T
    matrix_aux1 = np.dot(matriz_x.T, matriz_x)
    matrix_aux2 = np.linalg.inv(matrix_aux1)
    matrix_aux3 = np.dot(matrix_aux2, matriz_x.T)
    coeficient = np.dot(matrix_aux3, matriz_y)
    return coeficient


# Returns a polynomial function based on the given coefficients
def polynomial_value(coefficients):
    def function(x):
        result = 0
        for i, c in enumerate(coefficients):  # Onde i são os indices do vetor coef, e c são os valores do coef
            result += c * (x ** i)
        return result

    return function