class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addition = {} #value needed, index
        for i in range(len(nums)):
            if (target-nums[i]) in addition:
                solution = [addition[target - nums[i]], i]
                #print(solution)
                return solution
            else:
                addition[nums[i]] = i
        #print(addition)
      