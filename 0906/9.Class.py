# 第九章 类

# # 创建和使用类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is sitting.')

    def roll_over(self):
        print(f'{self.name} rolled over!')

fido = Dog('Fido', 6)
print(fido.name)
print(fido.age)

fido.sit()
fido.roll_over()

# # 使用类和实例
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.odometer = 0   # 给属性指定默认值

    def attribute(self):
        print(f'{self.brand} {self.model}'.title())

    def read_odometer(self):
        print(f'This car has {self.odometer} miles on it.')

    def update_odometer(self, mileage):
        """
        将里程表读数设定成指定的值
        禁止将读数往回调
        """
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加指定的量"""
        self.odometer += miles

new_car = Car('audi', 'rs7')
new_car.attribute()
new_car.read_odometer()
    # 直接修改属性的值
new_car.odometer = 2389
new_car.read_odometer()
    # 通过方法修改属性的值
new_car.update_odometer(8964)
new_car.read_odometer()
    # 通过方法让属性的值递增
new_car.increment_odometer(1036)
new_car.read_odometer()

