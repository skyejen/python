def is_prime(num):
    if num <= 1:
        return False
    else:
        for digit in range (2, num):
            if num % digit == 0:
                return False
        return True

prime_num = 73
not_prime_num = 75

print(f"Is {prime_num} prime? {is_prime(prime_num)}")
print(f"Is {not_prime_num} prime? {is_prime(not_prime_num)}")