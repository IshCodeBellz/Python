# Write your code below this line 👇


# def prime_checker(number):
#     if number % number == 0 and number % 1 == 0:
#         if number % 3 != 0 and number % 5 != 0 and number % 7 != 0 and number % 11 != 0 and number % 13 != 0:
#             print("It's a prime number.")

#         else:
#             print("It's not a prime number.")

#     else:
#         print("It's not a prime number.")


def prime_checker(number):
    prime = 0
    not_prime = 0
    for i in range(2, number):
        if number % i == 0:
            not_prime += 1

        else:
            prime += 1

    if not_prime > 0:
        print("It's not a prime number.")

    else:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



