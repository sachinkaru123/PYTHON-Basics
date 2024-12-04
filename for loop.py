#for counter in range(1,10):#start,stop,step
#   print(counter)

stop=0
count=int(input("Enter count that want to u :"))
while (stop!=count):
    print("Sachin" ,(count))
    stop=stop+1

print("closed the loop")

numbers = [3,2,5,7,8]
count = 0
for number in numbers:
    count+=1
    if number==5:
        break
else:
    count=-1
print(count)