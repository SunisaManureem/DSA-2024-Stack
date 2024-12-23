class Stack:
    def __init__(self):
        """สร้าง Stack เปล่า"""
        self.items = []  # ใช้ list เก็บข้อมูลใน Stack
    
    def is_empty(self):
        """ตรวจสอบว่า Stack ว่างหรือไม่"""
        return len(self.items) == 0
    
    def push(self, item):
        """เพิ่มข้อมูลเข้า Stack"""
        self.items.append(item)
    
    def pop(self):
        """นำข้อมูลออกจาก Stack"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        """ดูข้อมูลที่อยู่บนสุดของ Stack"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def size(self):
        """ดูขนาดของ Stack"""
        return len(self.items)


# เริ่มต้นการทดสอบ
def main():
    stack = Stack()
    
    # 1. ทดสอบการ push ข้อมูล 5 ตัว
    print("1. Push ข้อมูลเข้า Stack:")
    for i in range(1, 6):
        stack.push(i)
        print(f"Push {i}, Stack: {stack.items}")
    
    # 2. แสดงข้อมูลบนสุดโดยใช้ peek
    print("\n2. ข้อมูลบนสุดของ Stack (peek):")
    print(f"Top item: {stack.peek()}")
    
    # 3. ทดสอบ pop ข้อมูลออก 3 ตัว
    print("\n3. Pop ข้อมูลออก 3 ตัว:")
    for _ in range(3):
        popped_item = stack.pop()
        print(f"Pop {popped_item}, Stack: {stack.items}")
    
    # 4. แสดงข้อมูลที่เหลือใน Stack
    print("\n4. ข้อมูลที่เหลือใน Stack:")
    print(stack.items)


if __name__ == "__main__":
    main()
