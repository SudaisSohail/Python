class A:

    def __init__(self):

        print("I am class A")

class B:

    def __init__(self):

        print("I am class B")

class C(B, A):

    def __init__(self):
        
        print("I am class C")
        super().__init__()

c1 = C()
print(c1)


