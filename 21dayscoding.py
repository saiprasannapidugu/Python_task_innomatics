#============Day 1==========
#1.prime number
# n=int(input('Enter value of n:'))
# count=0
# for i in range(1,n+1,1):
#     if(n%i==0):
#         count=count+1
# if(count==2):
#     print('prime number')
# else:
#     print('not prime number')

#2.armstrong number
# n=int(input('enter value of n:'))
# new=n
# sum=0
# l=len(str(n))
# while(n>0):
#     ld=n%10
#     sum=sum+ld**l
#     n=n//10
# if(sum==new):
#     print("Armstrong number")
# else:
#     print('not a armstrong number')

#3.Reverse a number
# n=int(input('enter a number:'))
# rev=0
# while(n>0):
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# print('reverse of a number:',rev)

#4.Sum of digits
# n=int(input('enter a number:'))
# sum=0
# while(n>0):
#     ld=n%10
#     sum=sum+ld
#     n=n//10
# print("sum of digits=",sum)

#5.Find the First Even Digit from left
# n=int(input('enter a number:'))
# div=10**(len(str(n))-1)
# while(n>0):
#     ld=n//div
#     if(ld%2==0):
#         print(ld)
#         break
#     n=n%div
#     div=div//10

#6.Count Frequency of a Particular Digit
# n=int(input('enter a number:'))
# target=int(input('enter the target number:'))
# count=0
# while(n>0):
#     ld=n%10
#     if(ld==target):
#         count=count+1
#     n=n//10
# print("frequency of digit is:",count)


#2nd day
#1.Find the First Odd Digit
# n=int(input('enter a number:'))
# div=10**(len(str(n))-1)
# while(n>0):
#     ld=n//div
#     if(ld%2!=0):
#         print(ld)
#         break
#     n=n%div
#     div=div//10

# 2.Find the Last Even Digit
# n=int(input('enter a number:'))
# while(n>0):
#     ld=n%10
#     if(ld%2==0):
#         print(ld)
#         break
#     n=n//10

#3.Count Odd and Even Digits
# n=int(input('enter a number:'))
# counte=0
# counto=0
# while(n>0):
#     ld=n%10
#     if(ld%2==0):
#         counte=counte+1
#     if(ld%2!=0):
#         counto=counto+1
#     n=n//10
# print("count of even digits=",counte)
# print("count of odd digits=",counto)

#4.Find the Difference Between Sum of Odd and Even Digits
# n=int(input('enter a number:'))
# sume=0
# sumO=0
# while(n>0):
#     ld=n%10
#     if(ld%2==0):
#         sume=sume+ld
#     if(ld%2!=0):
#         sumO=sumO+ld
#     n=n//10
# diff=sumO-sume
# print("difference=",diff)

#5.Second Largest Distinct Digit
# n=int(input('enter a number:'))
# lar=-1
# second=-1
# while(n>0):
#     ld=n%10
#     if(ld>lar):
#         second=lar
#         lar=ld
#     elif ld>second and ld!=lar:
#         second=ld
#     n=n//10
# print("second largest=",second)

#6️.Strong Number
# n=int(input('enter a number:')) 
# new=n
# sum=0
# while(n>0):
#     ld=n%10
#     fact=1
#     for i in range(1,ld+1,1):
#         fact=fact*i
#     sum=sum+fact
#     n=n//10
# if(sum==new):
#     print("Strong number")
# else:
#     print('not a strong number')


#rearrange its digits to form the largest possible number.
# n=int(input('enter a number:')) 
# new=n
# lar=0
# ans=0
# while(n>0):
#     ld=n%10
#     if ld>lar:
#         lar=ld
#     ans=ans*10+lar
#     n=n//10
# print(ans)

#day3
#1.Print a Number Pattern
# 1
# 12
# 123
# 1234
# 12345

# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print(i,end='')
#     print()

#2.Frequency of Every Digit
# n = input("Enter a number: ")

# for i in range(0,10,1):
#     count=0
#     for digit in n:
#         if int(digit)==i:
#             count=count+1
#     print(i,'->',count)

#2.Frequency of Every Digit
# n = input("Enter a number: ")
# for i in range(0,10,1):
#     count=0
#     for digit in n:
#         if int(digit)==i:
#             count=count+1
#     if(count>0):
#         print(i,'->',count)

#3.Remove Duplicate Digits
# n = input("Enter a number: ")
# new=''
# for digit in n:
#     if digit not in new:
#         new=new+digit
# print(new)

#4.Find the First Non-Repeating Character
# ch=input("enter your input:")
# for charcter in ch:
#     count=0
#     for x in ch:
#         if charcter==x:
#             count+=1
#     if count==1:
#         print(charcter)
#         break

#5.Calculate Power Without **
# base=int(input('Enter the base:'))
# exponent=int(input('enter the exponent:'))
# res=1
# for i in range(exponent):
#     res=res*base
# print(res)

#6.Find GCD of Two Numbers
# a=int(input("enter first number:"))
# b=int(input('enter second number:'))
# while b!=0:
#     remi=a%b
#     a=b
#     b=remi
# print(a)

#day 4
#1. Decimal to Binary
# n=int(input('enter the value of n:'))
# binary=0
# place=1
# while(n>0):
#     res=n%2
#     binary=binary+res*place
#     place=place*10
#     n=n//2
# print(binary)

