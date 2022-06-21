class Solution:
    def maxDepth(self, s):
        if '(' not in s:
            return 0
        open_brackets = ''
        num_brackets = []
        for char in s:
            if char == '(':
                open_brackets += char
            elif char == ')':
                num_brackets.append(len(open_brackets))
                open_brackets = open_brackets[:-1]
        
        return max(num_brackets)


solution = Solution()
print(solution.maxDepth("(1)+((2))+(((3)))"))
