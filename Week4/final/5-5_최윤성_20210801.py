class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for i in range(n):
            answer.append("")
            if i % 3 == 2:
                answer[i] += "Fizz"
            if i % 5 == 4:
                answer[i] += "Buzz"
            if answer[i] == "":
                answer[i] = str(i+1)
        return answer