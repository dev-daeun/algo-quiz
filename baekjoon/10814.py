from sys import stdin

data = []
N = int(stdin.readline())
for _ in range(N):
    age, name = stdin.readline().split()
    data.append({
        'age': int(age),
        'name': name
    })

data = sorted(data, key=lambda x: x['age'])

for d in data:
    print('{} {}'.format(d['age'], d['name']))
