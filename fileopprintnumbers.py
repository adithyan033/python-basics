n = int(input("enter number of elements: "))

# open file in write mode
f = open("numbers.txt", "w")

# store N numbers in file
for i in range(n):
    num = input("enter number: ")
    f.write(num + "\n")

f.close()

# open file in read mode
f = open("numbers.txt", "r")

numbers = []

# read numbers from file
for line in f:
    numbers.append(int(line.strip()))

f.close()

# sort the numbers
numbers.sort()

print("Numbers in sorted order:")
for num in numbers:
    print(num)
