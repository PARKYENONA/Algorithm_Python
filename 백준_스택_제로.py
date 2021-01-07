# 백준 제로
k = int(input())
money = []

for _ in range(k):
   n = int(input())
   if n == 0:
     money.pop()
   else:
     money.append(n)

print(sum(money))
