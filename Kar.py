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

class Cet():
    def __init__(self,name,color):
        self.color = color
        self.name =name

    def meow (self):
     print(f"{self.color}\n"
            f"{self.name}\n")

Cet1=Cet("Roginald","red")
Cet1.meow()
Cet2=Cet( "Migel","braun")
Cet2.meow()

class Car():
    def __init__(self,brand,year):
        self.brand=brand
        self. year=year
    def start (self):
        print (f"{self.brand}\n"
            f"{self.year}\n")

Car1=Car("Rols Rois", "1999")
Car1.start()
Car2=Car("Chkoda", "2024")
Car2.start()

class MEN ():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce (self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")
    def celebrate_birthday (self,old):
        self.age += old
        print(f"{ self.name} отпраздновал день рождения! Теперь ему { self.age} лет.")
MEN1=MEN("Олег",15)
MEN1.introduce()
MEN1.celebrate_birthday(2)

x=20
y="Artem"
t=90
e="Andrei"
if  e == y:
    print("У нас одинаковые имена Andrei")
else:
    print("Приятно познакомится")
if t == x:
    print("А ещё, у нас одинаковый возраст Andrei")
elif t != x:
    print("Приятно познакомится")
if t > x:
    print("Ты старше, чем я")
else:
    print("Ты младше, чем я")
