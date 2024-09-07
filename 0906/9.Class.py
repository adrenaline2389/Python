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
        print(f'{self.brand} {self.model}'.upper())

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

new_car = Car('porsche', '718')
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

# 继承 inheritance
class ElectricCar(Car):
    def __init__(self, brand, model):
        """初始化父类的属性"""
        super().__init__(brand, model)   # 这里不需要"self"，因为super()函数会自动传递实例给类
        self.battery = Battery()   # 这里是给子类属性和方法，同时调用了另一个类
    # 重写父类中的方法：在子类中定义一个与要重写的父类方法同名的方法，python将忽略父类方法，只关注子类的新方法

# 组合：将大型类拆分成多个协同工作的小类，避免混乱
class Battery:
    def __init__(self, battery_size = 30):
        self.battery_size = battery_size

    def battery(self):
        """描述电池容量"""
        print(f'Your car has a {self.battery_size}-kWh battery.')


hot_ride = ElectricCar('xiaomi', 'su7')
hot_ride.attribute()
hot_ride.battery.battery()