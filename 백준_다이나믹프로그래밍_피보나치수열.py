# 백준 피보나치수열
# 자료 입력
t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))

# 제출 답안
d0 = [1, 0]
d1 = [0, 1]

for i in range(2, 41):
    d0.append(d0[i - 1] + d0[i - 2])
    d1.append(d1[i - 1] + d1[i - 2])

for j in n:
    print(d0[j], d1[j])

d = [0, 0] * 40
d[0] = [1, 0]
d[1] = [0, 1]



# 런타임 에러,,, 왜인지 모르지만 ^__ㅠ
d = [[0, 0]]* 40
d[0] = [1, 0]
d[1] = [0, 1]

# 피보나치 수열 0, 1 count
for i in range(t):
    for j in range(2, n[i]+1):
        d[j] = [d[j - 1][0] + d[j - 2][0], d[j - 1][1] + d[j - 2][1]]

for k in n:
    print(d[k][0], end = " ")
    print(d[k][1])
