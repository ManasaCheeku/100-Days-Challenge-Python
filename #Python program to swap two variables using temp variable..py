#Python program to swap two variables using temp variable:
a=9
b=0
temp=a
a=b
b=temp
print("the value of a after swapping is:",a )
print("the value of b after swapping is:",b)



#Method 2: without using temp variable 
a=input("enter the value of a:")
b=input("Enter the value of b:")
a,b=b,a
print("The value of a after swapping is:", a)
print("The value of b after swapping is:", b)

