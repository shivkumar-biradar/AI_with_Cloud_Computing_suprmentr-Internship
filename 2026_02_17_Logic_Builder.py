# Fizz Buzz 1-50
fizz_count = buzz_count = 0
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizz_count += 1
        buzz_count += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1
    else:
        print(i)

print(f"Total Fizz: {fizz_count}, Total Buzz: {buzz_count}")
