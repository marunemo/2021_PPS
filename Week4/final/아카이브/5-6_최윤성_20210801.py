class Solution(object):
    def isPalindrome(self, s):
        s = list(filter(lambda x: x.isalnum(), s.lower()))
        return s == s[::-1]