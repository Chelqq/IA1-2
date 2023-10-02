"""
Actividad: A02. El Algoritmo del Perceptron
Inteligencia Artificial 2
"""

import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, n_input, learning_rate):
        self.w = -1 + 2 * np.random.rand(n_input)
        self.b = -1 + 2 * np.random.rand()
        self.eta = learning_rate


    def predict(self, X):
        p = X.shape[1]
        y_est = np.zeros(p)

        for i in range(p):
            y_est[i] = np.dot(self.w, X[:, i]) + self.b
            if(y_est[i]) >= 0:
                y_est[i] = 1
            else:
                y_est[i] = 0

        return y_est


    def fit(self, X, Y, epochs = 50):
        p = X.shape[1]
        for _ in range(epochs):
            for i in range(p):
                y_est = self.predict(X[:, i].reshape(-1, 1))
                self.w += self.eta * (Y[i] - y_est) * X[:, i]
                self.b += self.eta * (Y[i] - y_est)


# *************** Ejercicio Compuertas Logicas ***************
#   Compuerta AND
X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
Y = np.array([0, 0, 0, 1])

#   Compuerta OR
#X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
#Y = np.array([0, 1, 1, 1])

#   Compuerta XOR
#X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
#Y = np.array([0, 1, 1, 0])


neuron= Perceptron(2, 0.1)
neuron.fit(X, Y)


# *************** Grafica ***************
# Dibuja la linea que separa las dos clases
def draw_2d(model):
    w1, w2, b = model.w[0], model.w[1], model.b
    plt.plot([-2, 2], [(1/w2) * (-w1 * (-2)-b), (1/w2) * (-w1 * 2 -b)], '--k')

# Se dibuja cada uno de los puntos
_, p = X.shape
for i in range(p):
    if Y[i] == 0:
        plt.plot(X[0, i], X[1, i], 'or') #punto rojo
    else:
        plt.plot(X[0, i], X[1, i], 'ob') #punto azul

plt.title('Perceptron')
plt.grid('on')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

draw_2d(neuron)


# *************** Ejercicio Sobrepeso ***************
# Creacion de dataset de entrenamiento
training_heights = np.random.uniform(1.5, 2.0, size=(100, 1))
training_weights = np.random.uniform(40, 120, size=(100, 1))
training_imc = training_weights / (training_heights ** 2)

X = (training_imc - training_imc.min()) / (training_imc.max() - training_imc.min())
Y = np.where(training_imc > 25, 1, -1)

overweight_training_neuron = Perceptron(100, 0.1)
overweight_training_neuron.fit(X, Y)


plt.title('Perceptron')
plt.grid('on')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel(r'IMC')
plt.ylabel(r'Sobrepeso')

draw_2d(overweight_training_neuron)
plt.scatter(X[:,0], Y, c=Y)
plt.plot(X[:,0], overweight_training_neuron.predict(X), c='r')