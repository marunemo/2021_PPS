class Solution(object):
    def countAndSay(self, n):
        say = "1"
        for _ in range(n-1):
            count = ""
            prev = say[0]
            repeat = 1
            for i in say[1:]:
                if prev == i:
                    repeat += 1
                else:
                    count += str(repeat) + prev
                    prev = i
                    repeat = 1
            say = count + str(repeat) + prev
        return say