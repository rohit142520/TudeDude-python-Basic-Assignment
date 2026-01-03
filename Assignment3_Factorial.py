#Calculate Factorial using a Function
def fact(n1):
    x = 1
    while n1 > 1:
        x *= n1
        n1-= 1
    return x
n1 = int(input("Enter value of n1: "))
print(f"Factorial of {n1}: is {fact(n1)}")