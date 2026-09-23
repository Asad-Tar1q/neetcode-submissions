class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        if not s:
            return 0
        longestSub = 0
        seen = {}                      # stores char -> last index

        for r, char in enumerate(s):   # r IS the loop index; drop manual r += 1
            if char in seen and seen[char] >= l:
                l = seen[char] + 1     # jump past the old occurrence
            seen[char] = r             # record/update last index

            currentSub = r - l + 1
            longestSub = max(longestSub, currentSub)

        return longestSub