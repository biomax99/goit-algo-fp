import matplotlib.pyplot as plt
import networkx as nx

# Функція для побудови графічної візуалізації бінарної купи
def visualize_heap(heap):
    # Створюємо граф
    G = nx.DiGraph()

    # Додаємо вузли та ребра
    for i in range(len(heap)):
        G.add_node(i, label=heap[i])  # Додаємо вузол з міткою значення
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(heap):
            G.add_edge(i, left)  # Додаємо лівого дочірнього вузла
        if right < len(heap):
            G.add_edge(i, right)  # Додаємо правого дочірнього вузла

    # Використовуємо spring_layout для розташування вузлів у вигляді дерева
    pos = nx.spring_layout(G, seed=42, k=1.5 / len(G.nodes) ** 0.5)  # Позиціюємо вузли

    # Малюємо граф
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'), node_size=800, node_color="skyblue", font_size=10, font_weight="bold")
    plt.title("Візуалізація бінарної купи")
    plt.show()

# Приклад використання
if __name__ == "__main__":
    # Приклад бінарної купи у вигляді списку (мін-купа)
    heap = [3, 9, 8, 15, 10, 20, 17]

    # Візуалізація бінарної купи
    visualize_heap(heap)
