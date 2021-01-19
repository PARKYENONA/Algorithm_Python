# 8-1 피보나치 함수 
# 피보나치 함수를 재귀함수로 구현

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

# 8-2 피보나치 수열 (재귀적)
# 탑다운 다이나믹 프로그래밍 (Memoization)

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현
def fibo(x):
    # 종료 조건 (1 혹은 2 일때 1 반환)
    if x == 1 or x == 2:
         return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라 결과 반환
    d[x] = fibo(x - 1)  + fibo(x - 2)
    return d[x]

print(fibo(99))

# 8-3 호출되는 함수 확인
d = [0] * 100

def fibo(x):
    print('f(' + str(x) + ')', end = " ")
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

fibo(6)

# 8-4 피보나치 수열 소스코드 (반복문)
# 보텀업 다이나믹 프로그래밍

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100

# 첫 번쨰 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
