# Question 6

def decimal_to_binary(decimal_num):
    stack = []

    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.append(remainder)
        decimal_num //= 2

    binary_num = ""
    while stack:
        binary_num += str(stack.pop())

    return binary_num if binary_num != "" else "0"


decimal_number = int(input("Enter a decimal number: "))

if decimal_number < 0:
    print("Please enter a non-negative decimal number.")
else:
    binary_result = decimal_to_binary(decimal_number)
    print(f"The binary equivalent of {decimal_number} is {binary_result}")
