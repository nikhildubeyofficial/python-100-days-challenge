# Functions

a = 8
b = 9
# gmean = (a*b)/(a+b)
# print(gmean)

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

calculateGmean(a,b)
calculateGmean(4,5)
isGreater(5,3)
isGreater(a,b)