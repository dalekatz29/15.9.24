# START

       # exercise 1

x: int = int(input("Enter a number: "))
counter: int = x

for i in range(1, x + 1):
    for i in range(1, i + 1):
        print(i, end=" ")
    print()

for y in range(x, 1, -1):
    for y in range(1, y):
       print(y, end=" ")
    print()


      # exersice 2

rows = int(input("Enter the rows number: "))

if rows > 0:
    for i in range(rows):
        for j in range(i, rows - 1):
            print(" ", end=" ")
        for _ in range(i + 1):
            print("*", end=" ")
        for _ in range(i):
            print("*", end=" ")
        print()
    print()





# END