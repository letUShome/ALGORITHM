def solution(genres, plays):
    answer = []
    
    # 속한 노래가 많이 재생된 장르 -> 장르 내에서 많이 재생된 노래 -> 고유번호 오름차순
    
    # 변수 선언
    genre = {}
    
    # 속한 노래 장르 재생횟수 총합
    for i in range(len(genres)):
        if genres[i] not in genre:
            genre[genres[i]] = plays[i]
        else:
            genre[genres[i]] += plays[i]
    
    # 재생횟수 내림차순 정렬
    # lamda 식을 활용하여 정렬: 각 키 x의 [0, 1] 중 [1]번째 값을 key로 두어 정렬
    genre = sorted(genre.items(), key=lambda x: x[1], reverse=True) # dict -> list 형변환
    # print(genre)
    
    # 장르 내에서 많이 재생된 노래 2개 우선 수록
    for i in range(len(genre)):
        in_genre = {}
        for j in range(len(genres)):
            if genres[j] != genre[i][0]:
                continue
            else:
                in_genre[j] = plays[j]
        in_genre = sorted(in_genre.items(), key=lambda x: x[1], reverse=True)
        if len(in_genre) < 2:
            answer.append(in_genre[0][0])
        else:
            answer.append(in_genre[0][0])
            answer.append(in_genre[1][0])
        # print(in_genre)
                
    
    return answer
