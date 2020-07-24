def solution(participant, completion):
    names = {}  # init dict
    combined = participant + completion

    # add name to dict
    for name in combined:
        names[name] = names.get(name, 0) + 1

    # name with odd number value is answer
    for name in names.keys():
        if names[name] % 2 == 1:
            return name


print(solution(['leo', 'kiki', 'leo', 'eden'], ['eden', 'kiki', 'leo']))