import operator

genres = [str(x) for x in input().split()]

plays = [int(x) for x in input().split()]


def solution(genres, plays):
    genre = {}
    play_genre = {}
    for ge in genres : genre[ge] = 0
    for i in range(len(genres)) :
        genre[genres[i]] += plays[i] 
        play_genre[(plays[i],i)] = genres[i]
    keys = genre.keys()
    keys = sorted(keys, key=lambda x : genre[x], reverse=True)
    answer = []
    for key in keys :
        agg = []
        for song in play_genre :
            if play_genre[song] == key :
                agg.append(song)
        ## multiple key 설정이 중요!!! -- 하나는 ascending, 나머지는 descending
        agg = sorted(agg, key = lambda x : (x[0],-x[1]), reverse=True)
        for i in range(len(agg)) :
            answer.append(agg[i][1])
            if i == 1 : break
    return answer

answer = solution(genres, plays)

print(answer)