#2.Perfect Square
# n=int(input('enter the number:'))
# flag=0
# for i in range(1,n,1):
#     if(i*i==n):
#         flag=1
# if(flag==1):
#     print('perfect square')
# else:
#     print("not a perfect square")

#3.Decimal to Octal
# n=int(input('enter the number:'))
# rem=0
# octal=0
# place=1
# while(n>0):
#     rem=n%8
#     octal=octal+rem*place
#     place=place*10
#     n=n//8
# print(octal)

#4.Lcm of numbers
# a=int(input('enter first number:'))
# b=int(input('enter second number:'))
# if(a>b):
#     greater=a
# else:
#     greater=b
# while True:
#     if(greater%a==0 and greater%b==0):
#         print('lcm=',greater)
#         break
#     greater+=1

#5.Number Spiral-like Pattern
#1 2 3 4 5
#2 3 4 5 6
#3 4 5 6 7
#4 5 6 7 8
#5 6 7 8 9
# for j in range(1,6,1):
#     for i in range(1,6,1):
#         print(i+j-1,end='')
#     print()

#6.

# *****
# ** **
# * * *
# ** **
# *****

# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if(j==1 or j==5 or i==1 or i==5 or j==2 and i!=3 or j==3 and i%2!=0 or j==4 and i!=3):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

#day 5
#1.Fibonacci Series
# n=int(input('enter the input:'))
# a=0
# b=1
# for i in range(1,n+1,1):
#     print(a,end=' ')
#     c=a+b
#     a=b
#     b=c

#2.Count the number of prime digits
# n=int(input('enter the number:'))
# while(n>0):
#     ld=n%10
#     count=0
#     for i in range(1,ld+1,1):
#         if(ld%i==0):
#             count=count+1
#     if(count==2):
#         print(ld)
#     n=n//10

#3.Reverse a string using a while loop
# s=input('enter a string:')
# i=len(s)-1
# rev=''
# while i>=0:
#     rev=rev+s[i] 
#     i=i-1
# print(rev)   

#4.X Pattern
# n=int(input('enter the value of n:'))
# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if(i==j or i+j==6):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#5.check anagram
# s1=input('enter first string:')
# s2=input('enter second string:')
# if(len(s1)!=len(s2)):
#     print("not anagram")
# else:
#     flag=1
#     for ch in s1:
#         if s1.count(ch)!=s2.count(ch):
#             flag=0
#             break
#     if flag==1:
#         print("anagram")
#     else:
#         print('not anargram')

#6.Count Prime Numbers Between Two Numbers
# s=int(input('enter start value:'))
# e=int(input('enter end value:'))
# countp=0
# for i in range(s,e+1,1):
#     count=0
#     for j in range(1,i+1,1):
#         if(i%j==0):
#             count=count+1
#     if(count==2):
#         countp=countp+1
# print('number of prime numbers:',countp)

#day 6
#1.Perfect Number in a Range
# for j in range(1,101,1):
#     n=j
#     sum=0
#     new=n
#     for i in range(1,n,1):
#         if(n%i==0):
#             sum=sum+i
#     if(sum==new):
#         print(sum)


#2.Find the Difference Between Maximum and Minimum Digit
# n=int(input('enter the number:'))
# lar=0
# small=9
# while(n>0):
#     ld=n%10
#     if(ld>lar):
#         lar=ld
#     if(ld<small):
#         small=ld
#     n=n//10
# diff=lar-small
# print('difference between max and min:',diff)

#3.Count Numbers Having Exactly 3 Factors
# for j in range(1,31,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count=count+1
#     if(count==3):
#         print(n)

#4. Pascal's Triangle Pattern
    #     1
    #    1 1
    #   1 2 1
    #  1 3 3 1
    # 1 4 6 4 1
# for j in range(1,6,1):
#     for s in range(1,6-j,1):
#         print(" ",end='')
#     value=1
#     for i in range(1,j+1,1):
#         print(value,end=' ')
#         value=value*(j-i)//i
#     print()

#5.Find the Missing Digit from 0–9

# n=input('enter digits:')
# for i in range(10):
#     if str(i) not in n:
#         print("missing digit:",i)    

#6.find the missing digit in number
# n=int(input('enter a number'))
# for i in range(10):
#     new=n
#     flag=0
#     while new>0:
#         ld=new%10
#         if ld==i:
#             flag=1
#             break
#         new=new//10
#     if flag==0:
#         print(i,end='')


#day 7
#1.First Repeated Digit
# n=input("enter the number:")
# for j in range(0,len(n)+1,1):
#     for i in range(j+1,len(n)):
#         if n[j]==n[i]:
#             print(n[j])
#             break
#     else:
#         continue
#     break
        
#2.Spy Number
# n=int(input('enter the number:'))
# sum=0
# prod=1
# while(n>0):
#     ld=n%10
#     sum=sum+ld
#     prod=prod*ld
#     n=n//10
# if(sum==prod):
#     print("it is a spy number")
# else:
#     print("it is not a spy number")

#3.Neon Number
# n=int(input('enter the number:'))
# new=n*n
# sum=0
# while new>0:
#     ld=new%10
#     sum=sum+ld
#     new=new//10
# if(sum==n):
#     print('neon number')
# else:
#     print("not a neon number")

#4.
# 1
# 22
# 333
# 4444
# 55555
# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print(j,end='')
#     print()

