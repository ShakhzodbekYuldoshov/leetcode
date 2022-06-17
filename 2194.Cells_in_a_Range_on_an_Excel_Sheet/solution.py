class Solution:
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    def cellsInRange(self, s):
        cells = []
        s = s.split(':')
        c1, r1, c2, r2 = self.letters.index(s[0][0]), int(s[0][1]), self.letters.index(s[1][0]), int(s[1][1])
        temp_r1 = int(r1)
        while c1 <= c2:
            r1 = temp_r1
            while r1 <= r2:
                cells.append(self.letters[c1]+str(r1))
                r1 += 1
            c1 += 1
        return cells


solution = Solution()
print(solution.cellsInRange("K1:L2"))
