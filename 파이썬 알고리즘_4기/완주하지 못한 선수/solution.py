def solution(participant, completion):
    participant_dict = {}

    for i in range(len(participant)):
        if participant[i] in participant_dict:
            participant_dict[participant[i]] += 1
        else:
            participant_dict[participant[i]] = 1

    for i in completion:
        participant_dict[i] -= 1

    for key, value in participant_dict.items():
        if value == 1:
            return key

participant = ['leo', 'kiki', 'eden']
completion = ['eden','kiki']
solution(participant, completion)