# Match Case 

x = int(input())

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _:
        print(x)