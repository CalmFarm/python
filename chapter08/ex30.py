

try:
    with open('sensors.csv','r',encoding='utf8') as f:
        data = f.readlines()
        
        for row in data:
            row = row.strip().split(',')
            print(row)

except Exception as e:
    print(e)


