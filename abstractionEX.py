

#example
# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class car(vehicle):
#     def start(self):
#         print('car starts with key...')
#     def stop(self):
#         print('car is stopped')
# class bike(vehicle):
#     def start(self):
#         print('bike starts with self button...')
# c=car()
# c.start()
# b=bike()
# b.start()

#example-2
# from abc import ABC,abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class UPI(Payment):
#     def pay(self):
#         print('payment is done using upi')
# class creditcard(Payment):
#     def pay(self,amount):
#         self.amount=amount-100
#         print(self.amount,'is paid after offer through credit card')
# class cash(Payment):
#     def pay(self):
#         print('payment is done by cash')
# u=UPI()
# u.pay()
# c=creditcard()
# c.pay(1000)
# cas=cash()
# cas.pay()

#employee
# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calsalary(self):
#         pass
# class Fulltime(Employee):
#     def __init__(self,months,sal):
#         self.total=months*sal
#     def calsalary(self):
#         print('total salary:',self.total)
# class freelancer(Employee):
#     def __init__(self,hours,sal):
#         self.total=hours*sal
#     def calsalary(self):
#         print('total salary:',self.total)
# class parttime(Employee):
#     def __init__(self,module,sal):
#         self.total=module*sal
#     def calsalary(self):
#         print('total salary:',self.total)
        
# full=Fulltime(5,35000)
# full.calsalary()
# free=freelancer(3,5000)
# free.calsalary()
# part=parttime(6,1500)
# part.calsalary()


#task on abstraction
#1.food delivery
# from abc import ABC,abstractmethod
# class fooddelivery(ABC):
#     @abstractmethod
#     def calbill(self):
#         return
# class swiggy(fooddelivery):
#     def __init__(self,price,quantity):
#         self.deliverycharges=40
#         self.total=(price*quantity)+self.deliverycharges
#     def calbill(self):
#         print('total bill by swiggy:',self.total)
# class zomato(fooddelivery):
#     def __init__(self,price,quantity):
#         self.total=price*quantity
#         self.discount=(self.total)*(10/100)
#         self.bill=self.total-self.discount
#     def calbill(self):
#         print('total bill by zomato:',self.bill)
# class Restaurant(fooddelivery):
#     def __init__(self,price,quantity):
#         self.total=price*quantity
#         self.tax=(self.total)*(5/100)
#         self.bill=self.total+self.tax
#     def calbill(self):
#         print('total bill by restaurant:',self.bill)
# s=swiggy(300,2)
# s.calbill()
# z=zomato(600,4)
# z.calbill()
# r=Restaurant(500,3)
# r.calbill()

#2.online booking
from abc import ABC,abstractmethod
class onlinebooking(ABC):
    @abstractmethod
    def calamount(self):
        pass
class trainbooking(onlinebooking):
    def __init__(self,price,noofticekts):
        self.total=price*noofticekts
        self.servicecharge=60
        self.amount=self.total+self.servicecharge
    def calamount(self):
        print('total amount in train:',self.amount)
class flightticket(onlinebooking):
    def __init__(self,price,noofticekts):
        self.total=price*noofticekts
        self.tax=(self.total)*(2/100)
        self.amount=self.total+self.tax
    def calamount(self):
         print('total amount for flight:',self.amount)
class hotelbooking(onlinebooking):
    def __init__(self,price,noofrooms):
        self.total=price*noofrooms
        self.servicecharge=100
        self.discount=(self.total)*(10/100)
        self.amount=(self.total-self.discount)+self.servicecharge
    def calamount(self):
         print('total amount for hotel:',self.amount)
t=trainbooking(300,2)
t.calamount()
f=flightticket(1500,3)
f.calamount()
h=hotelbooking(5000,4)
h.calamount()
    
        



