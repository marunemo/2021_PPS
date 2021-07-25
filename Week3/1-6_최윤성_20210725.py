class Solution(object):
    def generate(self, numRows):
        triangle = [[1]]
        for i in range(1, numRows):
            row = []
            for j in range(len(triangle[i-1])):
                if j == 0:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle