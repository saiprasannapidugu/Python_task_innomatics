# class Parent:
#     def brave(self):
#         print('iam Brave')
#     def talent(self):
#         print('iam talent')
# p=Parent()
# p.land=100
# # p.brave()
# # p.talent()
# # print('the land:',p.land)

# class Child(Parent):  #subclass
#     def artist(self):
#         print('iam a artist')
# c=Child()
# c.artist()
# c.brave()  #superclass -->parentclass
# c.talent()
# print('land of child accessed from parent:',c.land)

#type of inheritance
#1.single inheritance
#animal-->cat
# class Animal:
#     def eat(self):
#         print('Eating...')
#     def sleeps(self):
#         print('sleeping...')
# #single inheritance
# class cat(Animal):
#     def sounds(self):
#         print('meow meow ..')
# c=cat()
# c.eat()    #inherited from animal
# c.sleeps()  #inherites from animal
# c.sounds()   #its own method

#with variable static 

# class Bank:
#     bank_name='sbi'
# class hydbrach(Bank):
#     # def m1(self):
#     #     print('m1 from hyderbadbranch')
#     pass
# print('bank name',Bank.bank_name)
# print('hydrebad branch bank:',hydbrach.bank_name)

# h=hydbrach()
# print('Hyderbad bank name using object reference:',h.bank_name)

#instance varible
# class Product:
#     def diplaypod(self):
#         print('product name:',self.p_name)
#         print('product price:',self.p_price)

# p=Product()
# p.p_name='product'
# p.p_price=15000
# p.diplaypod()

# class Laptop(Product):
#     def printdet(self):
#         print('product name:',self.l_name)
#         print('product price:',self.l_price)


# l=Laptop()
# l.l_name='Laptop'
# l.l_price=95000
# l.printdet()

# # l.diplaypod()  #it will not work

#consrtuctor inheritance
# class Product:
#     def __init__(self,name,price):  
#         self.name=name
#         self.price=price
#     def displayprod(self):
#         print('product name=',self.name)
#         print('product price=',self.price)
# class laptop(Product):
    
#     # def __init__(self,name,price,ram):
#     #     self.name=name
#     #     self.price=price
#     #     self.ram=ram

#     def __init__(self,name,price,ram):
#             super().__init__(name,price)
#             self.ram=ram
#     def displaylaptop(self):
#         # print('product name=',self.name)
#         # print('product price=',self.price)
#         super().displayprod()
#         print('RAM=',self.ram)
# l=laptop('laptop',95000,'12gb')
# l.displaylaptop()


#2.multilevel inheritance
# class A:
#     def m1(self):
#         print('method from A')
# class B(A):
#     def m2(self):
#         print('method from B')
# class C(B):
#     def m3(self):
#         print('method from C')
# c=C()
# c.m1()
# c.m2()
# c.m3()

#Example-2
# class Gradparent:
#     def home(self):
#         print('Grand parent house..')
# class parent(Gradparent):
#     def car(self):
#         print('parents car...')
# class child(parent):
#     def money(self):
#         print('childs money...')

# #grandparent
# g=Gradparent()
# g.home()
# g.car()   #wrong
# g.money()   #wrong

#parent
# p=parent()
# p.home()
# p.car()
# p.money() #wrong

#child        
# c=child()
# c.car()
# c.home()
# c.money()

#task single -4 ,multilevel-4
#without constructor-2 withconstructor-2

#🔹 Single Inheritance
#1.Single Inheritance without constructor
# class Employee:
#     def work(self):
#         print('do some work')
#     def salary(self):
#         print('take some salary')
# class Manger(Employee):
#     def assign(self):
#         print('assign the task')
#     def manages(self):
#         print('manages the work')
# m=Manger()
# m.work()
# m.salary()
# m.assign()
# m.manages()

#2.Single Inheritance with constructor
# class Animal:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#     def displayanimaldet(self):
#         print('animal nam:',self.name)
#         print('animal type:',self.type)
# class cat(Animal):
#     def sound(self):
#         print('sounds:meow meow...')
# c=cat('cat','Carnivora')
# c.displayanimaldet()
# c.sound()

