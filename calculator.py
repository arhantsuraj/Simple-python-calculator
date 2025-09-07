def calculator():
    print("Enter 1 if you want to add numbers")
    print("Enter 2 if you want to subtract numbers")
    print("Enter 3 if you want to multiply numbers")
    print("Enter 4 if you want to divide numbers")
    try:
        choice=int(input("Pick any of the operations you want:"))
        a=float(input("Enter your number:"))
        b=float(input("Enter your number:"))
        def add(a,b):
            return a+b
        def subtract(a,b):
            return a-b
        def division(a,b):
            return a/b
        def multiplication(a,b):
            return a*b
        if choice==1:
            print("result",add(a,b))
        elif choice==2:
            print("result",subtract(a,b))
        
        elif choice==3:
            print("result",multiplication(a,b))
        
        elif choice==4:
            print("result",division(a,b))
        else:
            print("Sorry invalid request")
    except ZeroDivisionError:
        print("infinity")
    except ValueError:
        print("Sorry your input is invalid!")
calculator()
        
