age = int(input("Enter your age"))
if age>=18:
    print("Do you have a nid")
    nid = int(input("Give your nid"))
    Id = int(input("Give your student id"))
    if nid == 1:
        print("you can give vote")
    elif Id == 1:
        print("you can give exam")
    else:
        print("you can't vote")

else:
    print("you are not eligable for vote")