#5.
# A
# AB
# ABC
# ABCD
# ABCDE
# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print(chr(64+i),end='')
#     print()

#6.Check if a Number is a Happy Number
#input:19
# 1² + 9² = 82
# 8² + 2² = 68
# 6² + 8² = 100
# 1² + 0² + 0² = 1
# n=int(input('enter the number:'))
# while n!=1:
#     sum=0
#     while n>0:
#         ld=n%10
#         sum=sum+ld**2
#         n=n//10
#     n=sum
# if n==1:
#     print('happy number')

#day 8
#1. Collatz Sequence

# Given a positive integer:
# If n is even → n = n // 2
# If n is odd → n = 3*n + 1
# Continue until n becomes 1.

# n=int(input('enter the number:'))
# while(n!=1):
#     if(n%2==0):
#         n=n//2
#     else:
#         n=3*n+1
#     print(n,end=' ')

#2.Decimal Number to Roman Numerals
# n=int(input('Enter a number:'))
# roman=''
# while n>0:
#     if n>1000:
#         roman=roman+'M'
#         n=n-1000
#     elif n>900:
#         roman=roman+'CM'
#         n=n-900
#     elif n>500:
#         roman=roman+'D'
#         n=n-500
#     elif n>400:
#         roman=roman+'CD'
#         n=n-400
#     elif n>100:
#         roman=roman+'C'
#         n=n-100
#     elif n>90:
#         roman=roman+'XC'
#         n=n-90
#     elif n>50:
#         roman=roman+'L'
#         n=n-50
#     elif n>40:
#         roman=roman+'XL'
#         n=n-40
#     elif n>10:
#         roman=roman+'X'
#         n=n-10
#     elif n>9:
#         roman=roman+'IX'
#         n=n-9
#     elif n>5:
#         roman=roman+'V'
#         n=n-5
#     elif n>4:
#         roman=roman+'IV'
#         n=n-4
#     else:
#         roman=roman+'I'
#         n=n-1
# print(roman)

#3.Remove Spaces Without replace()
# Input: "hello world python"
#Output: "helloworldpython"
# s=input('enter the input:')
# new=''
# for ch in s:
#     if ch!=' ':
#         new=new+ch
# print(new)

#4.Check whether the given number is harshad number or not

# n=int(input('enter the input:'))
# sum=0
# new=n
# while(n>0):
#     ld=n%10
#     sum=sum+ld
#     n=n//10
# if(new%sum==0):
#     print('harshad number')
# else:
#     print('not a harshad number')

#5.Reverse Words in a Sentence
# s=input('enter the input')
# words=s.split()
# for i in range(len(words)-1,-1,-1):
#     print(words[i],end=' ')


#6.finding first repeated digit
# n=input('enter the number:')
# new=''
# for i in n:
#     if i in new:
#         print('first repeated digited:',i)
#         break
#     new=new+i
# else:
#     print('no repeated digits')

#day 9
#1. Automorphic Number
# n=int(input('enter the number:'))
# new=n
# sqr=n*n
# count=0
# while(new>0):
#     count=count+1
#     new=new//10
# l_d=sqr%(10**count)
# if(l_d==n):
#     print('automorphic number')
# else:
#     print('not a automorphic number')

#2. Neon Number
# n=int(input('enter the number:'))
# sum=0
# sqr=n*n
# while(sqr>0):
#     ld=sqr%10
#     sum=sum+ld
#     sqr=sqr//10
# if(sum==n):
#     print('Neon Number')
# else:
#     print('Not a Neon number')

#3. Spy Number
# n=int(input('enter the number:'))
# sum=0
# prod=1
# while(n>0):
#     ld=n%10
#     sum=sum+ld
#     prod=prod*ld
#     n=n//10
# if(sum==prod):
#     print('it is a spy number')
# else:
#     print('It is not a spy number')

#4.Perfect Number
# n=int(input('Enter the number:'))
# sum=0
# for i in range(1,n,1):
#     if(n%i==0):
#         sum=sum+i
# if(sum==n):
#     print('perfect number')
# else:
#     print('not a perfect number')

#5.Reverse Words in a Sentence
# s=input('enter the input:')
# words=s.split()
# for i in range(len(words)-1,-1,-1):
#     print(words[i],end=' ')

#6.Count Words Without split()
# s=input('enter the input:')
# prev=''
# count=1
# for ch in s:
#     if ch!='' and prev==' ':
#         count=count+1
#     prev=ch
# print(count)

#day 10
#1.Anagram Check
# s1=input('enter the s1:')
# s2=input('enter the s2:')
# flag=1
# if(len(s1)!=len(s2)):
#     flag=0
# else:
#     for ch in s1:
#         if(s1.count(ch)!=s2.count(ch)):
#             flag=0
#             break
# if flag==1:
#     print('anagram')
# else:
#     print('not a anagram')

#2.First Non-Repeating Character
# s=input('enter the input: ')
# new=''
# for ch in s:
#     if s.count(ch)==1:
#         print('non repeated character:',ch)
#         break
#     new=new+ch
# else:
#     print('there is no repeated charcater')

#2.First Non-Repeating Character
# s=input('enter the input:')
# for i in s:
#     count=0
#     for j in s:
#         if(i==j):
#             count=count+1
#     if(count==1):
#         print('non repeated digit:',i)
#         break
# else:
#     print('there is no non repeated digit')

