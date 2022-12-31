def maximum(num1, num2, num3):
    if(num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
        if(num1 > num1):
            return num1
        else:
            return num3
m = maximum(3, 5, 234)
print("The value of the maximun is " + str(m))