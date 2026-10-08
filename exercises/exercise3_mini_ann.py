# Mini Artificial Neural Network (ANN)
# Architecture: 4 inputs -> 3 hidden neurons -> 1 output neuron
# Hidden activation: ReLU
# Output activation: Sigmoid
# Implemented from scratch without ML libraries

import math

def relu(x):
    return max(0, x)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def neuron (inputs, weights, bias):
    z = 0 
    
# iterates through the neuron's inputs
    for i in range(len(inputs)):
        z += inputs[i] * weights[i]

    z += bias

    return relu(z)

def output_neuron(inputs, weights, bias):
    z = 0

    for i in range(len(inputs)):
        z += inputs[i] * weights[i]

    z += bias

    return sigmoid(z)

inputs = [2, 4, 1, 3]

weights = [[0.2, -0.5, 0.8, 0.3],
           [-0.7, 0.4, 0.9, 0.8],
           [0.8, 0.9, -0.1, 0.7]
           ]
bias = [1, -2, 0]

outputs = []

# iterates through the neurons in the hidden layer
for i in range(len(weights)):
    output = neuron(inputs, weights[i], bias[i])
    outputs.append(output)

print("hidden layer outputs: ", outputs)

output_weights = [0.5, -0.2, 0.3]
output_bias = -1

final_output = output_neuron(
    outputs,
    output_weights,
    output_bias
)

print("final network output", final_output)