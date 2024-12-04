#read file inputs and process via this code and Write to Output
#Coded by - sachin_thennakoon

from warnings import catch_warnings
f1=open("inputs.txt","r");
f2=open("output.txt","w");
total=0
#storeing value in a list

listItem=f1.readlines();
for item in listItem:
    #print(type(item));
    total=total+int(item);
print(total);
f2.write("The Total is : "+ str(total))
