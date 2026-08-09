def minimal(num1,num2,num3):
    return min(num1,num2,num3)
def maximal(num1,num2,num3):
    return max(num1,num2,num3)
def avrege(num1,num2,num3):
    return (num1+num2+num3) / 3 
def total(num1,num2,num3):
    return num1+num2+num3
num1 = max(min(float(input("please enter your {num1} : ")),20),0)
num2 = max(min(float(input("please enter your {num2} : ")),20),0)
num3 = max(min(float(input("please enter your {num3} : ")),20),0)
print(num1,num2,num3)
print("minimal : ",minimal(num1,num2,num3),"|", "maximal : ", maximal(num1,num2,num3),"|" ,"avrage : ",avrege(num1,num2,num3),"|","total : ",total(num1,num2,num3))

