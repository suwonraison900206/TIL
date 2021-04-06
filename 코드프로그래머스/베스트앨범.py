def solution(genres, plays):
    answer = []
    play_dict = {}

    for genre, play in zip(genres, plays):
        if genre not in play_dict:
            play_dict[genre] = play
        else:
            play_dict[genre] += play

    genre_dict = {}
    for genre, play in zip(genres, plays):
        if genre not in genre_dict:
            genre_dict[genre] = 0

    cnt = 0
    for genre, play in zip(genres, plays):
        if genre_dict[genre] == 0:

            genre_dict[genre] = [[play, cnt]]
        else:
            genre_dict[genre].append([play, cnt])
        cnt += 1

    for genre, lst in genre_dict.items():
        lst.sort(key=lambda x: (x[0], -x[1]))

    print(play_dict.keys())
    print(play_dict)
    while play_dict:

        k = max(play_dict.values())

        target = 0
        for key, value in play_dict.items():
            if value == k:
                target = key
                break

        if len(genre_dict[target]) >= 2:
            answer.append(genre_dict[target][-1][-1])
            answer.append(genre_dict[target][-2][-1])
        else:
            answer.append(genre_dict[target][-1][-1])

        del play_dict[target]


    return answer

genres=["classic", "pop", "classic", "classic"]
plays = [500, 600, 800, 800]

solution(genres,plays)