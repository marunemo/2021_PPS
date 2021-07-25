x = input()
result = ""
if "x" in x:
    i = x.index("x")
    s = str(int(x[:i])//2)
    if s == "1" or s == "-1":
        result += s.replace("1", "")
    else:
        result += s
    result += "xx"
    x = x[i+1:]
    if x:
        if "-" not in x:
            result += "+"
            x = x[1:]
        if x == "1" or x == "-1":
            result += x.replace("1","")
        else:
            result += x
        result += "x"
else:
    if x == "1" or x == "-1":
        result += x.replace("1","")
    else:
        result += x
    result += "x"
if x == "0":
    print("W")
else:
    print(result + "+W")