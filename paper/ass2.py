print("file Handing")
with open("demo.txt","w") as f:
    str = input("Enter a string :- ")
    f.write(str)
    f.close()
with open("demo.txt","r") as f:
    print(f.read())
    f.close()