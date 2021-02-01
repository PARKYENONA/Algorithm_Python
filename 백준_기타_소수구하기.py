# 백준 소수 구하기
# 제출 정답
m, n = map(int, input().split())

def prime_sieve(m, n):
    n += 1
    sieve = [True] * n
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(2*i, n, i):
                sieve[j] = False
    for i in range(m, n):
        if i > 1:
            if sieve[i]:
                print(i)

prime_sieve(m, n)

import math
m, n = map(int, input().split())

# 처음엔 모든 수가 소수(True)로 초기화(0, 1은 제외)
array = [True for i in range(n + 1)] 

# 에라토스테네스의 체 알고리즘
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우(남은 수)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2 
        while i * j <= n:
          array[i * j] = False
          j += 1

# 모든 소수 출력
for i in range(m, n + 1):
    if array[i]:
        print(i)
