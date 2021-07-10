check = input().split()
ratio = list(map(float, input().split()))
part = dict()

part["good"] = ratio[2] if check[1] == "1" else ratio[0]
part["bad"] = ratio[3] if check[1] == "1" else ratio[1]

for _ in range(int(check[0]) - 1):
    gg, gb, bg, bb = part["good"] * ratio[0], part["good"] * ratio[1], part["bad"] * ratio[2], part["bad"] * ratio[3]
    part["good"], part["bad"] = gg + bg, gb + bb

print("%.0f %.0f" % (part["good"] * 1000, part["bad"] * 1000))