#3.Single Inheritance with constructor + super()
# class Parent:
#     def __init__(self,house,car):
#         self.house=house
#         self.car=car
#     def dispalyparentdet(self):
#         print('Parent house:',self.house)
#         print('parent car:',self.car)
# class child(Parent):
#     def __init__(self,house,car,money,land):
#         super().__init__(house,car)
#         self.money=money
#         self.land=land
#     def displaychilddet(self):
#         super().dispalyparentdet()
#         print('child money:',self.money)
#         print('child land:',self.land)
# c=child('vella','BMW','5cr',100)
# c.displaychilddet()

#4.Single Inheritance with constructor + super()
#  using a different real-world example

# class Bankaccount:
#     bank_name='sbi'
#     def __init__(self,name,acc_no):
#         self.name=name
#         self.acc_no=acc_no
#     def displaybankacc(self):
#         print('bank name:',Bankaccount.bank_name)
#         print('bank holder name:',self.name)
#         print('bank account number:',self.acc_no)
# class savingsacc(Bankaccount):
#     def __init__(self, name, acc_no,interest_rate):
#         super().__init__(name, acc_no)
#         self.interest_rate=interest_rate
#     def displaysavings(self):
#         super().displaybankacc()
#         print('interest rate:',self.interest_rate)
# s=savingsacc('sai',12345,'6.5%')
# s.displaysavings()

#🔹 Multiple Inheritance
#1.Multiple Inheritance without constructor
# class Employee:
#     def work(self):
#         print('do some work')
#     def salary(self):
#         print('take some salary')
# class Manger(Employee):
#     def assign(self):
#         print('assign the work')
#     def manages(self):
#         print('manages the work')
# class testingmanger(Manger):
#     def testtask(self):
#         print('assign the testing task ')
#     def testmanaging(self):
#         print('manages the only testing task')
# t=testingmanger()
# t.work()
# t.salary()
# t.assign()
# t.manages()
# t.testtask()
# t.testmanaging()

#2.Multiple Inheritance with constructor
# class Animal:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#     def displayanima(self):
#         print('Animal name:',self.name)
#         print('Animal type:',self.type)
# class mammal(Animal):
#     def babies(self):
#         print('have babies and take care of them')
# class cat(mammal):
#     def sound(self):
#         print('sounds:meow meow...')
# c=cat('cat','Carnivora')
# c.displayanima()
# c.babies()
# c.sound()


#3.Multiple Inheritance with constructor + super()
# class product:
#     product_platform='amazon'
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def displayprod(self):
#         print('product platform:',product.product_platform)
#         print('product name:',self.name)
#         print('product price:',self.price)
# class electronic(product):
#     def __init__(self,name,price,warranty):
#         super().__init__(name,price)
#         self.warranty=warranty
#     def dipalyelectronic(self):
#         super().displayprod()
#         print('warrantay:',self.warranty)
# class mobile(electronic):
#     def __init__(self,name,price,warranty,ram):
#         super().__init__(name,price,warranty)
#         self.ram=ram
#     def displaymobile(self):
#         super().dipalyelectronic()
#         print('RAM:',self.ram)
# m=mobile('mobile',20000,'2 years','8 GB')
# m.displaymobile()

#4.Multiple Inheritance with constructor + super() 
# using a different real-world example
# class Car:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def displaycar(self):
#         print('car brand:',self.brand)
#         print('car price:',self.price)
# class Electricvehicle(Car):
#     def __init__(self,brand,price,battery):
#         super().__init__(brand,price)
#         self.battery=battery
#     def displayelecvehicle(self):
#         super().displaycar()
#         print('electric battery:',self.battery)
# class electriccar(Electricvehicle):
#     def __init__(self,brand,price,battery,model):
#         super().__init__(brand,price,battery)
#         self.model=model
#     def displayeleccar(self):
#         super().displayelecvehicle()
#         print('car model:',self.model)
# ec=electriccar('Tesla',200000,'75 kwh','model 3')
# ec.displayeleccar()

