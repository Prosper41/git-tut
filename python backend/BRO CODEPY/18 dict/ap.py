capitals = {
    'usa': 'DC',
    'ghana': 'nsawam',
    'togo': 'lome',
    'france': 'paris',
    'morrocco': ' '
}

# print(capitals.get('nsawma'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

capitals.update({'Germany': 'Berlin'})
capitals.update({'usa': 'djankrom'})
capitals.pop('france')
capitals.clear()

for key,value in capitals.items():
    print(key, value)
