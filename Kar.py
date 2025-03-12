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
