
print ("PERTEMUAN 05.FOR LOOP")
print("\nJawaban ")
# Soal Pertemuan ke 05
print ("\nNo.1")
# 1. Aku cinta Indonesia
# 3. Aku cinta Indonesia
# 5. Aku cinta Indonesia

a=1
max=3
x=0
while(x<max):
    print (a,".aku cinta indonesia ")  
    a+=2
    x+=1

print ("\nNo.2") 
# 2 4 7 11 16 22

a=2
b=2
for i in range (6):
    print (a, end=" ")  
    a+=b
    b+=1

print ("\nNo.3")
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3

a=1
b=1
for i in range (3):
    print (a,"x",b,"=",b)  
    b+=1

print ("\nNo.4")
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

a=7
b=6
c=42
for i in range (5):
    print (a,"X ",b,"=",c)  
   
    b+=1
    c=b*a


print ("\nNo.5")
# * * * *
# * * * *
# * * * *


b = 3
k = 4
for i in range(b):
    for j in range( k):
        print('*  ',end='')
    print()  


print ("\nNo.6")
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
b = 3
k = 4
for i in range(1, b +1):
    for j in range( k):
        print(i," ",end='')
    print()

    
print ("\nNo.7")
# 1 1 2 3 5 8 13 21 34 55


a = 1
b = 1
c = b
for i in range(10):
    print(a, end = " ") 
    c = a + b
    a = b
    b = c
print ("\n")

print ("\nNo.8")
# 1 2 3 6 11 20 37 68 125 230
a = 1
b = 2
c = 3

print(a, end=" ")
print(b, end =" ")
print(c, end =" ")
for i in range(7):
    d = a + b + c
    print(d, end = " ")
    a = b
    b = c
    c = d
print("\n")


print ("\nNo.9")
# 1 1 1 1
# 1 1 1
# 1 1
# 1

baris = 4 

for i in range(baris, 0, -1):
    for j in range(i):
        print("1", end=" ")
    print()


print ("\nNo.10")   
# 2 3 2 3 2
# 3 2 3 2
# 2 3 2
# 3 2
# 2

for i in range(5):
    print()
    for j in range(5,i,-1):
        if i % 2 == 0:
            if j % 2 == 0:
                print(3, end=" ")
            else:
                print(2, end=" ")
        else :
            if j % 2 == 1:
                print(3, end=" ")
            else :
                print(2, end=" ")
   






    
    
