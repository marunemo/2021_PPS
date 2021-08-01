class Solution(object):
    def convert(self, s, numRows):
        con = ["" for _ in range(numRows)]
        row = 0
        rowDir = -1
        if numRows == 1:
            return s
        for i in s:
            con[row] += i
            if row == 0 or row == numRows - 1:
                rowDir *= -1
            row += rowDir
        return "".join(con)