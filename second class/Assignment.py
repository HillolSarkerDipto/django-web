Number= int(input("Enter your number"))

if (Number <=100 and Number >=80):
    print("A+")
elif ( Number <=79 and Number >=75):
    print("A")
elif (Number <= 74 and Number >=70):
    print("A-")
elif (Number <= 69 and Number >=65):
    print("B+")
elif (Number <= 64 and Number >=60):
    print("B")
elif (Number <= 59 and Number >=55):
    print("B-")
elif (Number <= 54 and Number >=50):
    print("C+")
elif (Number <= 49 and Number >=45):
    print("C")
elif (Number <= 44 and Number >=40):
    print("D")
elif (Number <=39 and Number >=0) :
    print("Fail")
else:
    print("Invalid number")
