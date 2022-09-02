# article의 문자열에 나오는 글자의 출현 회수 계산

article = '''
Trundling around the hallways of Hong Kong's Cyberport innovation hub,
the little Rice Robot is on a mission.
The stocky white cuboid resembles Star Wars' R2D2 robot in its build,
but has the wide-eyed expression of Pixar's WALL-E.
It's delivering drinks to patrons of the HFT Life cafe in a compartment in its "head"
which is unlocked by the customer using a PIN code sent to their phone.
While Rice's operations at the cafe are limited to distributing drinks,
the compact robot is already providing a range of services at venues in Hong Kong and Japan.
Rice is deployed as a bellhop at Hong Kong's Dorsett Wanchai hotel,
providing room service to guests.
In Tokyo, it delivers snacks to employees at SoftBank Group's headquarters from the building's 7-11 convenience store.
Earlier this year, Rice even made its TV debut on Cantonese drama series Communion,
delivering coffee to a cast member.
'''

# ' ','\n','.',',','\'','\"'
article = [ch for ch in article if ch not in ('7','2','1','-',' ','\n','.',',','\'','\"')]

spel_count = {}

for ch in article:
    spel_count[ch] = spel_count.get(ch, 0) + 1

for ch, count in spel_count.items():
    print(f'{ch} : {count}')

ch_list = list(spel_count) # ch_list = list(spel_count.keys())
ch_list.sort()

for key in ch_list:
    print(f'{key} : {spel_count[key]}')

items = list(spel_count.items())
print(items)

def what(x):
    # print(x)
    return x[1]

items.sort(key=what, reverse=True) # 컬렉션이 들어가있는 리스트 정렬하는방법

# items가 count가 값으로 정렬된다면
for ch, count in items[:5]: # Top-N 문자
    print(f'{ch}: {count}')