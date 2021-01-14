# 백준 수 정렬하기 선택 정렬
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if num[j] < num[min_idx] :
            min_idx = j
    num[i], num[min_idx] = num[min_idx], num[i]

for i in range(n):
    print(num[i])  

# 백준 수 정렬하기 삽입 정렬
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

for i in range(1, n):
    for j in range(i,0, -1):
        if num[j] < num[j-1]:
            num[j], num[j-1] = num[j-1], num[j]
        else:
            break

for i in range(n):
    print(num[i])  
