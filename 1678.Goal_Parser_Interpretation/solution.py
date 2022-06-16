class Solution:
    def interpret(self, command: str) -> str:
        print(command.split(')'))
        return ''.join(['o' if letter == '(' else letter.replace('(', '') for letter in command.split(')')])


solution = Solution()
print(solution.interpret('(al)G(al)()()G'))
