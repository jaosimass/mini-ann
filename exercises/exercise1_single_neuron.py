def relu(x):
    return max(0, x)

inputs = [1, 5]

weights = [2, -7]

bias = -2

z = (
    inputs[0] * weights[0] + inputs[1] * weights[1] + bias
)

output = relu(z)

print(f"Resultado antes da ativação: {z}"  )
print(f"Saída do neurônio: {output}" )