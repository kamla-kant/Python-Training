"""
 Functions Summary
 """

# When we want to write same code again and again, instead
# of repeating, we can put in some block and reuse
# that block we called as function
# Many ways to write a function

print("1. Functions without arguments")
print("-" * 40)


# ------------------

def add():
    a = 10
    b = 20
    c = a + b
    print("c : ", c)


add()
add()
add()

print("-" * 40)
# ------------------


print("1. Functions with return")
print("-" * 40)


# ------------------

def add():
    a = 10
    b = 20
    c = a + b
    return c


res = add()
print("res : ", res)
print("-" * 40)
# ------------------


print("3. Functions with POSITIONAL arguments")
print("-" * 40)


# ------------------

def add(a, b):
    c = a + b
    print("c : ", c)


res = add(10, 20)
print("res : ", res)
print("-" * 40)
# ------------------

print("4. Functions with VARIABLE POSITIONAL arguments")
print("-" * 40)


# ------------------

def add(a, b=10, *c):
    d = a + b + sum(c)
    print("d : ", d)


res = add(10)  # a=10, b=10, c=()
print("res : ", res)

res = add(10, 20)  # a=10, b=20, c=()
print("res : ", res)

res = add(10, 20, 30, 40, 50, 60)  # a=10, b=20, c=(30,40,50,60)
print("res : ", res)

print("-" * 40)
# ------------------

###################################
# KEyword Args
###################################

print("3. Functions with POSITIONAL arguments")
print("-" * 40)


# ------------------

def add(*, a, b):  # * represents, after *, all args are keyword args
    c = a + b
    print("c : ", c)


res = add(a=10, b=20)  # Mandatory to metion arg name and values
print("res : ", res)
print("-" * 40)
# ------------------

print("4. Functions with VARIABLE POSITIONAL arguments")
print("-" * 40)


# ------------------

def add(*, a, b=10, **c):
    d = a + b + sum(c.values())
    print("d : ", d)


res = add(a=10)  # a=10, b=10, c={}
print("res : ", res)

res = add(a=10, b=20)  # a=10, b=20, c={}
print("res : ", res)

res = add(a=10, b=20, m=30, x=40, y=50, z=60)  # a=10, b=20, c={m=30, x:40,y:50,z:60}
print("res : ", res)

print("-" * 40)
# ------------------