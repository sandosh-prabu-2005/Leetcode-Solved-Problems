class Solution(object):
    def removeElement(self, nums, val):
        arr=[]
        if not nums: return 0
        for i in nums:
            if i is val:
                continue
            else:
                arr.append(i)
        nums[:len(arr)]=arr
        return len(arr)