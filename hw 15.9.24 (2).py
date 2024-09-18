# START
import random

    # exercise 1

num: int = random.randint(1,100)
tries = 1

print(num) # just for the test

x: int = int(input("Goose the number between 1 to 100: "))

while x != num:
    if x > num:
        print("Wrong!!! your number is too big")
        x: int = int(input("Goose the number between 1 to 100: "))
    else:
        print("Wrong!!! your number is too small")
        x: int = int(input("Goose the number between 1 to 100: "))
    tries += 1
else:
    print(f"BINGO, its took you {tries} tries!!!")

     # exercise 2


cities_sum = float == 0

for i in range(5):
    city_temp = float(input("Enter a city temp: "))
    while not -50 <= city_temp <= 45:
        city_temp = float(input("enter"))
    cities_sum += city_temp
print(f"The average temp in cities is {cities_sum / 5}°c")



















































# END