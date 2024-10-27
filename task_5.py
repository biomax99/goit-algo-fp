import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import numpy as np

# Функція для побудови дерева та візуалізації обходу за допомогою DFS
def visualize_dfs_tree(tree, start_node):
    G = nx.Graph(tree)
    pos = nx.spring_layout(G, seed=42)
    visited = set()
    stack = [start_node]
    order = []

    # DFS обхід з використанням стеку
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Додаємо дочірні вузли до стеку в зворотному порядку, щоб обхід йшов у правильному напрямку
            stack.extend(reversed(tree[node]))

    # Відображення графа з використанням порядку для кольорової карти
    color_map = np.linspace(0, 1, len(order))
    node_colors = {node: color_map[i] for i, node in enumerate(order)}
    node_color_values = [node_colors[node] for node in G.nodes]

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color=node_color_values, cmap="Blues", node_size=800, font_weight="bold")
    plt.title("DFS обхід дерева")
    plt.show()

# Функція для побудови дерева та візуалізації обходу за допомогою BFS
def visualize_bfs_tree(tree, start_node):
    G = nx.Graph(tree)
    pos = nx.spring_layout(G, seed=42)
    visited = set()
    queue = deque([start_node])
    order = []

    # BFS обхід з використанням черги
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Додаємо дочірні вузли до черги
            queue.extend(tree[node])

    # Відображення графа з використанням порядку для кольорової карти
    color_map = np.linspace(0, 1, len(order))
    node_colors = {node: color_map[i] for i, node in enumerate(order)}
    node_color_values = [node_colors[node] for node in G.nodes]

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color=node_color_values, cmap="Oranges", node_size=800, font_weight="bold")
    plt.title("BFS обхід дерева")
    plt.show()

# Приклад використання
if __name__ == "__main__":
    # Структура дерева у вигляді списку суміжностей
    tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }

    # Візуалізація обходу DFS
    visualize_dfs_tree(tree, 'A')

    # Візуалізація обходу BFS
    visualize_bfs_tree(tree, 'A')
