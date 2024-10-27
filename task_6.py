# Дані про їжу: назва страви, вартість, калорійність
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

# Жадібний алгоритм для вибору страв з максимальним співвідношенням калорій до вартості
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for name, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append(name)
            total_cost += details["cost"]
            total_calories += details["calories"]

    return selected_items, total_calories

# Динамічне програмування для вибору страв з максимальними калоріями при заданому бюджеті
def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(names)

    # Ініціалізація таблиці для динамічного програмування
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(budget + 1):
            if costs[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]

    # Визначення обраних страв
    selected_items = []
    total_calories = dp[n][budget]
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(names[i - 1])
            b -= costs[i - 1]

    selected_items.reverse()  # Зворотний порядок для правильного відображення

    return selected_items, total_calories

# Приклад використання
if __name__ == "__main__":
    budget = 100  # Заданий бюджет

    # Жадібний алгоритм
    greedy_items, greedy_calories = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print("Обрані страви:", greedy_items)
    print("Загальна калорійність:", greedy_calories)

    # Динамічне програмування
    dp_items, dp_calories = dynamic_programming(items, budget)
    print("\nДинамічне програмування:")
    print("Обрані страви:", dp_items)
    print("Загальна калорійність:", dp_calories)
