class Solution:
    def balancedStringSplit(self, s):
        prev_letters = ''
        split_counter = 0
        for idx, letter in enumerate(s):
            prev_letters += letter
            r_num = prev_letters.count('R')
            l_num = prev_letters.count('L')
            if r_num == l_num:
                split_counter += 1
                prev_letters = ''
        
        return split_counter


solution = Solution()
print(solution.balancedStringSplit("RLLLLRRRLR"))