#3.Remove Duplicate Characters
# s=input('enter the input:')
# new=''
# for ch in s:
#     if ch not in new:
#         new=new+ch
# print(new)

#4.Find the Longest Word
# s=input("enter the input:")
# words=s.split()
# long=0
# log_word=''
# for i in words:
#     l=len(i)
#     if(l>long):
#         long=l
#         log_word=i
# print(log_word)

#5.Count Vowels in Each Word
# s=input("enter the input:")
# words=s.split()
# for i in words:
#     countv=0
#     for ch in i:
#         if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
#             countv=countv+1
#     print(i,'-->',countv)
        
#6.Character With Maximum Frequency
# s=input("enter the input:")
# lar=0
# lar_c=''
# for ch in s:
#     count=0
#     for j in s:
#         if ch==j:
#             count=count+1
#     if count>lar:
#         lar=count
#         lar_c=ch
# print(lar_c,'-->',lar)

#day 11
#1. Armstrong Number
# def armstrong(n):
#     l=len(str(n))
#     sum=0
#     new=n
#     while(n>0):
#         ld=n%10
#         sum=sum+ld**l
#         n=n//10
#     if(sum==new):
#         return 'armstrong'
#     else:
#         return 'not a armstrong'
# print(armstrong(int(input('enter the input:'))))

#2.palindrom
# def palindrom(n):
#     rev=0
#     new=n
#     while(n>0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     if(rev==new):
#         return 'palindrom number'
#     else:
#         return 'not a palindrom'
# print(palindrom(int(input('enter the input:'))))

#3.Second Smallest digit in a number
# n=int(input('enter the input:'))
# small=9
# sec_small=9
# while(n>0):
#     ld=n%10
#     if(ld<small):
#         sec_small=small
#         small=ld
#     if ld<sec_small and ld!=small:
#         sec_small=ld
#     n=n//10
# print(sec_small)

#4.Find the Missing Number
# n=int(input('enter the input:'))
# for i in range(10):
#     new=n
#     flag=0
#     while new>0:
#         ld=new%10
#         if ld==i:
#             flag=1
#             break
#         new=new//10
#     if flag==0:
#         print(i)

#5.Remove Consecutive Duplicate Characters
# s=input('enter the input:')
# new=''
# for ch in s:
#     if new == '' or ch!=new[-1]:
#         new=new+ch
# print(new)

#6.pyramid of stars

#    *
#   ***
#  *****
# *******

# for j in range(1,5,1):
#     for s in range(j,5,1):
#         print(' ',end='')
#     for i in range(1,j+1,1):
#         print('*',end='')
#     for k in range(1,j,1):
#         print('*',end='')
#     print()

#day 12
#1.Decimal to Binary
# n=int(input('enter the input:'))
# bin=0
# place=1
# while n>0:
#     rem=n%2
#     bin=bin+rem*place
#     place=place*10
#     n=n//2
# print("Binary:",bin)

#2.LCM of Two Numbers
# a=int(input('enter value of a:'))
# b=int(input('enter value of b:'))
# if(a>b):
#     greater=a
# else:
#     greater=b
#     flag=0
#     while True:
#         if greater%a==0 and greater%b==0:
#             print('LCM=',greater)
#             break
#         greater=greater+1

#3.
        #      *
        #     ***
        #    *****
        #   *******
        #    *****
        #     ***
        #      *

# for j in range(1,5,1):
#     for s in range(j,4,1):
#         print(' ',end='')
#     for i in range(1,j+1,1):
#         print('*',end='')
#     for k in range(1,j,1):
#         print('*',end='')
#     print()
# for x in range(1,4,1):
#     for d in range(1,x+1,1):
#         print(' ',end='')
#     for y in range(x,4,1):
#         print('*',end='')
#     for z in range(2,x-1,-1):
#         print('*',end='')
#     print()

#4.
        #    *******
        #     *****
        #      ***
        #       *

# for j in range(1,5,1):
#     for s in range(1,j,1):
#         print(' ',end='')
#     for i in range(j,5,1):
#         print('*',end='')
#     for k in range(3,j-1,-1):
#         print('*',end='')
#     print()

#5.Find the Digital Root

# n=int(input('enter the input:'))
# sum=0
# while(n>0):
#     ld=n%10
#     sum=sum+ld
#     n=n//10
#     news=0
# while sum>=10:
#      news=0
#      while(sum>0):
#         ld=sum%10
#         news=news+ld
#         sum=sum//10
#      sum=news
# print("Digital Root:",sum)

#6. Find the Largest Difference Between Adjacent Digits
# n=int(input('enter the number:'))
# larg=0
# while n>0:
#     dig1=n%10
#     n=n//10
#     dig2=n%10
#     diff=abs(dig1-dig2)
#     if(diff>larg):
#         larg=diff
# print('largest:',larg)


#day -13
#1.Harshad number
# n=int(input('enter the input:'))
# sum=0
# new=n
# while(n>0):
#     ld=n%10
#     sum=sum+ld
#     n=n//10
# if(new%sum==0):
#     print('harshad number')
# else:
#     print('not a harshad number')

#2.Automorphic Number
# n=int(input('enter the input:'))
# new=n
# sq=n*n
# count=0
# while(n>0):
#     ld=n%10
#     count=count+1
#     n=n//10
# res=sq%(10**count)
# if(res==new):
#     print('automorphic number')
# else:
#     print('not automorphic number')

