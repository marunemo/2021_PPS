class Solution(object):
    def addDigits(self, num):
        num = str(num)
        while len(num) > 1:
            num = str(eval("+".join(num)))
        return int(num)