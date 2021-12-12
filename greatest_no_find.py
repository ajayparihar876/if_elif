print("Finding greatest among 4 num")

a= int(input("Enter the 1 num :-  "))
b= int(input("Enter the 2 num :-  "))
c= int(input("Enter the 3 num :-  "))
d= int(input("Enter the 4 num :-  "))

if a>b:
    f1 =a
else:
    f1 =b
if c>d:
    f2 =c
else:
    f2 =d

if (f1 > f2):
    print(str(f1) + " no. is greatest")
else:
    print(str(f2) + " no. is greatest")
