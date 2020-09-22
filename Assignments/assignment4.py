#Assignment 4
#Noah Timmer

 def Function1(self):
     lower = int(input("Enter the smallest number in the range: "))
     upper = int(input("Enter the biggest number in the range:  "))
     sum = 0
     
for n in range(lower, upper +1 ):
    sum = sum + n
    n = n + 1

print("The sum is: ", sum)

