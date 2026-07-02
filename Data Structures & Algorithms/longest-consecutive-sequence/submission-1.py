class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0
        for i in range(len(nums)):
            num = nums[i]
            if (num - 1) not in values:
                length = 1
                while (num + length) in values:
                    length += 1
                longest = max(length, longest)
        return longest
        
        