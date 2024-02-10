def mult_list(numbers):
    product = 1

    for num in numbers:
        product *= num

    return product

list1 = [1, 2, 3]
list2 = [2, 2, 2]
list3 = [2, 5]

result1 = mult_list(list1)
result2 = mult_list(list2)
result3 = mult_list(list3)

print(f"The product of the numbers in {list1} is: {result1}")
print(f"The product of the numbers in {list2} is: {result2}")
print(f"The product of the numbers in {list3} is: {result3}")
