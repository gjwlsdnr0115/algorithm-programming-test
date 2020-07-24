def solution(genres, plays):
    answer = []
    genres_count = {}  # dict for total plays for each genre

    # add genre to dict
    for i in range(len(genres)):
        if genres[i] in genres_count.keys():
            genres_count[genres[i]] += plays[i]
        else:
            genres_count[genres[i]] = plays[i]

    # list of tuples of sorted dict
    sorted_count = sorted(genres_count.items(), key=(lambda x: x[1]), reverse=True)

    # list of tuples as (index, genre, plays)
    songs = []
    for i in range(len(genres)):
        songs.append((i, genres[i], plays[i]))

    # extend result to 'answer'
    for t in sorted_count:
        answer.extend(get_most_played(t[0], songs))

    return answer

def get_most_played(genre, songs):
    """Returns the two most played songs for a particular genre"""

    first = 0  # most played count
    second = 0  # second most played count
    first_idx = -1  # index of most played
    second_idx = -1  # index of second most played

    for item in songs:
        if genre == item[1]:  # correct genre
            if item[2] > first:  # if most played
                second = first
                second_idx = first_idx
                first = item[2]
                first_idx = item[0]
            elif item[2] > second:  # if second most played
                second = item[2]
                second_idx = item[0]

    if second_idx == -1:  # only 1 song
        return [first_idx]
    else:
        return [first_idx, second_idx]