#3.
# * * * *     
# *       *   
# *         * 
# *         * 
# *         * 
# *       *   
# * * * *     

# for j in range(1,8,1):
#     for i in range(1,7,1):
#         if(i==1 or j==1 and i<=4 or j==7 and i<=4 or j==2 and i==5 or j==6 and i==5 or i==6 and 3<=j<=5):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#4.Count Positive, Negative and Zero in list
# lis=list(map(int,input('Enter the list:').split()))
# counte=0
# countn=0
# countz=0
# for i in range(0,len(lis)):
#     if(lis[i]>0):
#         counte=counte+1
#     elif(lis[i]<0):
#         countn=countn+1
#     else:
#         countz=countz+1
# print('Positive',counte)
# print('Negative:',countn)
# print('Zero:',countz)

#5.Find the Sum of All Elements in a List
# lis=list(map(int,input('Enter the list:').split()))
# sum=0
# for i in range(0,len(lis)):
#     sum=sum+lis[i]
# print('sum:',sum)
    
#6.Count Even and Odd Elements in a List
# lis=list(map(int,input('enter the list:').split()))
# counte=0
# countO=0
# for i in range(0,len(lis)):
#         if(lis[i]%2==0):
#              counte=counte+1
#         else:
#             countO=countO+1
# print('Even :',counte)
# print('odd :',countO)

#7.

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print('*',end='')
#     print()
# for x in range(4,0,-1):
#     for y in range(1,x+1,1):
#         print('*',end='')
#     print()

# A
# BB
# CCC
# DDDD
# EEEEE
# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print(chr(64+j),end='')
#     print()

#10.Find the First Repeated Word
# s=input('enter the input:')

#5926830
# n=int(input('enter the input:'))
# counte=0
# countO=0
# zero=0
# while(n>0):
#     ld=n%10
#     if(ld%2==0):
#         counte=counte*10+ld
#     elif(ld%2!=0):
#         countO=countO*10+ld
#     else:
#         zero=zero+1
#     n=n//10
# res=counte
# while(zero>0):
#         res=res*10
#         zero=zero-1

# print(f'{res}{countO}')


#Day-14
#1.Remove Consecutive Duplicate Characters
# s=input('Enter the input:')
# new=''
# for ch in s:
#     if new=='' or ch!=new[-1]:
#         new=new+ch
# print(new)

#2.ATM PIN verification

# att=0
# while(att<3):
#     pin=int(input('enter the pin:'))
#     if(pin==1234):
#         print('PIN verified')
#     else:
#         print('wrong pin')
#     att=att+1
# else:
#     print('card blocked')

#3.Mobile Recharge Validation 
# mob_number=int(input('enter your mobile number:'))
# count=0
# rec_amount=int(input('enter recharge amount:'))
# while(mob_number>0):
#     ld=mob_number%10
#     count=count+1
#     mob_number=mob_number//10
# if(count==10 and rec_amount>=10):
#     print('Recharge successful')
# else:
#     print('recharge not succesful')

#4.ATM Withdrawal
# acc_balance=int(input('enter account balance:'))
# with_draw=int(input('enter withdrwal amount:'))
# if(with_draw>0 and with_draw<=acc_balance and with_draw%100==0):
#     remaining=acc_balance-with_draw
#     print('remaing balance=',remaining)


#5.Password Strength Checker
# passw=input('enter the password:')
# count=0
# upper=0
# lower=0
# digit=0
# for ch in passw:
#     count=count+1
#     if('A'<=ch<='Z' ):
#        upper=1
#     elif('a'<=ch<='z'):
#         lower=1
#     elif('1'<=ch<='9'):
#        digit=1
# if(count>=8 and upper==1 and lower==1 and digit==1):
#     print('strong password')
# else:
#     print('not a strong password')


#6.Login System Function
# def login(username,password):
#     if(username=='admin' and password=='python123'):
#         return 'login successful'
#     else:
#         return 'Invalid username or password'
# print(login(input('username='),input('Password=')))

#7.Calculate Employee Salary
# def calulate_salary(basic_salary):
#     HRA=0.2*basic_salary
#     DA=0.1*basic_salary
#     gross=basic_salary+HRA+DA
#     return gross
# print(calulate_salary(int(input('enter basic salary:'))))


#rearrange digits in the numbers to get maximum number
# n=int(input('enter the input'))
# temp=n
# ans=0
# while(temp>0):
#     lar=0
#     rem=0
#     while(temp>0):
#         ld=temp%10
#         if(ld>lar):
#             rem=rem*10+lar
#             lar=ld
#         else:
#             rem=rem*10+ld
#         temp=temp//10
#     ans=ans*10+lar
#     temp=rem
# print('answer=',ans)

#or
# n=90348
# ans=0
# for i in range(9,-1,-1):
#     temp=n
#     while(temp>0):
#         ld=temp%10
#         if(ld==i):
#             ans=ans*10+ld
#         temp=temp//10
# print('answer=',ans)

#day -15
#1.
#Email Validation
# def emailvalidation(Email):
#     at=-1
#     dot=-1
#     spaces=0
#     for i in range(len(Email)):
#         if(Email[i]=='@'):
#              at=i
#         elif(Email[i]=='.'):
#              dot=i
#         elif(Email==''):
#             spaces=1
#     if(at!=1 and dot!=1 and spaces==0 and at<dot ):
#        print('Valid Email')
#     else:
#        print('Invalid Email')
# emailvalidation(input('enter the input:'))

