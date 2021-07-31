class Solution(object):
    def backspaceCompare(self, s, t):
        sb = []
        tb = []
        for i in s:
            if i != "#":
                sb.append(i)
            elif sb:
                sb.pop()
        for i in t:
            if i != "#":
                tb.append(i)
            elif tb:
                tb.pop()
        return sb == tb