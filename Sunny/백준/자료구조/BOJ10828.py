import sys
import math
from collections import deque

if __name__ == '__main__':
    n = int(input())
    q = deque();

    for i in range(n):
        cmd = sys.stdin.readline()

        # print("length of q: {0}",len(q))
        if 'push' in cmd:
            cmd, x = cmd.split()
            x = int(x)
            q.append(x)
        elif 'pop' in cmd:
            if len(q) != 0:
                x = q.pop()
                print(x)
            else:
                print(-1)
        elif 'size' in cmd:
            print(len(q))
        elif 'empty' in cmd:
            if len(q) != 0:
                print(0)
            else:
                print(1)
        elif 'top' in cmd:
            if len(q) == 0:
                print(-1)
            else:
                x = q.pop()
                q.append(x)
                print(x)
