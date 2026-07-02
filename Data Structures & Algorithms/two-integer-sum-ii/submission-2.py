class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        targetmap = {}
        sol = []

        for i in range(len(numbers)):
            needed = target - numbers[i]
            if (needed) in targetmap:
                sol = [targetmap[needed], i+1]
                return sol
            else:
                targetmap[numbers[i]] = i+1
                print("Adding " + str(needed) + ", " + str(i))

        return sol