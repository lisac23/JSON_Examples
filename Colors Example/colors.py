import json

with open('colors.json', 'r') as f:
    data = json.load(f)

print(data.keys())
print(data['colors'])

for color in data['colors']:
    print(color['color'])
    print(color.get('code'))
    print(color['code'].get('rgba'))
    for r in color['code'].get('rgba'):
        print(r)
    print(color['code'].get('hex'))