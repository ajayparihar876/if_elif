print('Simple if elif')
a = int(input("enter the A  "))
b = int(input("enter the B  "))
if b > a:
    print("b is greatest")
elif a == b:
    print("a and b are equal")
else:
    print('a is greatest')


print()  # work as \n


print(' if_Elif_else statement')
a = int(input("enter  a   "))
b = int(input("enter  b   "))

if b > a:
    print("b is greater than A")
elif a == b:
    print("A nd b are equal")
else:
    print("A is greater then B")  # non executed then this statement


print('short hand if _ only one codition apply when A is greater otherwise skip the condition')
a = int(input('enter the A  '))
b = int(input('enter the B  '))
if a > b:
    print("A is grater then b")


print('short hand if else')

a = int(input('enter the A  '))
b = int(input('enter the B  '))

print(a)if a > b else print(b)
