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


def check_json(json_string):
    stack = Stack()
    pairs = {']': '[', '}': '{', ')': '('}

    for char in json_string:
        if char in "[{(":
            stack.push(char)
        elif char in "]})":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


# ทดสอบการใช้งาน
json_input = input("ป้อน JSON string: ")
print("JSON ถูกต้อง" if check_json(json_input) else "JSON ไม่ถูกต้อง")
