s = input()
s = s.lower()
s2 = []
for i in s:
    if i not in ['a', 'o', 'y', 'e', 'u', 'i']:
        s2.append(i)

for i in s2:
    print(f".{i}", end='')
