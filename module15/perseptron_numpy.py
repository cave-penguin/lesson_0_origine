import numpy as np


class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=1000):
        # Инициализация весов и смещения
        self.weights = np.zeros(input_size)  # Веса для входных данных
        self.bias = 0  # Смещение
        self.learning_rate = learning_rate  # Скорость обучения
        self.epochs = epochs  # Количество итераций обучения

    def activation_function(self, x):
        # Функция активации (пороговая)
        return 1 if x >= 0 else 0

    def predict(self, x):
        # Вычисляем взвешенную сумму
        z = np.dot(x, self.weights) + self.bias
        return self.activation_function(z)

    def fit(self, X, y):
        """
        Обучение персептрона.
        X: матрица входных данных (размер n_samples x n_features)
        y: целевые метки (0 или 1)
        """
        for epoch in range(self.epochs):
            for i in range(len(X)):
                # Предсказание
                y_pred = self.predict(X[i])
                # Ошибка
                error = y[i] - y_pred
                # Обновление весов и смещения
                self.weights += self.learning_rate * error * X[i]
                self.bias += self.learning_rate * error

            # Вывод информации об обучении каждые 100 эпох
            if (epoch + 1) % 100 == 0:
                print(
                    f"Epoch {epoch + 1}/{self.epochs}, Weights: {self.weights}, Bias: {self.bias}"
                )


# Пример использования
if __name__ == "__main__":
    # Входные данные (например, логическая операция AND)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # Целевые метки
    y = np.array([0, 0, 0, 1])  # Логическая операция AND

    # Создаем и обучаем персептрон
    perceptron = Perceptron(input_size=2, learning_rate=0.1, epochs=1000)
    perceptron.fit(X, y)

    # Тестирование
    print("\nTesting:")
    for x in X:
        print(f"Input: {x}, Predicted: {perceptron.predict(x)}")
