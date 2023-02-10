import sys

# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
def solution(a, b, c):
    f = ((a+b)%c);
    s = (((a%c)+(b%c))%c);
    t = ((a*b)%c);
    fo = (((a%c) * (b%c))%c);
    print(f, s, t, fo, sep='\n')


if __name__ == '__main__':
    a, b, c = map(int, input().split());
    solution(a, b, c);