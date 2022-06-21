class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        key_index = {
            'type': 0,
            'color': 1,
            'name':2
        }
        return sum([1 for item in items if item[key_index[ruleKey]] == ruleValue])


solution = Solution()
print(solution.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))
