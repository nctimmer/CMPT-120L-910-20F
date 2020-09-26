#Assignment 4
#Noah Timmer

def function1():
min = int(input("Enter the lower number of the range (1): "))
max = int(input("Enter the upper number of the range: "))

sum = 0

for x in range(min, max + 1):
    sum = sum + x

print("Sum:", sum)

def main():
    again = int(input("Enter a random number: "))
    sum = sum + again

