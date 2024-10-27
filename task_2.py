import matplotlib.pyplot as plt
import numpy as np

# Рекурсивна функція для побудови "дерева Піфагора"
def draw_pythagoras_tree(ax, x, y, angle, length, level):
    if level == 0:
        return

    # Обчислюємо координати нового квадрата
    x0, y0 = x, y
    x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
    x2, y2 = x1 - length * np.sin(angle), y1 + length * np.cos(angle)
    x3, y3 = x0 - length * np.sin(angle), y0 + length * np.cos(angle)

    # Малюємо квадрат
    ax.plot([x0, x1, x2, x3, x0], [y0, y1, y2, y3, y0], color="brown")

    # Нові довжини та кути для лівого і правого квадрата
    new_length = length * np.sqrt(2) / 2
    left_angle = angle + np.pi / 4  # Лівий кут
    right_angle = angle - np.pi / 4  # Правий кут

    # Рекурсивні виклики для лівої та правої гілок
    draw_pythagoras_tree(ax, x2, y2, left_angle, new_length, level - 1)
    draw_pythagoras_tree(ax, x1, y1, right_angle, new_length, level - 1)

# Функція для ініціалізації графіка та побудови дерева з рівнем рекурсії, заданим користувачем
def plot_pythagoras_tree(level):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")
    ax.axis("off")

    # Параметри початкового квадрата
    x, y = 0, 0  # Початкова позиція
    angle = np.pi / 2  # Початковий кут (вертикально вгору)
    length = 1  # Початкова довжина квадрата

    # Побудова дерева з заданим рівнем рекурсії
    draw_pythagoras_tree(ax, x, y, angle, length, level)

    plt.show()

# Введення рівня рекурсії від користувача
if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії для 'дерева Піфагора': "))
        plot_pythagoras_tree(level)
    except ValueError:
        print("Будь ласка, введіть коректне ціле число для рівня рекурсії.")
