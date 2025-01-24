######### Farm Management System ##########

class Animal:
    def __init__(self,name,species,energy=120,hunger=50):
        self.name = name
        self.species = species
        self.energy = energy #เริ่มต้น 150/150 ถ้า 20/150 ต้องนอน
        self.hunger = hunger #เริ่มต้น 50/150 ถ้า 120/150 ต้องกิน
 
     
    # ------ ฟังก์ชันการกิน ------ #
    # ความหิวลดลง 20 และ พลังงานเพิ่ม 10  
    def eat(self):
        pass
    
    # ------ ฟังก์ชันการนอน ------ # 
    # ความหิวเพิ่มขึ้น 10 และ พลังงานเพิ่ม 30
    def sleep(self):
        if self.energy < 20:
            self.energy += 30
            self.hunger += 10
            print (f"--------------------\n"
                    f"{self.name} กำลังพักผ่อน\n"
                    f"ค่าพลังงานเพิ่มขึ้น 30\n"
                    f"ค่าความหิวเพิ่มขึ้น 10\n"
                    f"--------------------"
                   )
        else:
            print(f"{self.name} ค่าพลังงานเพียงพอแล้ว!")
            
    
    # ------ ฟังก์ชันการเคลื่อนที่ ------ #
    # ความหิวเพิ่มขึ้น 10 และ พลังงานลดลง 20
    
    def check_status(self):
        status = (
            f"{self.name} เป็น {self.species}\n"
            f"ค่าพลังงาน : {self.energy}\n"
            f"ค่าความหิว : {self.hunger}\n"
        )
        
        if self.energy < 20:
            status += " พลังงานต่ำ ต้องพักผ่อน\n"
        if self.hunger > 120:
            status += " ความหิวสูง ต้องกินข้าวเพิ่ม\n"
        print(status)
        
dog = Animal("แสนดี","หมา")
dog2 = Animal("ปีโป้","หมา",energy=10)
dog2.check_status()
dog2.sleep()
dog2.check_status()
