#  백준 ATM
n = int(input())
t = list(map(int, input().split()))
new_t = sorted(t)
min_time = 0
min_time_list = []
sum_min_time = 0

for i in range(0, n):
    min_time += new_t[i]
    min_time_list.append(min_time)

sum_min_time = sum(min_time_list)
print(sum_min_time)
