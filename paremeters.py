def foo(a, b=[]): #default values get created once when program first runs
    b.append(a)
    return b
for i in range(10):
    print(foo(i))

def foo2(a, b=None):
    if b is None:
        b =[]
    b.append(a)
    return b
for i in range(9):
    print(foo2(i))