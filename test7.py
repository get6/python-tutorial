
def solution(participant , completion):
    participantTmp = list(participant)
    answer = ""
    for i in participantTmp:
        if i in completion:
            participant.remove(i)
            completion.remove(i)
    
    for i in participant:
        if not (i in completion):
            answer = i
            break

    return answer



print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', "mislav"]))