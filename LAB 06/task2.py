print("Multiplication Table")
num=int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#using while loop
i=1
while i<=10:
    print(f"{num} x {i} = {num * i}")
    i += 1