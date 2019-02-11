def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return ('Fizz Buzz')
    elif num % 3 == 0:
        return ('Fizz')
    elif num % 5 == 0:
        return ('Buzz')
    else:
        return num


for num in range(1, 17):
    print(fizzbuzz(num))
