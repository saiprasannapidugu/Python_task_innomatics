# s='hero'
# print(type(s))
# x="zero"
# print(type(x))
# z=''' Hello'''
# print(type(z))
# y=""" Fullstack@123"""
# print(type(y))


#purpose of triple qoutes
#1.
# a='''Hello
# world'''
# print(a)

#2.
# def myname():
#     """This function displays the name """

#     name='hero'
#     print('my name is:',name)
# myname()

# class Test:
#     """This class helps to display the method"""
#     def m1():
#         print('this is the m1')
# Test()

#Accessing the individual charcters
# s='hero'
# print(s[1])  #positive
# print(s[-3])   #negative

#slicing
# s='Python'
# print(s[1:4:1])   #positive
# print(s[-5:-2:1])  #negative

#display the first charcter and length and last index and last charcter of string
# s='Python'
# print('First charcter:',s[0])
# print('length of string:',len(s))
# print('last index of string:',len(s)-1)
# print('last charcter of string:',s[len(s)-1])

#traversing the string
#using index
# s='Python'
# lastindex=len(s)-1
# for i in range(0,lastindex+1,1):
#     print(s[i])

#or
# s='Python'
# for i in range(0,len(s),1):
#     print(s[i])

#direct iterating
# s='python'
# for ch in s:
#     print(ch)

#iterating string in reverse order
# s='python'
# for i in range(len(s)-1,-1,-1):
#     print(s[i])

#reverse the given string
# s='python'
# rev=''
# for i in range(len(s)-1,-1,-1):
#     rev=rev+s[i]
# print('reverse of string:',rev)

#check given string is palindrom or not
# s='madam'
# rev=''
# for i in range(len(s)-1,-1,-1):
#     rev=rev+s[i]
# if(rev==s):
#     print('given string is a palindrom')
# else:
#     print('given string is not a palindrom')



#copy string chacter by charcter into array
# s='hero'
# arr=[0]*len(s)
# for i in range(0,len(s),1):
#     arr[i]=s[i]
# print(arr)

#mutation
# s='hero'
# s[1]='x'  #we cannot update
# print(s)

# s='hero'
# s='zero'
# print(s)

#ASCII values
# s='C'
# print(s,'ascii value :',ord(s))

#ascii values to charcter
# n=100
# print(chr(n))

#convertiing uppercase to lowercase
# s='A'
# print('Upper:',s,'lower:',chr(ord(s)+32))

#coverting lower case to uppdercase
# s='b'
# print('lower:',s,'upper:',chr(ord(s)-32))

#converting string digit to normal digit
# s1='0'
# print(ord(s1)-48)

#Strings Task
#1.count the vowels in the given string
# s='Prasanna'
# countv=0
# for i in range(0,len(s),1):
#     ch=s[i]
#     if(ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         countv=countv+1
# print('number of vowels:',countv)

#2.count the alphabets,digits,symbols in given string
# s='Prasanna@2004'
# countA=0
# countD=0
# countS=0
# for i in range(0,len(s),1):
#     ch=s[i]
#     if('A'<=ch<='Z' or 'a'<=ch<='z'):
#         countA=countA+1
#     elif('0'<=ch<='9'):
#         countD=countD+1
#     else:
#         countS=countS+1
# print('number aplabets:',countA)
# print('number of digits:',countD)
# print('number of symbol:',countS)

#3.remove spaces from given string
# s='welcome to python'
# res=''
# for i in range(0,len(s),1):
#     ch=s[i]
#     if(ch!=' '):
#         res=res+ch
# print(res)

#4.converting lowercase string to uppercase string
# s='python'
# res=''
# for i in range(0,len(s),1):
#     ch=s[i]
#     res=res+chr(ord(ch)-32)
# print('Upper case:',res)

#5.converting uppercase string to lowercase string
# s='PYTHON'
# res=''
# for i in range(0,len(s),1):
#     ch=s[i]
#     res=res+chr(ord(ch)+32)
# print('Lower case:',res)

#6.display the sum of digits in given string
# s='python@123'
# sum=0
# for i in range(0,len(s),1):
#     ch=s[i]
#     if('0'<=ch<='9'):
#         sum=sum+(ord(ch)-48)
# print('sum:',sum)
