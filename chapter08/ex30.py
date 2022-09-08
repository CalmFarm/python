from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

try:
    with open('sensors.csv','r',encoding='utf8') as f:
        data = f.readlines()
        
        result = []
        for row in data[1:]:
            row = row.strip().split(',')
            row[0] = int(row[0]) # ID => int 변환
            row[3] = float(row[3]) # VALUE => float 변환
            row[4] = datetime.strptime(row[4], DATE_FORMAT)
            result.append(row)
            print(row)

        header, data = data[0].strip().split(','), result

        print(header)
        print("="*77)
        for row in data:
            print(row)

except Exception as e:
    print(e)


