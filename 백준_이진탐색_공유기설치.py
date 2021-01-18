# 백준 공유기 설치
n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]

x.sort()
start = 1 
end = x[-1] - x[0]  # 끝 집

# 이진 탐색 (반복법)
result = 0 
while(start <= end):
    mid = (start + end) // 2
    st = x[0] # 설치한 집
    count = 1
    for i in range(1, n):
        if x[i] >= st + mid: # 일정거리 위치한 집
            count += 1
            st = x[i] # 공유기 설치한 집 
    #  (오른쪽 탐색)
    if count >= c:
        start = mid + 1
        result = mid
    #  (오른쪽 탐색)
    else:
        end = mid - 1
    

print(result)
