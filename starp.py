for i in range(6):
    for j in range(i):
        print("*",end="")
    print()

for i in range(1,6):
    print("*" * i)
    

for i in range(6,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()

for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()


a=1
for i in range(5,0,-1):
    for j in range(i):
        print(" ",end="")
    print("* "*a)
    a+=1