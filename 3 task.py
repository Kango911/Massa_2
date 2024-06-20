# Определение класса узла списка
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


# Определение класса очереди
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        return " -> ".join(map(str, elements))


# Функция для перемещения элементов из первой очереди во вторую
def move_elements(queue1, queue2):
    while not queue1.is_empty():
        value = queue1.dequeue()
        if value % 2 == 0:
            queue2.enqueue(value)
            break
        else:
            queue2.enqueue(value)


# Создание и заполнение первой очереди (P1 и P2)
queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(3)
queue1.enqueue(5)
queue1.enqueue(2)
queue1.enqueue(7)

# Создание второй очереди (P3 и P4)
queue2 = Queue()
queue2.enqueue(8)
queue2.enqueue(6)
queue2.enqueue(4)

# Вывод начальных адресов первой очереди
if queue1.is_empty():
    print("nil nil")
else:
    print(f"P1 = {queue1.head.value}, P2 = {queue1.tail.value}")

# Вывод начальных адресов второй очереди
if queue2.is_empty():
    print("nil nil")
else:
    print(f"P3 = {queue2.head.value}, P4 = {queue2.tail.value}")

# Перемещение элементов из первой очереди во вторую
move_elements(queue1, queue2)

# Вывод новых адресов первой очереди
if queue1.is_empty():
    print("nil nil")
else:
    print(f"Новые P1 = {queue1.head.value}, P2 = {queue1.tail.value}")

# Вывод новых адресов второй очереди
if queue2.is_empty():
    print("nil nil")
else:
    print(f"Новые P3 = {queue2.head.value}, P4 = {queue2.tail.value}")
