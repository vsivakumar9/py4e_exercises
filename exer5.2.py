largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break

    try :
        sval = int(num)
        if largest is None :
        	largest = sval

        if smallest is None :
           	smallest = sval

        if sval < smallest :
            smallest = sval
        elif sval > largest :
            largest = sval
        else :
        	continue

    except :
        print('invalid input')
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
