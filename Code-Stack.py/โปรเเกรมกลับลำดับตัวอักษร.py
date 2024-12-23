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

def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

# ทดสอบการใช้งาน
user_input = input("ป้อนข้อความที่ต้องการกลับลำดับ: ")
print("ผลลัพธ์หลังกลับลำดับ:", reverse_string(user_input))
