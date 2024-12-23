class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def apply_operation(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            raise ValueError("ไม่สามารถหารด้วยศูนย์ได้")
        return a // b


def evaluate_infix(expression):
    values = Stack()
    operators = Stack()

    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue

        if expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            values.push(val)
            i -= 1
        elif expression[i] == '(':
            operators.push(expression[i])
        elif expression[i] == ')':
            while not operators.is_empty() and operators.peek() != '(':
                b = values.pop()
                a = values.pop()
                op = operators.pop()
                values.push(apply_operation(a, b, op))
            operators.pop()  # Remove '('
        else:
            while (not operators.is_empty() and
                   precedence(operators.peek()) >= precedence(expression[i])):
                b = values.pop()
                a = values.pop()
                op = operators.pop()
                values.push(apply_operation(a, b, op))
            operators.push(expression[i])
        i += 1

    while not operators.is_empty():
        b = values.pop()
        a = values.pop()
        op = operators.pop()
        values.push(apply_operation(a, b, op))

    return values.pop()


# ทดสอบการใช้งาน
try:
    infix_expr = input("ป้อน Infix Expression (เช่น '3 + (2 * 4)'): ")
    print("ผลลัพธ์:", evaluate_infix(infix_expr))
except ValueError as e:
    print("ข้อผิดพลาด:", e)
