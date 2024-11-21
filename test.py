# import torch


# # Функция активации (sigmoid)
# def activation_function(x):
#     return torch.sigmoid(x)


# # Класс персептрона
# class Perceptron:
#     def __init__(self, num_inputs):
#         # Инициализация весов случайными значениями
#         self.weights = torch.randn(num_inputs, dtype=torch.float64)
#         self.bias = torch.zeros(1, dtype=torch.float64)  # Инициализация смещения нулем

#     # Функция, вычисляющая выход персептрона
#     def feed_forward(self, inputs):
#         return activation_function(torch.sum(inputs * self.weights) + self.bias)

#     # Функция обучения персептрона
#     def train(self, inputs, target, learning_rate=0.1):
#         output = self.feed_forward(inputs)
#         print('output -- ',output)
#         error = target - output
#         # print('error -- ',error)
#         # Обновление весов и смещения
#         self.weights += error * inputs * learning_rate
#         # print('weights -- ',self.weights)
#         self.bias += error * learning_rate
#         # print('bias -- ',self.bias)


# # Основная функция
# if __name__ == "__main__":
#     # Создание персептрона с двумя входами
#     perceptron = Perceptron(2)

#     # Обучающие данные
#     training_inputs = torch.tensor(
#         [[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float64
#     )
#     training_outputs = torch.tensor(
#         [0, 1, 1, 1], dtype=torch.float64
#     )  # Логическая операция ИЛИ

#     # Обучение персептрона
#     for _ in range(100):
#         for inputs, target in zip(training_inputs, training_outputs):
#             perceptron.train(inputs, target)

#     # Проверка обученного персептрона
#     accuracy = 0
#     for inputs, target in zip(training_inputs, training_outputs):
#         output = perceptron.feed_forward(inputs)
#         print(f"Входы: {inputs.tolist()} Выход: {int(output)}")
#         accuracy += int(output.round() == target)
#     print(f"Accuracy: {accuracy / len(training_outputs)}")


import torch


def activation_function(x):
    return torch.tensor(1.0) if x >= 0 else torch.tensor(0.0)


# Класс персептрона
class Perceptron:
    def __init__(self, num_inputs):
        # Инициализация весов случайными значениями
        self.weights = (
            torch.randn(num_inputs, dtype=torch.float64) * 0.5
        )  # Уменьшенная инициализация весов
        self.bias = (
            torch.randn(1, dtype=torch.float64) * 0.5
        )  # Уменьшенная инициализация смещения
        # print(self.weights, self.bias)

    # Функция, вычисляющая выход персептрона
    def feed_forward(self, inputs):
        return activation_function(torch.sum(inputs * self.weights) + self.bias)

    # Функция обучения персептрона
    def train(self, inputs, target, learning_rate=0.1):
        output = self.feed_forward(inputs)
        error = target - output
        # print("output -- ", output)
        # print("error -- ", error)
        # Обновление весов и смещения
        self.weights += error * inputs * learning_rate
        # print("bias before -- ", self.bias)
        self.bias += error * learning_rate
        # print("weights -- ", self.weights)


# Основная функция
if __name__ == "__main__":
    # Создание персептрона с двумя входами
    perceptron = Perceptron(2)

    # Обучающие данные
    training_inputs = torch.tensor(
        [[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float64
    )
    training_outputs = torch.tensor(
        [0, 0, 0, 1], dtype=torch.float64
    )  # Логическая операция И

    # Обучение персептрона
    for _ in range(10):
        for inputs, target in zip(training_inputs, training_outputs):
            perceptron.train(inputs, target)

    # Проверка обученного персептрона
    for inputs, target in zip(training_inputs, training_outputs):
        output = perceptron.feed_forward(inputs)
        print(f"Входы: {inputs.tolist()} Выход: {int(output)}")
