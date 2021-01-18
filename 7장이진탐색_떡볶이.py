# 실전 문제 떡볶이 떡 만들기

n, m = list(map(int, input().split()))
tteok =  list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점
start = 0
end = max(tteok)

# 이진 탐색 (반복법)
result = 0 
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in tteok:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    
    # 떡의 양이 부족해 더 많이 자르기 (왼쪽 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때 정답
        start = mid + 1

print(result)
