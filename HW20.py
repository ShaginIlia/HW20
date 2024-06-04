class Car:
    price = '1000000 р.'

    def horse_powers(self):
        return '210 л.с.'


class Nissan(Car):
    price = '800000 р.'

    def horse_powers(self):
        return '145 л.с.'


class Kia(Car):
    price = '500000 р.'

    def horse_powers(self):
        return '110 л.с.'


my_car = Car()
my_nissan = Nissan()
my_kia = Kia()
print(my_kia.horse_powers())
print(my_kia.price)
print(my_nissan.horse_powers())
print(my_nissan.price)
