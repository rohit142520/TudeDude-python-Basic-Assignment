# sum of range of integer  by using for loop.
a=int(input("enter starting value of range: ", ))
b=int(input("enter last value of range: ", ))
total_sum = 0
for x in range(a,b+1):
    total_sum+= x
print("Total sum of given range:", total_sum)