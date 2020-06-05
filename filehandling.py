# import os
# f=open("d:/ankasweaty.txt","w")
# writing=f.write("hi anka is cute girl")
# print(writing)
# f.close()

# ------------------------------------------------
# f=open("d:/ankasweaty.txt","r")
# reading=f.read()
# print(reading)
# f.close()

# -------------------------------------------------
# f=open("d:/ankasweaty.txt","a")
# appending=f.write("wrtiten some contents")
# print(appending)
# f.close()

# -------------------------------------------------
# f=open("d:/ankasweaty.txt","r")
# reading=f.read()
# print(reading)
# f.close()
# -----------------informations----------------------
# r=read mode
# w=write mode
# t=text mode
# b=binary
# + = read /write
# a=append
# x= file exit nahi to naya create

# --------------------------------------
# f=open("d:/ankasweaty.txt","r")
# contains=f.read(100)
# print(1,contains)
# f.close()
# f=open("d:/ankasweaty.txt","r")
# contains=f.read(100)
# print(2,contains)

# ---------------------------------------
# f=open("d:/ankasweaty.txt","r")

# f.seek(15)

# reading=f.read()

# print(reading)
# print(f.tell())
# -------------------------------------------
# a=10
# b=20
# print(f"a which have value {a} is greater") if a>b else print(f"b which have value {b} is greater")

# ---------------------------------------------
# def argu(*args,**kwargs):
#     print(args[1])
#     print(kwargs.values())

# drg=["raj","102",1,9,2,3,5,6,7,8]
# drg1={"raj":1,"dev":2}

# argu(*drg,**drg1)

# name= input("Enter Your String")
# key= int(input("Enter your Key"))

# for i in name[::]:
#     print(chr(ord(i)+key),end="")

# def print1(n):
#     m = 1

#     for i in range(1, n):
#         if(i != 2):
#             for j in range(1, n+1):
#                 print(m, end=" ")
#                 m += 1
#             print("\n")
#         else:
#             m = m+n
#             for j in range(1, n+1):
#                 print(m, end=" ")
#                 m += 1
#             print("\n")
#     for i in range(n+1, (n+n+1)):
#         print(i, end=" ")

# print1(6)

n=int(input("enter your number"))
m=n*n+1
dict={}
c=0
for i in range(1,m):
    print(i,end=" ")
    c+=1
    if (c%2!=0):
        dict.add({i:i})
        print(i,end="")

    
print(dict)
    
