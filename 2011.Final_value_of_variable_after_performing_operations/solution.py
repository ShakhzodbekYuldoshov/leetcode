class Solution:
    def finalValueAfterOperations(self, operations):
        return sum([1 if '+' in operation else -1 for operation in operations])

solution = Solution()
print(solution.finalValueAfterOperations(["++X","++X","X++"]))
