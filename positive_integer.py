# Question 5

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    stack = []
    divisor = 2

    while n > 1:
        if n % divisor == 0 and is_prime(divisor):
            stack.append(divisor)
            n //= divisor
        else:
            divisor += 1

    while stack:
        print(stack.pop(), end=' ')

# Input an integer
num = int(input("Enter an integer: "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    print("Prime factors of", num, "in descending order:", end=' ')
    prime_factors(num)
