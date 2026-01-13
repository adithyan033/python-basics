n1 = int(input("enter the starting number: "))
n2 = int(input("enter the ending number: "))

print("Numbers divisible by 9 are:")

for num in range(n1, n2 + 1):
    if num % 9 == 0:
        print(num)
