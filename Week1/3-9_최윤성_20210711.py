lyric = '''baby sukhwan tururu turu
very cute tururu turu
in bed tururu turu
baby sukhwan'''.split()
num = int(input()) - 1
word = lyric[num % len(lyric)]
loop = num // len(lyric)
if word.count("ru") != 0:
    if word.count("ru") + loop > 4:
        print("tu+ru*" + str(word.count("ru") + loop))
    else :
        print(word + "ru" * loop)
else:
    print(word)