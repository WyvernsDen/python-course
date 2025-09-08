num = -1
sum = 0
avg = 0
i = 0

while True:
    try:
        num = int(input("Type a number in (0 exits the program): "))
        if num != 0:
            sum += num
            i += 1
        if num == 0:
            avg = sum / i
            print(f"The average of all the numbers is {avg}")
            break
    except:
        print("Error undefined")
