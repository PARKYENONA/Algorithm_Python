# 백준 수 찾기
# 자료 입력
n = int(input())
num1 = sorted(list(map(int, input().split())))
m = int(input())
num2 = list(map(int, input().split()))

# 백준 수 찾기 (재귀함수)
def bi_search(num, target, start, end):
    if start > end :
        return 0
    mid = (start + end) // 2
    if num[mid] == target:
        return 1
    elif num[mid] > target:
        return bi_search(num, target, start, mid -1)
    else:
        return bi_search(num, target, mid + 1, end)


# 이진 탐색의 시작과 끝
start = 0
end = n - 1

for i in range(m):
    print(bi_search(num1, num2[i], start, end))
