# 백준 주유소
n = int(input())
meter = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]*meter[0]
m = price[0]
d = 0

for i in range(1, n-1):
  if price[i] < m :
    min_price += m*d
    d = meter[i]
    m = price[i]
  else:
    d += meter[i] 
  if i == n-2:
    min_price += m*d

print(min_price)
