fin = open('words.txt')

hi = fin.readline().strip()
i = 0

while i < 113809:
    if len(hi) > 20:
        print hi
    hi = fin.readline().strip()
    i = i + 1