#multilevel with constructor
# class Bankaccount:
#     bank_name='union'
#     def __init__(self,acc_number,acc_hold_name):
#         self.acc_number=acc_number
#         self.acc_hold_name=acc_hold_name
#     def displaybankacc(self):
#         print('bank name:',Bankaccount.bank_name)
#         print('bank account number:',self.acc_number)
#         print('bank account holder:',self.acc_hold_name)
# class Bankaccountbal(Bankaccount):
#     def __init__(self,acc_number,acc_hold_name,acc_bal):
#         super().__init__(acc_number,acc_hold_name)
#         self.acc_bal=acc_bal
#     def displaybankbal(self):
#         super().displaybankacc()  #to use the method of parent
#         print('bank balance:',self.acc_bal)
# class Bankacctype(Bankaccountbal):
#      def __init__(self,acc_number,acc_hold_name,acc_bal,acc_type):
#          super().__init__(acc_number,acc_hold_name,acc_bal)
#          self.acc_type=acc_type
#      def displaybanktype(self):
#          super().displaybankbal()
#          print('bank type:', self.acc_type)
# bt=Bankacctype(1234,'hero1',12000,'savings')
# bt.displaybanktype()

#3.hierarchical inheritance
# class Parent:
#     def m1(self):
#         print('m1 from parent')
# class Child1:
#     def m2(self):
#         print('m2 from child1')
# class Child2:
#     def m3(self):
#         print('m3 from child2')

# c2=Child2()
# c2.m3()  #its own -->right
# c2.m1()  #parent -->right
# c2.m2()   #sibling -->wrong

# c1=Child1()
# c1.m3()  #sibling -->wrong
# c1.m1()  #parent -->right
# c1.m2()  #its own -->right

# p=Parent()
# p.m1()  #its own-->right
# p.m2()  #child-->wrong
# p.m3()   #child-->wrong

#exmaple

# class Employee:
#     def det(self):
#         print('iam a employee')
# class Manger(Employee):
#     def mywork(self):
#         print('iam a manger')
# class developer(Employee):
#     def myDesig(self):
#         print('iam a developer')
# d=developer()
# d.det()
# d.myDesig()

# m=Manger()
# m.det()
# m.mywork()

# e=Employee()
# e.det()

#4.multiple inheritance
# class Father:
#     def brave(self):
#         print('iam brave')
# class Mother:
#     def beautiful(self):
#         print('i am beautiful')
# class Child(Father,Mother):
#     def intelligent(self):
#         print('i am intelligent')
# c=Child()
# c.intelligent()
# c.brave()
# c.beautiful()

#smart phone

# class Camera:
#     def pic(self):
#         print('take the pictures')
# class Musicplayer:
#     def player(self):
#         print('plays the music ')
# class smartphone(Camera,Musicplayer):
#     def call(self):
#         print('make the calls')
# s=smartphone()
# s.call()
# s.player()
# s.pic()

#5.Hybrid inheritance
#combinatin of mutiple and multi-level
# class A:
#     def m1(self):
#         print("m1 from A")
# class B:
#     def m2(self):
#         print("m2 from B")
# class C(A,B):
#     def m3(self):
#         print("m3 from C")
# class D(C):
#     def m4(self):
#         print("m4 from D")
# d=D()
# d.m4()
# d.m3()
# d.m2()
# d.m1()


#combination heirarchical and mutltilevel

# class A:
#     def m1(self):
#         print("m1 from A")
# class B(A):
#     def m2(self):
#         print("m2 from B")
# class C(A):
#     def m3(self):
#         print("m3 from C")
# class D(C):
#     def m4(self):
#         print("m4 from D")
# d=D()
# d.m4()
# d.m3()
# d.m2()
# d.m1()

#.hierarchical inheritance with constructor
# class Employee:
#     def __init__(self,employee_id,employee_name,salary):
#         self.employee_id=employee_id
#         self.employee_name=employee_name
#         self.salary=salary
#     def displayemployee(self):
#         print('employee id:',self.employee_id)
#         print('employee name:',self.employee_name)
#         print('employee salary:',self.salary)
# class Manger(Employee):
#     def __init__(self,employee_id,employee_name,salary,team_size):
#         super().__init__(employee_id,employee_name,salary)
#         self.team_size=team_size
#     def dispalymanger(self):
#         print('----Manger----')
#         super().displayemployee()
#         print('team size:',self.team_size)
# class Developer(Employee):
#     def __init__(self,employee_id,employee_name,salary,prgram_lang):
#         super().__init__(employee_id,employee_name,salary)
#         self.prgram_lang=prgram_lang
#     def displaydeveloper(self):
#         print('-----developer----')
#         super().displayemployee()
#         print('Programming language:', self.prgram_lang)
# m=Manger(100,'sai',12000,10)
# m.dispalymanger()
# d=Developer(101,'prasanna',15000,'python')
# d.displaydeveloper()

