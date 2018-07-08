fizzbuzz = ["fizz buzz" if i % 15 == 0 else "fizz" if i % 5 == 0 else "buzz" if i % 3 == 0
            else str(i) for i in range(1, 31)]

print(fizzbuzz)

for buzz in fizzbuzz:
    print(buzz.center(12, "*"))