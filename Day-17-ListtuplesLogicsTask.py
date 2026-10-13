#1.display pairs in list  whose sum is 5
# mylist=[2,4,0,3,5,6,9,10,28]
# sum=0
# for i in range(0,len(mylist),1):
#     for j in range(0,len(mylist),1):
#         if(mylist[i]+mylist[j]==5):
#             print(f'pairs:{mylist[i]},{mylist[j]}')

#2.Find the  all prime numbers between in a list.
# mylist=[2,3,4,5,9,10,11,17]
# for i in range(0,len(mylist),1):
#     n=mylist[i]
#     count=0
#     for j in range(1,n+1,1):
#         if(n%j==0):
#             count=count+1
#     if(count==2):
#         print(n)

#3.Find the  sum of all prime numbers between in a list.
# mylist=[2,3,4,5,9,10,11,17]
# sum=0
# for i in range(0,len(mylist),1):
#     n=mylist[i]
#     count=0
#     for j in range(1,n+1,1):
#         if(n%j==0):
#             count=count+1
#     if(count==2):
#         sum=sum+n
# print('sum of prime numbers:',sum)

#4.Find the average of all perfect numbers in list.
# mylist=[2,3,4,6,5,9,10,11,17,28,496]
# count=0
# sump=0
# for i in range(0,len(mylist),1):
#     n=mylist[i]
#     sum=0
#     for j in range(1,n,1):
#         if(n%j==0):
#             sum=sum+j
#     if(sum==n):
#         count=count+1
#         sump=sump+n
# avg=sump/count
# print('average of all perfect numbers:',avg)

#5.find Leap Years in a list
# mylist=[2004,2005,2006,2020,2023,2024]
# for i in range(0,len(mylist),1):
#     year=mylist[i]
#     if(year%400==0 or year%100!=0 and year%4==0):
#         print(year)

#6.Find all the palindrom numbers in list
# mylist=[11,1,2,121,100,200,212,300]
# for i in range(0,len(mylist),1):
#     n=mylist[i]
#     temp=n
#     rev=0
#     while(n>0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     if(rev==temp):
#         print(temp)

#7.Print all numbers in list whose digit sum is exactly 10.direct traversal
# mylist=[21,19,10,55,23,28,11,37]
# for n in mylist:
#     temp=n
#     sum=0
#     while(n>0):
#         ld=n%10
#         sum=sum+ld
#         n=n//10
#     if(sum==10):
#        print(temp)

#8.Print all pairs (a, b) in list whose sum is 30. Print each pair only once.
# mylist=[10,20,50,21,7,3,11,23]
# for n in mylist:
#     for x in mylist:
#         if((n+x)==30):
#             print(f'({n},{x})')

#9.Print all numbers in tuple  that have exactly 3 factors.
# mytuple=(2,4,6,7,5,10,9,11)
# for n in mytuple:
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count=count+1
#     if(count==3):
#         print(n)

#10.Print the prime factors of every number in list.
mylist=[21,24,27,33,67,98,20]
for n in mylist:
    for j in range(1,n+1,1):
        count=0
        for i in range(1,j+1,1):
            if(j%i==0):
                count=count+1
        if(n%j==0 and count==2):
            print(f'{n}-->{j}',end=' ')
    print()



