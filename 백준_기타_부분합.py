# 백준 부분합
import sys
# n : 개수 s : 부분합
n, s = map(int, input().split())
num = list(map(int, input().split()))

interval_sum = 0
start, end = 0, 0
min_lenth = sys.maxsize

while True:
    if interval_sum >= s:
        min_lenth = min(min_lenth, end - start)
        interval_sum -= num[start]
        start += 1
    elif end == n:
        break
    else:
        interval_sum += num[end]
        end += 1

if min_lenth == sys.maxsize:
    print(0)
else:
    print(min_lenth)
