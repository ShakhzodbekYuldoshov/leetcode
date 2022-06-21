import math

class Solution:
    def countConsistentStrings(self, allowed, words):
        counter = 0
        for word in words:
            s_p = 0
            e_p = -1
            not_consistent = False
            for j in range(math.ceil(len(word)/2)):
                print(word, s_p, e_p)
                if word[s_p] not in allowed or word[e_p] not in allowed:
                    not_consistent = True
                    break
                s_p += 1
                e_p -= 1
            if not not_consistent:
                counter += 1
        return counter


solution = Solution()
print(solution.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
