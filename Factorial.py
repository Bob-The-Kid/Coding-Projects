n=int(input("Enter any number"))
factorial=1
for i in range(1,n+1):
    factorial *= i  #(factorial =factorial * i) is the same thing...
print(f"Write the factorial of {n} is {factorial}")