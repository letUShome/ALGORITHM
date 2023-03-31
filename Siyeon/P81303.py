"""

"""
import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

table_idx = {}
table_pri = {}
deleted = []


def solution(n, k, cmd):
    global table, deleted
    # key-table속 순서, value-실제 idx
    for i in range(n):
        table_idx[i] = i
        table_pri[i] = i

    selected = k

    for c in cmd:
        if "D" in c:
            d, x = map(str, c.split())
            selected += int(x)

        elif "U" in c:
            u, x = map(str, c.split())
            selected -= int(x)

        elif "C" == c:
            priority = table_idx[selected]
            last_idx = len(table_idx) - 1

            for i in range(selected, last_idx):
                table_idx[i] = table_idx[i + 1]
                table_pri[table_idx[i]] = i

            if selected == last_idx:
                selected -= 1
            del table_pri[priority]
            del table_idx[last_idx]
            deleted.append(priority)

        else:
            priority = deleted.pop()
            idx = 0
            last_idx = len(table_idx) - 1
            for i in range(priority+1, n):
                if i in table_pri:
                    idx = table_pri[i]
                    break

            if idx != 0:
                for i in reversed(range(idx+1, last_idx+2)):
                    table_idx[i] = table_idx[i - 1]
                    table_pri[table_idx[i]] = i

                table_idx[idx] = priority
                table_pri[priority] = idx

            else:
                for i in reversed(range(priority)):
                    if i in table_pri:
                        idx = table_pri[i]
                        break

                table_idx[idx+1] = priority
                table_pri[priority] = idx+1


            if selected >= idx:
                selected += 1


    return table_pri


if __name__ == "__main__":
    n, k = 8, 2
    cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
    output = solution(n, k, cmd)
    answer = ""
    for i in range(n):
        if i in output:
            answer += "O"
        else:
            answer += "X"

    print(answer)
