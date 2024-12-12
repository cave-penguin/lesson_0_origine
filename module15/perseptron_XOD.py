import numpy as np

# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# y = np.array([[0], [1], [1], [0]])

# input_size = 2
# hidden_size = 2
# output_size = 1

# np.random.seed(0)

# weights_input_hidden = np.random.rand(input_size, hidden_size)

# weights_hidden_output = np.random.rand(hidden_size, output_size)


# bias_hidden = np.random.rand(hidden_size)
# bias_output = np.random.rand(output_size)


# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))


# def sigmoid_derivative(x):
#     return x * (1 - x)


# learning_rate = 0.1
# epochs = 10

# for epoch in range(epochs):
#     hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
#     hidden_layer_output = sigmoid(hidden_layer_input)
#     print(hidden_layer_input)

#     output_layer_input = (
#         np.dot(hidden_layer_output, weights_hidden_output) + bias_output
#     )
#     predicted_output = sigmoid(output_layer_input)

#     error = y - predicted_output
#     d_predicted_output = error * sigmoid_derivative(predicted_output)

#     error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
#     d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

#     weights_hidden_output += (
#         hidden_layer_output.T.dot(d_predicted_output) * learning_rate
#     )
#     bias_output += np.sum(d_predicted_output, axis=0) * learning_rate
#     weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate
#     bias_hidden += np.sum(d_hidden_layer, axis=0) * learning_rate


# # Тестирование
# hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
# hidden_layer_output = sigmoid(hidden_layer_input)

# output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
# predicted_output = sigmoid(output_layer_input)

# print(predicted_output)  # Ожидаемые значения близки к [0, 1, 1, 0]


def act(x):
    return 0 if x < 0.5 else 1


def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11, w12])
    weight2 = np.array([-1,1])
    
    sum_hidden = np.dot(weight1, x)
    print('Значения сумм на нейронах скрытого слоя: '+str(sum_hidden))
    
    out_hidden = np.array([act(x) for x in sum_hidden])
    print('Значения на выходах скрытого слоя: '+str(out_hidden))
    
    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print('Выходное значение НС: '+str(y))
    
    return y

house = 1
rock = 0
attr = 1

res = go(house, rock, attr)
if res == 1:
    print('Ты мне нравишься')
else:
    print('Созвонимся')