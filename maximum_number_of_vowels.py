class Solution(object):
    def maxVowels(self, s, k):
        v = "aeiou"
        count = 0
        maxc = 0
        for i in range(len(s)):
            if s[i] in v:
                count += 1
            if i >= k and s[i-k] in v:
                count -= 1
            if count > maxc:
                maxc = count
        return maxc
