def relu(x):
    return max(0, x)

def neuron (inputs, weights, bias):
    z = 0 
    
#travels through the entrances of a neuron
    for i in range(len(inputs)):
        z += inputs[i] * weights[i]

    z += bias

    return relu(z)

inputs = [2, 4, 1, 3]

weights = [[0.2, -0.5, 0.8, 0.3],
           [-0.7, 0.4, 0.9, 0.8],
           [0.8, 0.9, -0.1, 0.7]
           ]
bias = [1, -2, 0]

outputs = []

#travels along the neurons
for i in range(len(weights)):
    output = neuron(inputs, weights[i], bias[i])
    outputs.append(output)

print(outputs)