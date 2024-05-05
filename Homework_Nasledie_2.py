

class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def horse_powers(self, h_p=1000):
        print("лошединные силы = ", h_p)

class Nissan(Car, Vehicle):
    price = 1050000
    vehicle_type = "Yes"

    def horse_powers(self, h_p=15000):
        print("лошединные силы = ", h_p)

# class Kia(Car):
#     price = 140000
#
#     def horse_powers(self, h_p=14000):
#         print("лошединные силы = ", h_p)
#
# car = Car()
car_nissan = Nissan()
# car_kia = Kia()
# print(car.horse_powers(), "цена = ", car.price)
print(car_nissan.vehicle_type, "цена = ", car_nissan.price)
# print(car_kia.horse_powers(), "цена = ", car_kia.price)

