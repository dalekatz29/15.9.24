# START

num = int(input('Enter a number: '))

if num % 5 == 0 and num % 3 == 0:
    print('Fizz Buzz')
elif num % 3 == 0:
    print('Buzz')
elif num % 5 == 0:
    print('Fizz')
else:
    print("The number isn't divisible by 5 or 3!")

# END