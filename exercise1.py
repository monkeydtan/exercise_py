# ทวนเรื่อง class def ใหม่

# def greet(name):
#     return f"สวัสดี, {name}"

# print(greet("Tan"))

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.energy = 50
        self.hunger = 30
        
    def bark(self):
        if self.energy >= 10: #ตรวจสอบว่ามีพลังงานพอมั้ย
            self.energy -= 10 # ถ้าพอให้ลบออกไป 10 เมื่อมันเห่า
            print(f"{self.name} เห่า! พลังงานลดลง 10 หน่วย คงเหลือ {self.energy}")
        else:
            print(f"{self.name} พลังงานไม่พอสำหรับเห่า!")
    
    def eat(self):
        if self.hunger >= 30: #ถ้าค่าความหิว = 30 >>> กินแล้วค่าความหิวลดทีละ20
            self.hunger -= 20 
            self.energy += 10
            print(f"{self.name} กินข้าว ค่าความหิวลดลงเหลือ {self.hunger} และ พลังงานเพิ่มขึ้น {self.energy}")
        else:
            print(f"{self.name} หิวเกินไปหรือพลังงานไม่พอที่จะเห่า!")
            
    def play(self):
        if self.energy >= 20:
            self.energy -= 20
            self.hunger += 15
            print(f"{self.name} เล่นกับเจ้าของ ทำให้ พลังงานลดลง 20 หน่วย\n" 
                  f"และค่าความหิวเพิ่มขึ้น 15 หน่วย")
        else:
            print(f"{self.name} มีพลังงานไม่พอที่จะเล่น!")

    # ตรวจสอบสถานะของหมา energy แลำ hunger
    def check_status(self):
        status = (
            f"--------------------------------\n"
            f"{self.name} อายุ {self.age} ปี\n"
            f"ค่าความหิว : {self.hunger} / 100\n"
            f"ค่าพลังงาน : {self.energy} / 100")
        
        if self.energy <= 10:
           status += " พลังงานต่ำ อาจต้องพักผ่อนหรือกินข้าวเพิ่ม\n"
        if self.hunger >= 80:
           status += " ความหิวสูง อาจต้องกินข้าวเพิ่ม\n"
        print(status)
        

dog1 = Dog("คุกกี้",2) # สร้าง object ขึ้นมา หรือก็คือสร้างหมา 1 ตัวขึ้นมา
dog1.bark()  # แสดงผล เห่าครั้งที่ 1
dog1.bark()  # แสดงผล เห่าครั้งที่ 2
dog1.play()
dog1.play()
dog1.check_status()