num=22
if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            print("prime number")
            break
    else:
        print("Prime numebr")
else:
    print("Not a prime number")