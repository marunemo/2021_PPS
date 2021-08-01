class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        i = 1
        while i <= n:
            if i == n:
                return True
            i *= 4
        return False