class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solutions = list()
        for i in range(len(nums)):
            a = 0
            b = len(nums)-1
            leftProd = 1
            rightProd = 1
            while(a < i):
                leftProd *= nums[a]
                a += 1
            while (b > i):
                rightProd *= nums[b]
                b -= 1
            
            solutions.append(leftProd*rightProd)
            print("L: " + str(leftProd) + "\nR: " + str(rightProd))
        print(solutions)
        return solutions

                
