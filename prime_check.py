def prime_check():

    number = int(input(f"Enter the number: "))

    if number == 2:
        print(f"{number} is a prime number.")

    else:
        if number > 1:

            for i in range(2, number):

                if number % i == 0:
                    print(f"{number} is not a prime number.")
                    break

            else:
                print(f"{number} is a prime number.")

        else:
            print(f"{number} is not a prime number.")


prime_check()
