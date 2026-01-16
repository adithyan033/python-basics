try:
    a=int(input("num1"))
    b=int(input("num2"))
    print(a)
    c=a/b
    print(c)
except(ZeroDivisionError,TypeError):
    print("NOt possible division by zero")
else:
    print("try different input")