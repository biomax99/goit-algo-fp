import heapq

# Клас для графа з методом додавання ребер
class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        # Додаємо ребро у вигляді словника
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []

        # Додаємо напрямок з from_node до to_node з певною вагою
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))  # Якщо граф неорієнтований

# Функція для знаходження найкоротшого шляху за алгоритмом Дейкстри
def dijkstra(graph, start):
    # Ініціалізація мінімальної купи та початкових відстаней
    min_heap = [(0, start)]  # (вага, вузол)
    distances = {node: float('inf') for node in graph.edges}  # Початкові відстані
    distances[start] = 0
    visited = set()

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        # Пропускаємо вузли, які вже були оброблені
        if current_node in visited:
            continue

        visited.add(current_node)

        # Оновлюємо відстані для сусідів
        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            # Якщо знаходимо коротший шлях, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# Приклад використання
if __name__ == "__main__":
    # Створення графа
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)
    graph.add_edge('C', 'E', 3)
    graph.add_edge('D', 'E', 2)

    # Запуск алгоритму Дейкстри від початкової вершини 'A'
    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)

    # Вивід найкоротших шляхів від 'A' до всіх інших вершин
    print(f"Найкоротші шляхи від вершини '{start_node}':")
    for node, distance in shortest_paths.items():
        print(f"Відстань до {node}: {distance}")
