n = int(input())
atm = list(map(int, input().split()))
atm.sort()

# 1, 3, 6, 9, 13

result = 0
wait = 0
for i in atm:
    result += wait + i
    wait += i
print(result)