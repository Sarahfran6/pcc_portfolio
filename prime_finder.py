

#determing if a number  is prime



#function for determining prime
def find_prime(number):
    is_prime = True
    for num in range(2, number):
        if number % num ==0:
            is_prime = False
            break
    if is_prime:
        print("This is a prime number")
    else:
        print("This is not a prime number")

number = int(input('Please enter a number: '))
find_prime(number)