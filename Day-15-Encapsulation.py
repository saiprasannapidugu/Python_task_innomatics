# class Person:
#     def setdata(self):
#         self.__name='prasanna'
#         self.__salary=50000
#     def accessname(self):
#         return self.__name
#     def accesssalary(self):
#         return self.__salary
# p=Person()
# p.setdata()
# print('name:',p.accessname())
# print('salary:',p.accesssalary())

#with constructor
#class is public
# class Person:
#     def __init__(self,name,salary):
#         #data is private to avoid direct access
#         self.__name=name
#         self.__salary=salary
#         #methods are public to establish the communication
#     def getName(self):
#         return self.__name
#     def getSalary(self):
#         return self.__salary
#     def setname(self,Nname):
#         self.__name=Nname
#     def setsalary(self,Nsalary):
#         self.__salary=Nsalary
# p=Person('prasanna',60000)

# print('before updating name:',p.getName())
# print('before updating salary:',p.getSalary())
# p.setname('sai')
# p.setsalary(95000)

# print('after updating name:',p.getName())
# print('after updating salary:',p.getSalary())

#Example-2
# class student:
#     def __init__(self,id,name,course,fees):
#         self.__id=id
#         self.__name=name
#         self.__course=course
#         self.__fees=fees
#     def getid(self):
#         return self.__id
#     def getname(self):
#             return self.__name
#     def getcourse(self):
#             return self.__course
#     def getfee(self):
#             return self.__fees
#     def setid(self,Sid):
#           self.__id=Sid
#     def setname(self,Sname):
#           self.__name=Sname
#     def setcousre(self,Scourse):
#           self.__course=Scourse
#     def setfees(self,Sfee):
#           self.__fees=Sfee
# s=student(101,'kusuma','cse',20000)
# print('Before updation')
# print('ID:',s.getid())
# print('Name:',s.getname())
# print('Course:',s.getcourse())
# print('fees:',s.getfee())

# s.setid(102)
# s.setname('shravya')
# s.setcousre('IT')
# s.setfees(70000)

# print('After updation')
# print('ID:',s.getid())
# print('Name:',s.getname())
# print('Course:',s.getcourse())
# print('fees:',s.getfee())


#example-3

# class Bank:
#     def __init__(self,accNo,blc):
#         self.__accNo=accNo
#         self.__blc=blc
#     def getaccno(self):
#         return self.__accNo
#     def getblc(self):
#         return self.__blc
#     def setaccno(self,accNo):
#         self.__accNo=accNo
#     def deposit(self,depblc):
#         self.__blc=self.__blc+depblc
#     def withdraw(self,with_balc):
#         if(self.__blc>with_balc):
#             self.__blc=self.__blc-with_balc
#             return self.__blc
#         else:
#             return 'insufficent'
        
# b=Bank(1234,20000)
# print('before updation')
# print('account number:',b.getaccno())
# print('account balance',b.getblc())
# b.deposit(5000)
# print('after deposit account balance',b.getblc())
# result=b.withdraw(10000)
# print('after withdraw')
# print('account balance',result)

#three real world examples of encaplsulation-task
#1.Mobile phone
# class Mobile:
#     def __init__(self,phoneNo,balance):
#         self.__phoneNo=phoneNo
#         self.__balance=balance
#     def getphoneno(self):
#         return self.__phoneNo
#     def getbalance(self):
#         return self.__balance
#     def recharge(self,amount):
#         self.__balance=self.__balance+amount
#     def makecall(self,callamount):
#         if(self.__balance>=callamount):
#             self.__balance=self.__balance-callamount
#             print('call successful')
#         else:
#             print('insufficient balance')
# m=Mobile(9876543210,500)
# print('before recharge')
# print('phoneNO:',m.getphoneno())
# print('balance:',m.getbalance())

# m.recharge(700)
# print('after recharge balance:',m.getbalance())

# m.makecall(50)
# print('after making call balance:',m.getbalance())

#2.Employee salary
# class Employee:
#     def __init__(self,employeeid,salary):
#         self.__employeeid=employeeid
#         self.__salary=salary
#     def getemployeeid(self):
#         return self.__employeeid
#     def getsalary(self):
#         return  self.__salary
#     def setsalary(self,salary):
#         self.__salary=salary
#     def bonus(self,amount):
#         if(amount>0):
#             self.__salary=self.__salary+amount
#         else:
#             print('invalid bonus')
#     def deduction(self,damount):
#         if(self.__salary>=damount):
#             self.__salary=self.__salary-damount
#         else:
#             print('deduction cannot exceed salary')
# e=Employee(123,50000)
# print('employee id:',e.getemployeeid())
# print('before bonus salary:',e.getsalary())

# e.setsalary(70000)
# print('updated salary',e.getsalary())

# e.bonus(5000)
# print('after adding bonus:',e.getsalary())

# e.deduction(10000)
# print('after deduction balance:',e.getsalary())

#3.online shopping
class Product:
    def __init__(self,productname,price,quantity):
        self.__productname=productname
        self.__price=price
        self.__quantity=quantity
    def getproductname(self):
        return self.__productname
    def getprice(self):
        return self.__price
    def getquantity(self):
        return self.__quantity
    def setprice(self,price):
        self.__price=price
    def addstock(self,quantity):
        self.__quantity=self.__quantity+quantity
    def purchase(self,quantity):
        if(self.__quantity>=quantity):
            self.__quantity=self.__quantity-quantity
        else:
            print('insufficient stock')
p=Product('shoes',1000,2)
print('product name:',p.getproductname())
print('price before update:',p.getprice())
print('quantity before adding and purchasing:',p.getquantity())

p.setprice(1500)
print('price after update:',p.getprice())

p.addstock(3)
print('quantity after adding :',p.getquantity())

p.purchase(10)
print('quantity adding adding and purchasing:',p.getquantity())



    
