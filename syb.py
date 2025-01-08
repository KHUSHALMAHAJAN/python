a=[3,4,5,6]
print(a)
print(a[2]) 
a[1] = 1
print(a)

print("tuples")
t1 = ('a','b','c')
print(t1)
print(t1[1])
# t1[1] = 5  tuples not re-change value
print(t1)

print("dictionary")

a = {
    1 : "red",
    2 : "yellow",
    3 : "pink"
}
print(a)
print(a.keys())
print(a.values())
