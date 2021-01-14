# 백준 통계학
import sys
from collections import Counter

n = int(sys.stdin.readline())
num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

print(round(sum(num) / n))    # 산술평균
print(num[n//2])       # 중앙값
# 최빈값
if len(num) > 1:
    c = Counter(num).most_common(2)
    print(c[1][0] if c[0][1] == c[1][1] else c[0][0])
else:
    print(num[0])
# 범위
print(max(num) - min(num))

# 시간 초과  ^__^ 답안

n = int(input())
num = []

for _ in range(n):
    num.append(int(input())))

# 선택 정렬
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if num[j] < num[min_idx]:
            min_idx = j
    num[i], num[min_idx] = num[min_idx], num[i]

# 삽입 정렬
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(round(sum(num) / n))    # 산술평균
print(num[n//2])       # 중앙값
# 최빈값
if len(num) > 1:
    c = Counter(num).most_common(2)
    print(c[1][0] if c[0][1] == c[1][1] else c[0][0])
else:
    print(num[0])
# 범위
print(max(num) - min(num))