#2.Local and Global Variable
# x=100
# def display():
#     x=50
#     print('Local variable:',x)
#     print('Global variable:',x)
# display()
    
#3.modify a Global Variable
# count = 0
# def increment():
#     global count                                                                                                                                                                                                       
#     count=count+1
#     print('Local variable:',count)
#     print('global variable:',count)
# increment()

#4.Bank Account Class
# class BankAccount:
#     Baccount_name='sai'
#     Balance=10000
#     def deposit(self,deposit):
#         self.Bdeposit=deposit
#         self.new_balance1=BankAccount.Balance+self.Bdeposit
#     def withdraw(self,withdraw):
#         self.Bwithdraw=withdraw
#         self.new_balance=self.new_balance1-self.Bwithdraw
#     def display(self):
#         print('Account name:',BankAccount.Baccount_name)
#         print('Balance:',BankAccount.Balance)
#         print('Deposit:',self.Bdeposit)
#         print('new balance:',self.new_balance1)
#         print('Withdraw:',self.Bwithdraw)
#         print('New balance:',self.new_balance)
# b1=BankAccount()
# b1.deposit(2000)
# b1.withdraw(3000)
# b1.display()

#5.Student Class
# class Student:
#     def assigndata(self,name,roll_number,branch,marks):
#         self.Sname=name
#         self.Sroll_number=roll_number
#         self.Sbranch=branch
#         self.Smarks=marks
#     def calculate_grade(self):
#         if(90<=self.Smarks<=100):
#             self.grade='A+'
#         elif(80<=self.Smarks<90):
#             self.grade='A'
#         elif(70<=self.Smarks<80):
#             self.grade='B'
#         elif(60<=self.Smarks<70):
#             self.grade='C'
#         elif(self.Smarks<60):
#             self.grade='D'
#     def display(self):
#         print('Name:',self.Sname)
#         print('Roll Number:',self.Sroll_number)
#         print('Branch:',self.Sbranch)
#         print('Marks:', self.Smarks)
#         print('Grade:',self.grade)
# s1=Student()
# s1.assigndata('Sai',101,'CSE',75)
# s1.calculate_grade()
# s1.display()

#6.MObile constructor
# class Mobile:
#     def __init__(self,brand,model,price,storage):
#         self.Sbrand=brand
#         self.Smodel=model
#         self.Sprice=price
#         self.Sstorage=storage
#     def display(self):
#         print('BRAND:',self.Sbrand)
#         print('Model:',self.Smodel)
#         print('price:',self.Sprice)
#         print('Storage:',self.Sstorage)
# m1=Mobile('samsung','galaxy s24',65000,'256GB')
# m1.display()

#day-16
#1.Compress Consecutive Characters
# s=input('Enter the input:')
# new=''
# count=0
# for ch in s:
#     if(new==''):
#         new=new+ch
#         count=1
#     elif(ch==new[-1]):
#         count=count+1
#     else:
#         print(f'{new[-1]}{count}',end='')
#         count=1
#         new=new+ch
# print(f'{new[-1]}{count}')

#2.First Non-Repeating Character
# s=input('enter the input:')
# for ch in s:
#     count=0
#     for x in s:
#         if(ch==x):
#             count=count+1
#     if(count==1):
#         print(ch)
#         break
            
#3.second largest digit
# n=int(input('enter the input:'))
# lar=0
# sec=0
# while(n>0):
#     ld=n%10
#     if(ld>lar):
#         sec=lar
#         lar=ld
#     if(ld>sec and ld!=lar):
#         sec=ld
#     n=n//10
# print('second largest digit:',sec)
            
#4.Maximum Digit Sum
# n=int(input('enter the input:'))
# maxs=0
# max_num=0
# for i in range(n):
#     num=int(input('enter number:'))
#     temp=num
#     sum=0
#     while(num>0):
#         ld=num%10
#         sum=sum+ld
#         num=num//10
#     if(sum>maxs):
#         maxs=sum
#         max_num=temp
# print(max_num)

#5.Shopping Bill
# am=int(input('Enter the amount:'))
# discount=0
# if(am<=1000):
#     discount=0
# elif(1000<am<5000):
#     discount=5
# elif(5000<=am<10000):
#     discount=10
# elif(am>=10000):
#     discount=15
# discount_a=am*discount/100
# final=am-discount_a
# print('Discount :',discount,'%')
# print('Discount amount:',discount_a)
# print('final amount:',final)

#day-17
#1.Remove All Duplicate Characters
# s=input('enter the input:')
# new=''
# for ch in s:
#     count=0
#     for x in s:
#         if(ch==x):
#             count=count+1
#     if(count==1):
#         new=new+ch
# print(new)

#2.Find the Smallest Missing Digit
# n=int(input('enter the input:'))
# for i in range(10):
#     temp=n
#     flag=0
#     while temp>0:
#         ld=temp%10
#         if ld==i:
#             flag=1
#             break
#         temp=temp//10
#     if flag==0:
#         print('smallest misiing digit:',i)
#         break
# else:
#     print('no digit is missing')

#3.First Character With Maximum Frequency
# s=input('enter the input:')
# maxc=0
# maxchar=''
# for ch in s:
#     count=0
#     for x in s:
#         if(ch==x):
#             count=count+1
#     if(count>maxc):
#         maxc=count
#         maxchar=ch
# print(f'{maxchar} --> {maxc} ')

