class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")


def evaluate_postfix(expression):
    stack = Stack()
    for char in expression.split():
        if char.isdigit():
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a / b)  # แบ่งแบบ float
    return stack.pop()


# ทดสอบการใช้งาน
postfix_expr = input("ป้อน Postfix Expression (เช่น '3 4 + 2 *'): ")
print("ผลลัพธ์:", evaluate_postfix(postfix_expr))
