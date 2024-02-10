def num_within(number, start_range, end_range):
    return start_range <= number <= end_range

number1, start_range1, end_range1 = 3, 2, 4
number2, start_range2, end_range2 = 3, 1, 3
number3, start_range3, end_range3 = 10, 2, 5

result1 = num_within(number1, start_range1, end_range1)
result2 = num_within(number2, start_range2, end_range2)
result3 = num_within(number3, start_range3, end_range3)

if result1:
    print(f"{number1} falls between {start_range1} and {end_range1}: {result1}")
else:
    print(f"{number1} doesn't fall between {start_range1} and {end_range1}: {result1}")

if result2:
    print(f"{number2} falls between {start_range2} and {end_range2}: {result2}")
else:
    print(f"{number2} doesn't fall between {start_range2} and {end_range2}: {result2}")

if result3:
    print(f"{number3} falls between {start_range3} and {end_range3}: {result3}")
else:
    print(f"{number3} doesn't fall between {start_range3} and {end_range3}: {result3}")