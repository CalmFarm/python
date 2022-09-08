import json
data = {'name':'홍길동','birth':'0525','age':30}

with open('myinfo.json','w', encoding='utf8') as f:
    json.dump(data, f, indent=4 , ensure_ascii=False)

json_str=json.dumps(data,indent=4 , ensure_ascii=False)
print(json_str)