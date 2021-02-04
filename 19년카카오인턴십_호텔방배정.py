# 19년 카카오 겨울 인턴십 호텔 방 배정
# 시간 초과 
def solution(k, room_number):
    answer = []
    room = [n for n in range(1, k + 1)]
    for i in range(len(room_number)):
        if room_number[i] in room:
            answer.append(room_number[i])
            room.remove(room_number[i])
        else:
            z = min(room)
            answer.append(z)
            room.remove(z)
        i += 1
    return answer

# while문
# 시간 초과 
def solution(k, room_number):
    answer = []
    m = max(max(room_number), len(room_number))
    room = [n for n in range(1, m + 1)]
    i = 0
    while i != len(room_number):
        if room_number[i] in room:
            answer.append(room_number[i])
            room.remove(room_number[i])
        else:
            z = min(room)
            answer.append(z)
            room.remove(z)
        i += 1
    return answer
