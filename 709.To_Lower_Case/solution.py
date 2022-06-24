class Solution:
    def toLowerCase(self, s: str) -> str:
        letters = {
            'A':'a',
            'B':'b',
            'C':'c',
            'D':'d',
            'E':'e',
            'F':'f',
            'G':'g',
            'H':'h',
            'I':'i',
            'J':'j',
            'K':'k',
            'L':'l',
            'M':'m',
            'N':'n',
            'O':'o',
            'P':'p',
            'Q':'q',
            'R':'r',
            'S':'s',
            'T':'t',
            'U':'u',
            'V':'v',
            'W':'w',
            'X':'x',
            'Y':'y',
            'Z':'z'
        }
        return letters.values()
        return ''.join([letters[letter] if letter in letters.keys() else letter for letter in s])
        # another way
        return s.lower()


solution = Solution()
print(solution.toLowerCase("LOVELY"))
