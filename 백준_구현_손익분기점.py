# 백준 손익분기점
a, b, c = map(int, input().split())

n = 0

if b < c :
  n = a // (c - b)
  print(n + 1)
else:
  print(-1)
