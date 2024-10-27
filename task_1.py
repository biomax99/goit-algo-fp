# Клас вузла однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Клас для роботи з однозв'язним списком
class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання елемента в початок списку
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Вивід списку
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Функція для реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # зберігаємо посилання на наступний вузол
            current.next = prev       # змінюємо напрямок посилання
            prev = current            # переміщаємо prev на поточний вузол
            current = next_node       # переміщаємо current на наступний вузол
        self.head = prev  # новий початок списку

    # Функція сортування однозв'язного списку
    def sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None  # Початок нового відсортованого списку

        # Проходимо по кожному елементу і вставляємо у відповідне місце у відсортованому списку
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list  # Оновлюємо голову списку на відсортований список

    # Допоміжна функція для вставки у відсортованому порядку
    def sorted_insert(self, sorted_list, new_node):
        if sorted_list is None or new_node.data < sorted_list.data:
            new_node.next = sorted_list
            return new_node
        else:
            current = sorted_list
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_list

    # Функція об'єднання двох відсортованих однозв'язних списків в один відсортований список
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node(0)  # Тимчасовий вузол для початку нового списку
        tail = dummy

        # Проходимо по обох списках і додаємо менший елемент до нового списку
        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Додаємо залишки з одного з двох списків
        tail.next = list1 if list1 else list2

        return dummy.next  # Повертаємо голову об'єднаного списку

# Приклад використання
if __name__ == "__main__":
    # Створення першого списку та додавання елементів
    ll1 = LinkedList()
    ll1.push(10)
    ll1.push(30)
    ll1.push(20)
    ll1.push(40)

    print("Перший початковий список:")
    ll1.print_list()

    # Реверсування першого списку
    ll1.reverse()
    print("Реверсований перший список:")
    ll1.print_list()

    # Сортування першого списку
    ll1.sort()
    print("Відсортований перший список:")
    ll1.print_list()

    # Створення другого списку та додавання елементів
    ll2 = LinkedList()
    ll2.push(15)
    ll2.push(25)
    ll2.push(5)
    ll2.push(35)

    print("Другий початковий список:")
    ll2.print_list()

    # Сортування другого списку
    ll2.sort()
    print("Відсортований другий список:")
    ll2.print_list()

    # Об'єднання двох відсортованих списків
    merged_head = LinkedList.merge_sorted_lists(ll1.head, ll2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head

    print("Об'єднаний відсортований список:")
    merged_list.print_list()
