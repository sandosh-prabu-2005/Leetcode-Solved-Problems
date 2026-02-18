class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num=set(nums)
        res=1
        print(num)
        while res in num :
            res += 1
        return res