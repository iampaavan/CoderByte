import math


def prime_test(number):

    if number == 1:
        print(f"{number} not a prime.")
        return 1

    if number > 1:

        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                print(f"{number} not a prime.")
                break

        else:
            print(f"{number} is a prime.")

    else:
        print(f"{number} not a prime.")


prime_test(1)
prime_test(2)
prime_test(3)
prime_test(1000)

print(ord('i'))
