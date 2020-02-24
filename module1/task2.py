numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
max_value = numbers[0]
min_value = numbers[0]
for n in numbers:
    try:
        temp = int(n)
        max_value = max(max_value, temp)
        min_value = min(min_value, temp)
    except ValueError:
        print(f"It is not possible to convert {n} to int")
print(f"Max value from the list is {max_value}")
print(f"Min value from the list is {min_value}")
