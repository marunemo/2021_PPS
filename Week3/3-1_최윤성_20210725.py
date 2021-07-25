class Solution(object):
    def checkRecord(self, s):
        conLate = 0
        absent = 0
        for i in s:
            if i == "A":
                absent += 1
            if i == "L":
                conLate += 1
            else:
                conLate = 0
            if absent == 2 or conLate == 3:
                return False
        return True