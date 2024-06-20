# Определение класса узла списка
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None#Kango911


# Определение класса очереди
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # Kango911
    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Kango911
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:#Kango911
            self.tail = None
        return value

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        return " -> ".join(map(str, elements))
#Kango911

# Создание очереди и добавление элементов
queue = Queue()
queue.enqueue("one")
queue.enqueue("two")
queue.enqueue("three")#Kango911
queue.enqueue("four")
queue.enqueue("five")
queue.enqueue("six")
queue.enqueue("seven")

# Вывод содержимого очереди
print("Исходная очередь:")
print(queue)

# Удаление одного элемента из очереди
queue.dequeue()#Kango911

# Добавление новой строки в очередь
queue.enqueue("eight")

# Вывод очереди после изменений
print("\nОчередь после удаления и добавления:")
print(queue)

# Поиск строк, начинающихся с букв "s" или "t"
count_st_start = sum(1 for item in str(queue).split(" -> ") if item.startswith("s") or item.startswith("t"))
print(f"\nКоличество строк, начинающихся с 's' или 't': {count_st_start}")
