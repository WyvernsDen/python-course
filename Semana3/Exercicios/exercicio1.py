even = 0
odd = 0

for i in range(10):
    num = int(input("Type a number in: "))
    if num % 2 == 0:
        even += 1
    if not num % 2 == 0:
        odd += 1
print(f"There are {even} even numbers, and {odd} odd numbers.")