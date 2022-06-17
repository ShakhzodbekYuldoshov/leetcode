class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(', '').replace(')', '')


solution = Solution()
print(solution.interpret('(al)G(al)()()G'))
