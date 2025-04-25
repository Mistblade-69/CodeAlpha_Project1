#This is a task for making of the fibonacci generator

def fibonacci_generator(n):
    a,b=0,1
    print("The series is: ")
    print(a,b,end=" ")
    for i in range(n+1):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
    return("\nThis is the fibonacci generator")
#Example code
print(fibonacci_generator(10))
