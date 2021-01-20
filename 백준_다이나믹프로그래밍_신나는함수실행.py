# 백준 신나는 함수실행
d = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(d,a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c >20:
        return w(d, 20, 20, 20)
    if d[a][b][c] != 0:
        return d[a][b][c]
    if a < b and b < c:
         d[a][b][c] = w(d, a, b, c - 1) + w(d, a, b - 1, c - 1) - w(d, a, b - 1, c)
    else:
        d[a][b][c] = w(d, a - 1, b, c) + w(d, a - 1, b - 1, c) + w(d, a - 1, b, c - 1) - w(d, a - 1, b - 1, c - 1)
    return d[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w(%d, %d, %d) = %d" %(a, b, c, w(d, a, b, c)))
