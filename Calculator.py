def continued():
    z = input("Do You Wish To Continue (Y/N): ")
    if z == "Y" or z == "y":
        calculator()
    else:
        quit()
            
def calculator():
    a = int(input("Enter The First Number: "))
    b = int(input("Enter The Second Number: "))

    x = int(input ("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nPlease Enter Your Input: "))

    if x == 1:
        c = a + b
        print ("The Sum = %d" % (c))
        continued()
    elif x == 2:
        if a > b:
            c = a - b
            print ("The Difference = %d" % (c))
            continued()
        elif a < b:
            c = b - a
            print ("The Difference = %d" % (c))
            continued()
        elif a == b:
            c = a - b
            print ("The Difference = %d" % (c))
            continued()
    elif x == 3:
        c = a * b
        print ("The Product = %d" % (c))
        continued()
    elif x == 4:
        if (a != 0 and b != 0):
            c = float(a) / float(b)
            print ("The Remainder = %.2f" % (c))
            continued()
        else:
            print ("Enter Non Zero Values")
            calculator()
    else:
        print ("Enter a  Valid Input")
        calculator()
        
calculator()
