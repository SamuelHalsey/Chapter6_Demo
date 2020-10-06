import time

def hello(name="<You didn't Enter a name>"):
    print("Processing my favorite action....")
    print("Hello {}!".format(name))



def getAverage():
    print("Enter -1 to get the average.")
    num = int(input("Enter Numbers to average: "))
    total = []
    while num != -1:
        if num >= 0:
            total.append(num)
            num = int(input("Enter Numbers to average: "))

    return sum(total)/len(total)



def getAverage2():
    total = []
    try:
        num = int(input("Enter Numbers to average: "))
        while num:
           try:
               total.append(num)
               num = int(input("Enter Numbers to average: "))
           except ValueError:
               break
        return sum(total) / len(total)
    except ValueError:
        print("No value given")

def countDown():
    pass