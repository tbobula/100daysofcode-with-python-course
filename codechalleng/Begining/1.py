def sum_numbers(numbers=None):
    sum = 0
    if numbers == None:
        for number in range(1,101):
            sum += number
        return sum

    for number in numbers:
        sum += number
    return sum


