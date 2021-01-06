# 내 풀이 방법
# Q2

s = list(map(int, input().split()))
num = 0

for i in len(s):
  if s[i] <= 1 or num <= 1:
    num += s[i]
  else:
    num *= s[i] 

print(num)

# 모범답안
data = input()

# 첫 번쨰 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 더하기 수행
  num = int(data[i])
  if num <= 1 or result <= 1 :
    result += num
  else:
    result *= num

print(result)
