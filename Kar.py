class Car:
    def __init__(self,brend,model,year,melenger):
        self.brend=brend
        self.model=model
        self.year=year
        self.melenger=melenger

    def get_info(self):
         print(f"{self.brend}\n"
          f"{self.model}\n"
         f"{self.year}\n"
        f"{self.melenger}\n")

    def drive(self, km):
        self.melenger += km

car = Car("киа","спортейдж","20",500)
car.get_info()
car.drive(200)
car.get_info()

class Laptop:
    def __init__(self,brand,ram,battery):
        self.brand=brand
        self.ram=ram
        self.battery=battery
    def upgrade_ram (self,GB):
        self.ram += GB

    def se_batteryu (self,Proc):
        self.battery -=Proc
    def get_info(self):
        print(f"{self.brand}\n"
              f"{self.ram}\n"
              f"{self.battery}\n")
l1 = Laptop ("Lenovo", 300, 15)
l1.get_info()
l1.upgrade_ram(80)
l1.se_batteryu(9)
l1.get_info()

l2 = Laptop("Apple",500,50)
l2.get_info()
l2.upgrade_ram(990)
l2.se_batteryu(16)
l2.get_info()

l3 = Laptop("ASUS",560,70)
l3.get_info()
l3.upgrade_ram(33)
l3.se_batteryu(20)
l3.get_info()
