import json

ar = []

with open('D:\\Work\\Python\\MyProject\\cenz.txt', 'r',  encoding='utf-8') as file:
    for i in file:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open('C:\\Users\\mybox\\Desktop\\cenz.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e)
