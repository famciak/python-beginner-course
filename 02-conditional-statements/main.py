print(" ")


name =input("please enter your name : ")

print(" ")

age = int(input("please enter your age : "))

print(" ")


if age >= 18:

    midterm = int(input("please input your midterm : "))

    print(" ")
    
    final_term = int(input("please input your final term "))
    
    print(" ")

    sum = (midterm + final_term) //2
    
    print(f"your avrage point is : {sum}")

    
    print(" ")


    if sum <= 50:
    
        
        print("you were failed in exam > you can try it later " ) 
        
        print(" ")
    
    elif sum >=50 and sum < 70:
    
        print(" you were passed the exam ")
    
    else:

        sum >= 70 and sum >= 100

        print("exllent")

else:

   print("you are a teenager try again later ")

