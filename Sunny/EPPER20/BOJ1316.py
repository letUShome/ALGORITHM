n = int(input())
answer = 0
for i in range(n):
    word = input()
    alphabet = [0 for _ in range(26)]
    isGroupWord = 1
    for i in range(len(word)):
        if i == 0:
            alphabet[ord(word[i]) - 97] = 1
            continue

        if word[i-1] != word[i] and alphabet[ord(word[i]) - 97] == 1:
            isGroupWord = 0
            break

        alphabet[ord(word[i]) - 97] = 1

    if isGroupWord == 1:
        answer += 1

print(answer)