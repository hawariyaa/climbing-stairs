# climbing stair
# this leet code question asks how may ways there are to climb a stair where one
# person can climb one stair or two stair at a time
# i used dynamic programming to solve the question
# we can solve it using fibonaci sereis where a number = (number - 1) + (number - 2)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one , two = 1, 1
        for i in range(n -1):
            temp = one
            one = one + two
            two = temp
        return one
n  = 10
number = Solution()
answer = number.climbStairs(n)
print(str(answer) + " ways")


