class Stack:
    def __init__(self):
        self.elements = []
        self.brackets = {')': '(', ']': '[', '}': '{'}

    def is_empty(self):
        """Проверка стека на пустоту. Метод возвращает True или False"""
        return len(self.elements) == 0  # Возвращает True, если количество элементов равно 0

    def push(self, element):
        """добавляет новый элемент на вершину стека. Метод ничего не возвращает;"""
        self.elements.append(element)

    def pop(self):
        """удаляет верхний элемент стека.
        Стек изменяется. Метод возвращает верхний элемент стека;"""
        if not self.is_empty():
            return self.elements.pop()
        else:
            raise IndexError("в стеке нет элементов")

    def peek(self):
        '''возвращает верхний элемент стека, но не удаляет его. Стек не меняется;'''
        if not self.is_empty():
            return self.elements[-1]
        else:
            raise IndexError("в стеке нет элементов")

    def size(self):
        """возвращает количество элементовв стеке."""
        return len(self.elements)

    """задание 2. решите задачу на проверку сбалансированности скобок. 
    Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, 
    и пары скобок правильно вложены друг в друга."""


    def is_balanced(self, expression):
        stack = []  # Стек для хранения открывающих скобок
        for char in expression:
            if char in self.brackets.values():  # Если это открывающая скобка
                stack.append(char)
            elif char in self.brackets.keys():  # Если это закрывающая скобка
                if stack == [] or stack.pop() != self.brackets[char]:
                    return "Несбалансированно"
        return "Сбалансированно" if not stack else "Несбалансированно"

if __name__ == "__main__":
    stack_ = Stack()
    # print(stack.is_empty())
    # stack.push(1)
    # stack.push(2)
    # print(stack.is_empty())
    # print(stack.pop())
    # print(stack.size())
    # user_input = input("Ожидаю на вход строку со скобками: ")
    # result = stack_.is_balanced(user_input)
    # print(result)