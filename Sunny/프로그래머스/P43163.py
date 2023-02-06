'''
begin -> target
한번에 한 개의 알파벳만
즉 hot일 때 
words에 있는 단어로만 변환 가능
모든 단어의 길이는 같다
음...

'''

from collections import deque

def isSame(begin_words, target_words):
    for i in range(len(begin_words)):
        if begin_words[i] != target_words[i]:
            return False;
    return True;
    
    
def isChangeable(begin_words, target_words, word):
    idx = [];
    
    for i in range(len(word)):
        if begin_words[i] != word[i]:
            idx.append(i);
    
    if len(idx) == 1:
        return True;
    else:
        return False;

    
def solution(begin, target, words):
    answer = 0
    
    if target not in words: # O(n)
        return answer;
    
    begin_words = list(begin);
    target_words = list(target);
    
    for i in range(len(words)):
        words[i] = list(words[i])

    used_words = [];
    tmp = 0;
    # 두 단어가 같아질때까지
    while tmp < 1000:
        # words 문자열을 탐색하면서
        # 1개만 다름 + 다른 문자 하나가 target의 문자와 위치까지 같음 => 변경, answer++
        tmp += 1;
        for word in words:
            if isSame(begin_words, target_words):
                break;
            if isChangeable(begin_words, target_words, word) and word not in used_words:
                answer += 1;
                begin_words = word;
                used_words.append(word)
                print(begin_words);
                print(answer)

    
    return answer;
