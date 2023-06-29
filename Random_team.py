import random 

class Principals():
    def __init__(self,name,rating,kep):
        self.name = name
        self.rating = int(rating)
        self.kep = kep

class Car():
    def __init__(self,name,rating,kep):
        self.name = name
        self.rating = int(rating)
        self.kep = kep

class Drivers():
    def __init__(self,name,rating,kep):
        self.name = name
        self.rating = int(rating)
        self.kep = kep

principals = []

def beolp():
    f = open("principals.txt","r", encoding="utf-8")

    while True:
        sor = f.readline().strip()
        if not sor:
            break
        else:
            part = sor.split(";")
            obj = Principals(part[0],part[1],part[2])
            principals.append(obj)

cars = []

def beolc():
    f = open("car.txt","r", encoding="utf-8")

    while True:
        sor = f.readline().strip()
        if not sor:
            break
        else:
            part = sor.split(";")
            obj = Car(part[0],part[1],part[2])
            cars.append(obj)

drivers = []

def beold():
    f = open("drivers.txt","r", encoding="utf-8")

    while True:
        sor = f.readline().strip()
        if not sor:
            break
        else:
            part = sor.split(";")
            obj = Drivers(part[0],part[1],part[2])
            drivers.append(obj)

def randomizer():
    principal = random.choice(principals)
    car = random.choice(cars)
    driver1 = random.choice(drivers)
    drivers.remove(driver1)
    driver2 = random.choice(drivers)

    rating = round((principal.rating + car.rating + car.rating + car.rating + driver1.rating + driver2.rating)/6,1)

    if rating<5:
        rate = "terribble team"
    elif 5<rating<8:
        rate = "top of midfield"
    elif 8<rating<10:
        rate = "championship winning team"

    print("Principal:",principal.name,"Car:",car.name,"Drivers:",driver1.name,driver2.name,"Rating:",rating,rate)

    #f = open("f1team.html", "w")
    #a= "<html><head></head><body><img src='kepp'><img src='kepc'><img src='kepd1'><img src='kepd2'></body></html>"
    #b = a.replace("kepp",principal.kep).replace("kepc",car.kep).replace("kepd1",driver1.kep).replace("kepd2",driver2.kep)
    #f.write(b)




def main():
    beolp()
    beolc()
    beold()
    randomizer()

main()
