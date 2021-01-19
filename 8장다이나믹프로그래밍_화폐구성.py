# 8-8 효율적인 화폐 구성
n, m = map(int, input().split())
k = []
for _ in range(n):
    k.append(int(input()))

# DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 (보텀업)
d[0] = 0
for i in range(n):
    for j in range(k[i], m +1):
        if d[j - k[i]] != 10001:  # (i-k)원을 만드는 방법 존재 O
            d[j] = min(d[j], d[j - k[i]] + 1)

if d[m] == 10001: # 최종적으로 M원을 만드는 방법 X
    print(-1)
else:
    print(d[m])
