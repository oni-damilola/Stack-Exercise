# Question 5

def binary_to_decimal(binary_num):
    decimal_num = 0
    power = 0

    # Reversing the binary number to start calculating from the rightmost digit
    binary_num = binary_num[::-1]

    for digit in binary_num:
        # Converting each character (digit) to an integer
        bit = int(digit)
        # Adding the contribution of each bit to the decimal number
        decimal_num += bit * (2 ** power)
        power += 1

    return decimal_num

binary_number = input("Enter a binary number: ")
decimal_result = binary_to_decimal(binary_number)
print(f"The decimal equivalent of {binary_number} is {decimal_result}")