#multiple inheritance with constructor without super
# class Student:
#     def __init__(self,student_name,roll_number):
#         self.student_name=student_name
#         self.roll_number=roll_number
#     def displaystudent(self):
#         print('student name:',self.student_name)
#         print('student roll number:',self.roll_number)
# class Address:
#     def __init__(self,city,pincode):
#         self.city=city
#         self.pincode=pincode
#     def displayaddress(self):
#         print('student city:',self.city)
#         print('student pincode:',self.pincode)
# class Collegestudent(Student,Address):
#     def __init__(self,student_name,roll_number,city,pincode,branch):
#         Student.__init__(self,student_name,roll_number)
#         Address.__init__(self,city,pincode)
#         self.branch=branch
#     def displaycollegestudent(self):
#         Student.displaystudent(self)
#         Address.displayaddress(self)
#         print('branch:',self.branch)
# c=Collegestudent('sai',121,'hyderbad',500085,'CSE')
# c.displaycollegestudent()



#multiple inheritance with constructor with super()
# class Student:
#     def __init__(self,student_name,roll_number,city,pincode):
#         self.student_name=student_name
#         self.roll_number=roll_number
#         super().__init__(city,pincode)
#     def displaystudent(self):
#         print('student name:',self.student_name)
#         print('student roll number:',self.roll_number)
#         super().displayaddress()
# class Address:
#     def __init__(self,city,pincode):
#         self.city=city
#         self.pincode=pincode
#     def displayaddress(self):
#         print('student city:',self.city)
#         print('student pincode:',self.pincode)
# class Collegestudent(Student,Address):
#     def __init__(self,student_name,roll_number,city,pincode,branch):
#         super().__init__(student_name,roll_number,city,pincode)
#         self.branch=branch
#     def displaycollegestudent(self):
#         super().displaystudent()
#         print('branch:',self.branch)
# c=Collegestudent('sai',121,'hyderbad',500085,'CSE')
# c.displaycollegestudent()

# Hybrid inheritance with constructor
#multiple and multilevel
# class person:
#     def __init__(self,name,age,employee_id,salary):
#         self.name=name
#         self.age=age
#         super().__init__(employee_id,salary)
#     def displayperson(self):
#         print('name of perosn:',self.name)
#         print('age of person:',self.age)
#         super().displayemployee()
# class Employee:
#     def __init__(self,employee_id,salary):
#         self.employee_id=employee_id
#         self.salary=salary
#     def displayemployee(self):
#         print('employee id:',self.employee_id)
#         print('employee salary:',self.salary)
# class Developer(person,Employee):
#     def __init__(self,name,age,employee_id,salary,prog_lan):
#         self.prog_lan=prog_lan
#         super().__init__(name,age,employee_id,salary)
#     def displaydeveloper(self):
        
#         super().displayperson()
#         print('programming language:',self.prog_lan)
# class Manager(Developer):
#     def __init__(self,name,age,employee_id,salary,prog_lan,team_size):
#         self.team_size=team_size
#         super().__init__(name,age,employee_id,salary,prog_lan)
#     def displaymanger(self):
#         super().displaydeveloper()
#         print('team size:',self.team_size)
# m=Manager('sai',24,121,30000,'java',12)
# m.displaymanger()

#MRO-method resulution order
# class A:
#     def m1(self):
#         print('iam m1 from A')
# class B(A):
#     def m2(self):
#         print('Iam m2 from B')
# b=B()
# #b.m2()
# b.m1()

# class A:
#     def m1(self):
#         print('iam m1 from A')
# class B(A):
#     def m2(self):
#         print('Iam m2 from B')
# class C(B):
#     def m3(self):
#             print('Iam m3 from C')
# c=C()
# c.m1()
# print(C.mro())

#mutilple inheritance
# class A:
#     def m1(self):
#         print('m1 from A')
# class B:
#     def m1(self):
#         print('m1 from B')
# class C(A,B):
#     pass
# c=C()
# c.m1()
# print(C.mro())  #C-->A-->B-->object

#diamond problem
# class X:
#     def m0(self):
#         print('m0 from X')
# class A(X):
#     def m1(self):
#         print('m1 from A')
# class B(X):
#     def m1(self):
#         print('m1 from B')
# class C(A,B):
#     pass
# c=C()
# c.m1()
# print(C.mro())




    





    

    





