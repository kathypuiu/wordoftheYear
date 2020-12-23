import json
import operator

dictionar = {}
f = open('result.json', encoding="utf8")
data = json.load(f)


for campuri in data['chats']['list'][0]['messages']:
    if 'from' in campuri:
        if campuri['from'] == 'Cati' and type(campuri['text']) == str:
            cuvinte = campuri['text'].split(' ')
            for cuvant in cuvinte:
                dictionar.setdefault(cuvant.lower(), 0)
                dictionar[cuvant.lower()] += 1

# Converts the dict to a sorted array
cry = sorted(dictionar.items(), key=operator.itemgetter(1))
cry.reverse()
# print(dictionar['pepiz'])
for stuff in range(150):
    print(cry[stuff])
