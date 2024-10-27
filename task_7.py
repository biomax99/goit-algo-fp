import random
import matplotlib.pyplot as plt
import pandas as pd

# Функція для симуляції кидків кубиків і підрахунку ймовірностей
def monte_carlo_simulation(num_rolls=100000):
    outcomes = [0] * 13  # Ініціалізуємо масив для підрахунку частот сум від 2 до 12

    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        outcomes[roll_sum] += 1

    # Обчислення ймовірностей для кожної суми
    probabilities = {sum_: (count / num_rolls) * 100 for sum_, count in enumerate(outcomes) if sum_ >= 2}
    return probabilities

# Функція для порівняння з аналітичними результатами
def get_analytical_probabilities():
    return {
        2: (1 / 36) * 100,
        3: (2 / 36) * 100,
        4: (3 / 36) * 100,
        5: (4 / 36) * 100,
        6: (5 / 36) * 100,
        7: (6 / 36) * 100,
        8: (5 / 36) * 100,
        9: (4 / 36) * 100,
        10: (3 / 36) * 100,
        11: (2 / 36) * 100,
        12: (1 / 36) * 100
    }

# Візуалізація результатів у вигляді таблиці та графіка
def visualize_results(monte_carlo_probs, analytical_probs):
    # Створення DataFrame для візуалізації
    data = {
        "Сума": list(monte_carlo_probs.keys()),
        "Ймовірність Монте-Карло (%)": list(monte_carlo_probs.values()),
        "Аналітична ймовірність (%)": [analytical_probs[sum_] for sum_ in monte_carlo_probs.keys()]
    }
    df = pd.DataFrame(data)

    # Виведення таблиці
    print(df)

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(df["Сума"], df["Ймовірність Монте-Карло (%)"], label="Ймовірність Монте-Карло", marker='o')
    plt.plot(df["Сума"], df["Аналітична ймовірність (%)"], label="Аналітична ймовірність", marker='x')
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність (%)")
    plt.title("Порівняння ймовірностей для суми при киданні двох кубиків")
    plt.legend()
    plt.grid()
    plt.show()

# Основна частина коду
if __name__ == "__main__":
    num_rolls = 100000  # Кількість кидків для симуляції Монте-Карло

    # Симуляція методом Монте-Карло
    monte_carlo_probs = monte_carlo_simulation(num_rolls)

    # Отримання аналітичних результатів
    analytical_probs = get_analytical_probabilities()

    # Візуалізація результатів
    visualize_results(monte_carlo_probs, analytical_probs)
