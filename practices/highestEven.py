def highestEven(*numbers):
    highest = 0
    for num in numbers:
        if num % 2 == 0 and num > highest:
            highest = num
    print(f"The highest even number in the list is: {highest}")

highestEven(49,5,23,6,11,13,12,8,2)