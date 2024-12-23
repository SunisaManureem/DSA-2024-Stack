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


def decimal_to_base(decimal_number, base):
    stack = Stack()
    digits = "0123456789ABCDEF"
    
    while decimal_number > 0:
        stack.push(digits[decimal_number % base])
        decimal_number //= base
    
    converted_number = ""
    while not stack.is_empty():
        converted_number += stack.pop()
    return converted_number


# ทดสอบการใช้งาน
decimal = int(input("ป้อนตัวเลขฐาน 10: "))
print(f"ฐาน 2: {decimal_to_base(decimal, 2)}")
print(f"ฐาน 16: {decimal_to_base(decimal, 16)}")
