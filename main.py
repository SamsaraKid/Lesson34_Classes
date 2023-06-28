class Cat:
    city = 'Moscow'
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def sleep(self):
        print(self.name, 'спит')
    def walk(self):
        print(self.name, 'гуляет')


cat1 = Cat('vasia', 'black')

print(cat1.name, cat1.color)
cat1.walk()
cat1.sleep()

cat2 = Cat('petya', 'ginger')

print(cat2.name, cat2.color)
cat2.walk()
cat2.sleep()


class Lisiy(Cat):
    def cold(self):
        print(self.name, 'мёрзнет')


class Auto:
    city = 'moscow'
    def __init__(self, mark='q', year=1111, color='w'):
        self.mark = mark
        self.year = year
        self.color = color
    def run(self, where='домой'):
        print(self.color, self.mark, 'едет', where)
    def brek(self):
        print(self.color, self.mark, 'тормозит')
    def accel(self, speed=100):
        print(self.color, self.mark, 'ускоряется', 'до', speed, 'км/ч')


audi = Auto('audi', 1996, 'red')
bmw = Auto('bmw', 2000, 'black')
tesla = Auto('tesla', 2020, 'silver')
audi.run('в москву')
bmw.brek()
tesla.accel(100500)

class TruckCar(Auto):
    kuda = ['omsk', 'ufa']
    def where(self, city):
        print(self.color, self.mark, 'везёт груз в', self.kuda[city])

class SportCar(Auto):
    def krug(self, circle):
        print(self.color, self.mark, 'заходит на', circle, 'круг')

t = TruckCar('audi', 1996, 'black')
s = SportCar('audi', 1996, 'black')

t.where(1)
s.krug(3)
