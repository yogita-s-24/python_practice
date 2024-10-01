def a():
    print("a() start")
    b()
    d()
    print("a() returns")

def b():
    print("b() start")
    c()
    print("b() returns")

def c():
    print("c() start")
    print("c() return")

def d():
    print("d() start")
    print("d() return")

a()