limit=int(input("enter the limit"))
print("prime numbers are",limit)
for num in range(2,limit+1):
    prime=True
    i=2
    while i<=int(num**0.5):
        if num%i==0:
            prime=False
            break
        i+=1
    if prime:
        print(num)