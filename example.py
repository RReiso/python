import helper  # name if the file - or import helper as yourname
#  or -  from helper import some_function, a or * - then you can reference directly by the name
helper.some_function()
print(helper.a)

print(1)
print("keee")
print(2*6)
print("kkw" + " ll " + str(7.5))
print(f"kkw ll  {7.5}")  # f - format
to_seconds = 24 * 60 * 60


def fun_function(some_param=8):
    print("hey")
    print(some_param)


fun_function()
fun_function(9)

# b = input("Tell me something\n")  # receives a string
# print(b)

# expression evaluates to a single value

c = fun_function()
print(c)  # None


def fun_function2(some_param=86):
    return some_param


d = fun_function2()
print(d)

# e = int(input())

if 5 > 0:
    print(9)
elif 4 > 5:
    print(4)
else:
    print(1)

print(9) if 5 > 0 else print(1)

print(type(5 > 0))  # <class 'bool'>
print(type(5.5))  # <class 'float'>

print("19.5".isdigit())  # False
print("19.5s".isdigit())  # False
print("19".isdigit())  # True

try:
    int("oo")
except ValueError:  # you can specify error type
    print("Boo!")

a = 0
while True:
    if a > 5:
        break
    else:
        print(a)
        a += 1

d = [10, True, "dd"]
d.append(8)
print(d)

for el in d:
    print(el)

print("1 3 5".split())
print("1, 3, 5".split(", "))

print(set([1, 2, 3, 2, 3]))  # converts a list to a set -  {1, 2, 3}

a = {1, True, "hh", 3.45}
for el in a:
    print(el)  # order not guaranteed

a.add(5)
a.remove(1)

print([5, 8, 9, 5].count(5))  # counts occurances - 2

b = {"lala": 9, "kal": True, "lsds": "hhh"}
print(b["kal"])

for num in range(2, 5):
    print(num) # 2,3,4

