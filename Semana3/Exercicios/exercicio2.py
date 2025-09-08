lesser = 100000
larger = -100000

for i in range(5):
    num = int(input("Type a number in: "))
    if num < lesser:
        lesser = num
    if num > larger:
        larger = num

print(f"The lesser number is {lesser}, and the larger number is {larger}")