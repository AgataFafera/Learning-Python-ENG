ef is_prime(num):
    if num == 1:
        return False
    elif num < 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

giv_num = int(input('Type your number: '))
print(is_prime(giv_num))
