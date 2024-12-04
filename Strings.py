def stringIndex():
    myString="Hello World";
    print(myString[2]);
    print(myString[-3]);
    print(myString[2:5]);
    print(myString[-5:]);
    print(myString[:-5]);
    print("<"+"sos"*5 +">")

def StringConcatinate():
    myString="sakalahansamale";
    print(myString[:1]); #s
    print(myString[1:]);#akalahansamale
    conStr= myString[:2]+"N";
    print(conStr)
    
def Activity():
    for i in range(3,2,-1): 
        print('!'*i)

#StringConcatinate();
#stringIndex();
Activity();