
# exercise 1 : 

# Task : Write a Python program to check if a given number is prime.


def prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


num = int(input("Enter a number: "))
print(prime(num))


"""

This function checks if a number is prime.

It returns False for numbers less than or equal to 1.

Then it checks all numbers from 2 up to the square root of n.

If any number divides n exactly, it is not prime.

If no divisors are found, the number is prime.

"""