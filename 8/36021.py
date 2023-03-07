import itertools

strings = itertools.product('ВИШНЯ', repeat=6)
count = 0
for str in strings:
    line = ''.join(str)
    if line.count('В') <= 1 and line[0] != 'Ш' and line[-1] not in 'ИЯ':
        count += 1
print(count)

# II способ
count = 0
for i1 in 'ВИШНЯ':
    for i2 in 'ВИШНЯ':
        for i3 in 'ВИШНЯ':
            for i4 in 'ВИШНЯ':
                for i5 in 'ВИШНЯ':
                    for i6 in 'ВИШНЯ':
                        line = i1 + i2 + i3 + i4 + i5 + i6
                        if line.count('В') <= 1 and line[0] != 'Ш' and line[-1] not in 'ИЯ':
                            count += 1
print(count)
