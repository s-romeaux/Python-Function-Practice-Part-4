def rev_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

string_a = "Winifred"
string_b = "short-term"
string_c = "How now brown cow."

result_a = rev_string(string_a)
result_b = rev_string(string_b)
result_c = rev_string(string_c)

print(f"The reversed string of {string_a} is: {result_a}")
print(f"The reversed string of {string_b} is: {result_b}")
print(f"The reversed string of {string_c} is: {result_c}")