#4.Second Most Frequent Character
# s=input('Enter the input:')
# smax=0
# maxc=0
# maxch=''
# smaxch=''
# for ch in s:
#     count=0
#     for x in s:
#         if(ch==x):
#             count=count+1
#     if(count>maxc):
#         smax=maxc
#         smaxch=maxch
#         maxc=count
#         maxch=ch
#     elif(count>smax and count<maxc):
#         smax=count
#         smaxch=ch
# print(f'{smaxch} ---> {smax}')    

# 5.Maximum Product of Two Adjacent Digits
# n=int(input('enter the input:'))
# new=n
# maxp=0
# prod=0
# newp=0
# prev=n%10
# n=n//10
# while(n>0):
#     ld=n%10
#     prod=prev*ld
#     if(prod>maxp):
#         maxp=prod
#         newld=ld
#         newp=prev
#     prev=ld
#     n=n//10
# print('maximum product:',maxp)
# print('digits:',newp,newld)

#6.Move All Zeros to the End
# n=int(input('Enter the input:'))
# dig=10**(len(str(n))-1)
# new=0
# zeros=0
# while(n>0):
#     ld=n//dig
#     if(ld==0):
#         zeros=zeros+1
#     else:
#         new=new*10+ld
#     n=n%dig
#     dig=dig//10
# for i in range(zeros):
#     new=new*10
# print(new)

#day-18
#1.Find the Number With the Smallest Digit Sum
# n=int(input('enter the number of inputs:'))
# minsum=9999999
# minnum=0
# for i in range(n):
#     num=int(input(f'enter {i+1} number:'))
#     temp=num
#     sum=0
#     while(num>0):
#         ld=num%10
#         sum=sum+ld
#         num=num//10
#     if(sum<minsum):
#         minsum=sum
#         minnum=temp
# print('number with smallest digit sum:',minnum)
# print('Digit sum:',minsum)

#2. Count Words Without Using split()
# w=input('enter the input:')
# count=1
# for ch in w:
#     if(ch==' '):
#         count=count+1
# print('number of words:',count)

#OR
# w=input('enter the input:')
# count=0
# for i in range (len(w)):
#     if(w[i]!=' '):
#         if(i==0 or w[i-1]==' '):
#             count=count+1
# print('number of words:',count)

#3.Find the First Capital Letter
# w=input('enter the input:')
# for ch in w:
#     if('A'<= ch <='Z'):
#         print('First capital letter:',ch)
#         break

#4.Remove Repeated Consecutive Words
# w=input('enter the input:')
# new=''
# word=''
# prev=''
# for ch in w:
#     if(ch!=' '):
#         word=word+ch
#     else:
#         if word!=prev:
#             new=new+word+' '
#         prev=word
#         word=''
# if(word!=prev):
#     new=new+word
# print(new)

#5.Convert First Letter of Each Word to Capital
# w=input('enter the input:')
# new=''
# for i in range(len(w)):
#         if(i==0 or w[i-1]==' '):
#                 if ('a'<=w[i]<='z'):
#                         new=new+chr(ord(w[i])-32)
#                 else:
#                         new=new+w[i]
#         else:
#                 new=new+w[i]
# print(new)
            
#6.Food Ordering System
# print('---menu---')
# print('1.Pizza - ₹250')
# print('2.Burger - ₹150')
# print('3.Sandwich - ₹100')
# print('4.Exit')
# opt=int(input('enter your choice'))
# match opt:
#     case 1:
#         print('Pizza')
#         q=int(input('enter the quantity:'))
#         price=250*q
#     case 2:
#         print('Burger')
#         q=int(input('enter the quantity:'))
#         price=150*q
#     case 3:
#         print('Sandwich')
#         q=int(input('enter the quantity:'))
#         price=100*q
#     case _:
#         print('Invalid choice')
# if(price>500):
#     discount=price*(10/100)
#     final=price-discount
#     print('final bill:',final)
# else:
#     final=price
#     print('final bill:',final)

#day-19
#1. Count Uppercase, Lowercase and Digits
# w=input('enter the input:')
# countU=0
# countL=0
# countD=0
# for ch in w:
#     if('A'<=ch<='Z'):
#         countU=countU+1
#     elif('a'<=ch<='z'):
#         countL=countL+1
#     elif('0'<=ch<='9'):
#         countD=countD+1
# print('Uppercase:',countU)
# print('Lowercase:',countL)
# print('Digits:',countD)

#2.Find the First Digit in a String
# w=input('enter the input:')
# for ch in w:
#     if('0'<=ch<='9'):
#         print('First digit:',ch)
#         break

#3.Reverse Each Word Without split()
# w=input('enter the input:')
# new=''
# start=0
# for i in range(len(w)):
#     if(w[i]==' '):
#         for j in range(i-1,start-1,-1):
#             new=new+w[j]
#         new=new+' '
#         start=i+1
# for j in range(len(w)-1,start-1,-1):
#     new=new+w[j]
# print(new)

#4.Find the Word With the Most Vowels
# w=input('enter the input:')
# count=0
# mcount=0
# word=''
# maxword=''
# for ch in w:
#     if(ch!=' '):
#         word=word+ch
#         if(ch=='a' or ch =='e'or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
#             count=count+1
#     else:
#         if(count>mcount):
#             mcount=count
#             maxword=word
#         count=0
#         word=''
        
