# 8-6 개미전사
n = int(input())
food = list(map(int, input().split()))

# DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = food[0]
d[1] = max(food[0], food[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + food[i])

print(d[n - 1])
