# ทวนเรื่อง class def ใหม่

# def greet(name):
#     return f"สวัสดี, {name}"

# print(greet("Tan"))

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def bark(self):
        return f"{self.name} อายุ {self.age} ปี กำลังเห่า!"
       
    
       
dog1 = Dog("คุกกี้",2)

print(dog1.bark()) 