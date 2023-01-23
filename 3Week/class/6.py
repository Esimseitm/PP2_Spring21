listnumber = (110025, 9646, 5686746, 2, 4547, 5158 , 557 , 888)

def is_prime(n):
    
    for i in range(2, n//2):
        if n%i == 0:
            return False
    return True

result = filter(is_prime, listnumber)
print(*result)