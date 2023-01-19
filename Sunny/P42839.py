from itertools import permutations

def all_prime_numbers():
    array = []
    prime_numbers = []
    number = 1000000
    
    for i in range(0, number):
        array.append(i)
    
    array[0] = 0
    array[1] = 0
    
    for i in range(2, number):
        if array[i] == 0:
            continue
        j = i * 2
        while j < number:
            array[j] = 0
            j += i
            
    for i in range(len(array)):
        if(array[i] != 0):
            prime_numbers.append(i)
            
    return prime_numbers

def solution(numbers):
    answer = 0
    
    # 0. 에라토스테네스의 체 활용 => 10000000(백만) 이하의 모든 숫자 소수판별
    prime_numbers = all_prime_numbers()
    
    # 1. 숫자 배열로 쪼개서 오름차순 sort
    array = []
    numbers = str(numbers)
    for i in range(len(numbers)):
        array.append(numbers[i])
    array.sort()
    
    # 2-1. 중복 방지를 위해 판별한 소수들 저장하는 배열
    primes = []
    
    # 3. 완탐
    for j in range(1, len(array)+1):
        for i in permutations(array, j):
            tmp = ''
            for k in range(j):
                tmp += i[k]
                if int(tmp) not in primes:
                    primes.append(int(tmp))
        
    print(primes)
    
    for i in range(len(primes)):
        if primes[i ] in prime_numbers:
            answer += 1
    
    return answer
