lower = int (input("enter the lower limit for the range:"))
upper = int(input("enterb the upper limit of the range:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
