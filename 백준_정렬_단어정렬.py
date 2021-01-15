# 백준 단어 정렬
# 자료입력
n = int(input())
word = []

for _ in range(n):
    word.append(str(input()))

set_word = list(set(word))
sort_word =[]

for i in set_word:
    sort_word.append((len(i), i))

sort_word.sort()

for a, b in sort_word:
    print(b)
