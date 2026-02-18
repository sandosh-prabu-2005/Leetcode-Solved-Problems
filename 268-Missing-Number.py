class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num=set(nums)
        res=0
        print(num)
        while res in num :
            res += 1
        return res
        