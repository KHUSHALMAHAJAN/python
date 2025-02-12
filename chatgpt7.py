n = int(input("How many item enter in list :- "))
a = []
for i in range(0,n):
    temp = int(input(f"enter a element {i} :- "))
    a.append(temp)
print(a)
print(sum(a))
print(max(a))
print(min(a))
print(len(a))
print(all(a))
