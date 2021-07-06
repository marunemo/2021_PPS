testcase = int(input())
ratio = []
for i in range(testcase):
    scores = list(map(int, input().split()))
    ratio.append(len(list(filter(lambda x : x > sum(scores[1:])/scores[0], scores[1:]))) / scores[0])
for i in ratio: print("%.3f%%" % (i * 100))