x = int(input("Type in a number: "))
print(f"Multiplication table for {x}:")

for i in range(1, 11):
    mult = i * x
    print(f"{x} * {i} = {mult}")