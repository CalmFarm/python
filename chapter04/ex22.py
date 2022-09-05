datas = [
    'livingroom, temp, 24.5',
    'livingroom, humi, 60.4',
    'bedroom, temp, 28.5',
    'bedroom, humi, 60.2'
]

def load_date(datas):
    dict_list = []
    for line in datas:
        row = line.split(',')
        data = {
            'place' : row[0].strip(),
            'type' : row[1].strip(),
            'value' : float(row[2])
        }
        dict_list.append(data)

    return dict_list

dict_list = load_date(datas)

print(dict_list)

for data in dict_list:
    print(data)
