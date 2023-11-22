#Given two numbers, write a Python code to find the Maximum and Miminum of these two numbers without using maximum function:

def minimum(a,b):
    if a <= b:
        return a
    else:
        return b
a=9
b=18
print(minimum(a,b))


#: Find Maximum of two numbers Using max() function:

a=3
b=3
maximum=max(a,b)
print(maximum)