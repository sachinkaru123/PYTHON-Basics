
i=0;
while(i<2):
    f=open("text01.txt");
    fcon=f.readline();
    fcon2=f.readline();
    i+=1
f2=open("sck.txt","w");
f2.write(fcon);
f2.write(fcon2);
f2.close()
f.close()

f2=open("sck.txt")
value=f2.read()
print(value);




#f1=open("text2.txt","r+");
#f1.write(fcon);
#cont=f1.read();
#print(cont);
#f.close();
#f1.close();