# if(count>mcount):
#         mcount=count
#         maxword=word
# print('Words:',maxword)
# print('vowels:',mcount)

#5. Remove All Spaces and Count Them
# w=input('enter the input:')
# count=0
# new=''
# for ch in w:
#     if(ch==' '):
#         count=count+1
#     else:
#         new=new+ch
# print('word:',new)
# print('spaces removed:',count)

#6. Function – Student Attendance
# def attendence(name,total_days,present_days):
#     perc=(present_days/total_days)*100
#     if(perc>=75):
#         print('Attendence:',perc,'%')
#         print('status:Eligible')
#     else:
#         print('Attendence:',perc,'%')
#         print('status:Not Eligible')
# attendence(input('NAME:'),int(input('Total Days:')),int(input('Present:')))

#Day-20
#1.Replace Every Vowel With *
# w=input('enter the input:')
# new=''
# for ch in w:
#     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
#         new=new+'*'
#     else:
#         new=new+ch   
# print(new)

#2.Function – Calculate Employee Experience
# def employee(join_year,current_year):
#     exp=current_year-join_year
#     if(exp==0):
#         print('fresher')
#     elif(1<=exp<=2):
#         print('Junior')
#     elif(3<=exp<=5):
#         print('Experienced')
#     elif(exp>5):
#         print('Senior')
# employee(int(input('Joining Year:')),int(input('Current year:')))

#3.Class – Employee
# class Employee:
#     def __init__(self,name,basic_salary):
#         self.name=name
#         self.basic_salary=basic_salary
#     def cal_salary(self):
#         self.hra=0.2*self.basic_salary
#         self.da=0.1*self.basic_salary
#         if(self.basic_salary>50000):
#             self.bonus=0.05*self.basic_salary
#         else:
#             self.bonus=2000
#         self.gross=self.basic_salary+self.hra+self.da+self.bonus
#     def display(self):
#         print('HRA:',self.hra)
#         print('DA:',self.da)
#         print('Bonus:',self.bonus)
#         print('gross salary:',self.gross)
# e=Employee('sai',60000)
# e.cal_salary()
# e.display() 

#4. Constructor + Method – Mobile
# class Mobile:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def display(self):
#         if(self.price>50000):
#             self.category='Premium'
#         elif(20000<=self.price<=50000):
#             self.category='Mid range'
#         elif(self.price<20000):
#             self.category='Budget'
#         print('Brand:',self.brand)
#         print('model:',self.model)
#         print('price:',self.price)
#         print('category:',self.category)
# m=Mobile('Samsung','A55',35000)
# m.display()

#5.Single Inheritance – Vehicle
# class vehicle:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#     def displayveh(self):
#         print('brand of vehicle',self.brand)
#         print('color of vehicle:',self.color)
# class Car(vehicle):
#     def __init__(self,brand,color,model):
#         super().__init__(brand,color)
#         self.model=model
#     def displaycar(self):
#         super().displayveh()
#         print('car model:',self.model)
# c=Car('Honda','black','city')
# c.displaycar()

#6.Multiple Inheritance
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
                
#day-21
#1.Count Character Categories
# w=input('enter the input:')
# calpha=0
# cdigits=0
# cspecial=0
# for ch in w:
#     if('A'<=ch<='Z' or 'a'<=ch<='z'):
#         calpha=calpha+1
#     elif('0'<=ch<='9'):
#         cdigits=cdigits+1
#     else:
#         cspecial=cspecial+1
# print('Alphabets:',calpha)
# print('Digits:',cdigits)
# print('Special characters:',cspecial)

#2.First Non-Repeating Character
# w=input('enter the input:')
# for ch in w:
#     count=0
#     for x in w:
#         if(ch==x):
#             count=count+1
#     if(count==1):
#         print('first non repeating character:',ch)
#         break
# else:
#     print('No non repeating character')

#3.remove Consecutive Duplicate Characters
# w=input('enter the input:')
# new=''
# for i in range(len(w)):
#     if(i==0 or w[i]!=w[i-1]):
#         new=new+w[i]
# print(new)

#4. Find the Longest Word
# w=input('enter the input:')
# word=''
# maxlen=0
# longword=''
# for ch in w:
#     if(ch!=' '):
#         word=word+ch
#     else:
#         if(len(word)>maxlen):
#             maxlen=len(word)
#             longword=word
#         word='' 
# if(len(word)>maxlen):
#     maxlen=len(word)
#     longword=word
# print('Longest word:',longword)
# print('length:',maxlen)

#5.polymorphism
#single inheritance
# class Vehicle:
#     def move(self):
#         print('vehicle is moving')
# class Car(Vehicle):
#     #overriding
#     def move(Self):
#         print('car is driving on the road')
# c=Car()
# v=Vehicle()
# c.move()
# v.move()

#6.multilevel inheritance
# class Vehicle:
#     def move(self):
#         print('vehicle is moving')
# class Car(Vehicle):
#     #overriding 
#     def move(self):
#         print('car is driving on the road')
# class Sportscar(Car):
#     #overriding 
#     def move(self):
#         print('Sports car is racing at high speed')
# s=Sportscar()
# c=Car()
# v=Vehicle()
# s.move()
# c.move()
# v.move()




    










  
    
    





    


        






        
    



        

    

    







            











