import numpy as np

class Neuron:
    # Get weights and bias
    def __init__(self,weights,bias):
        self.weights=weights
        self.bias=bias

    # Get feedforward with input neuron
    def feedforward(self,inputs):
        total = np.dot(self.weights,inputs)+self.bias
        return sigmoid (total)
        
# Sigmoid function
def sigmoid(x):
        return 1/(1+np.exp(-x))



inputs = np.array([1,0])
weight =np.array([0,1])
bias = 4 

neuron1=Neuron(weight,bias)

neuron2 = Neuron ()

print(neuron1.weights,neuron1.bias)
print(neuron1.feedforward(inputs))




