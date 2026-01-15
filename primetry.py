def showprime(start,end):
    for num in range(start,end+1):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num)
n1=int(input("enter the starting range"))
n2=int(input("enter the ending range"))
print("prime numbers are")
showprime(n1,n2)