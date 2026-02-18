class Solution(object):
    def longestCommonPrefix(self, strs):
        first_word = strs[0]
        for i in range(len(first_word)):
            current_sub = first_word[:i+1]
            for s in strs:
                if not s.startswith(current_sub):
                    return first_word[:i]
        return first_word