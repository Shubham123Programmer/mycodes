#Faulty calculator for some operations

print("Enter first number:")
num1 = int(input())
print("Enter second number:")
num2 = int(input())


print("Enter your choice:")
print("1.Addition\n2.Subs\n3.Mult\n4.Div...")
choice = int(input())

if choice == 3 and num1 == 45 and num2 == 3:
    print("555")
elif choice == 1 and num1 == 56 and num2 == 9:
    print("77")
elif choice == 4 and num1 == 56 and num2 == 6:
    print("4")
 
if num1 != 56 and num2 !=9:
    if choice == 1:
        num1+num2
        print("Your sum is:", num1 + num2) 

elif choice == 2:
    num1-num2
    print("Your subs is:", num1 - num2)

if num1 != 45 and num2 != 3:
    if choice == 3:
        num1 * num2
        print("Your mult is:", num1 * num2)

if num1 != 56 and num2 != 6:
    if choice == 4:
        num1 / num2
        print("your div is", num1 / num2)     

if choice > 4:
    print("Wrong Choice!")






