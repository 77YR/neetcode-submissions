class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addition = {} #value needed, index
        for i in range(len(nums)):
            num = nums[i]
            if (target-num) in addition:
                solution = [addition[target - num], i]
                #print(solution)
                return solution
            else:
                addition[num] = i
        #print(addition)
      