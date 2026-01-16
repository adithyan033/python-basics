class A:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        return self.x * other.x

a1 = A(10)
a2 = A(20)

print(a1 * a2)
