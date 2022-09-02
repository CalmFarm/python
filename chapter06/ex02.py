# 무한 루프를 돌면서
# 검색어를 입력 함
# 검색어로 exit을 입력하면 루프 종료
# 입력한 검색어의 검색 횟수 관리
# 검색어 : 카운트

keywords = {}

while True:
    keyword = input('검색어 :')

    if keyword == 'exit':
        break

    print('..........')
    # 검색어의 카운트를 1증가 시킴
    keywords[keyword] = keywords.get(keyword, 0)+1

    #정렬,
    #상위 10개 추출...        실시간 인기 검색어

for keyword, count in keywords.items():
    print(f'{keyword}:{count}')