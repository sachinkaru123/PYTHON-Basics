#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2

def add(a,b):
     result=float(a)+float(b)
     return result

def subtract(a,b):
     result=float(a)-float(b)
     return result

def multiply(a,b):
     result=float(a)*float(b)
     return result

def divide(a,b):
    try:
        result=float(a)/float(b)
        return result
    except ZeroDivisionError:
        print("float division by zero")
        return " None"

def power(a,b):
     result= pow(int(a),int(b)) 
     return result

def remainder(a,b):
     result=float(a)%float(b)
     return result

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def inputfunc():
    num1=(input("Enter first number: " ))
    print((num1))
    if("$" in num1 ):
        start()
    elif("#" in num1 ):
        print("Done. Terminating")
        exit()

    num2=(input("Enter second number: "))
    print((num2))
    if("$" in num2 ):
        start()
    elif("#" in num2 ):
        print("Done. Terminating")
        exit()

    return(num1,num2) 
    

def select_op(choice):
    if((choice) == "#"):
        #program ends here
        print("Done. Terminating")
        exit()

    elif(choice=="$"):
        return True;
        
       
    elif(choice=="+"):
        num1,num2=inputfunc()
        print(str(float(num1))+ " + " + str(float(num2))+" = "+ str(add(num1,num2)))
            
    elif(choice=="-"):
        num1,num2=inputfunc()
        print(str(float(num1))+ " - " + str(float(num2))+" ="+str(subtract(num1,num2)))
            
    elif(choice=="*"):
        num1,num2=inputfunc()
        print(str(float(num1))+ " * " + str(float(num2))+" ="+ str(multiply(num1,num2)))
            
    elif(choice=="/"):
        num1,num2=inputfunc()
        print(str(float(num1))+ " / " + str(float(num2))+" ="+ str(divide(num1,num2)))
            
    elif(choice=="^"):
        num1,num2=inputfunc()
        print(str(float(num1))+ " ^ " + str(float(num2))+" ="+ str(power(num1,num2)))
        
    elif(choice=="%"):
        num1,num2=inputfunc()
        print(str(float(num1))+ " % " + str(float(num2))+" ="+ str(remainder(num1,num2)))
            
    else:
        print("Unrecognized operation")
        return False


#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
def start():
    while True:
        print("Select operation.")
        print("1.Add      : + ")
        print("2.Subtract : - ")
        print("3.Multiply : * ")
        print("4.Divide   : / ")
        print("5.Power    : ^ ")
        print("6.Remainder: % ")
        print("7.Terminate: # ")
        print("8.Reset    : $ ")
            
                # take input from the user
        choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
        print(choice)
        select_op(choice)
start()
