# "Two Sum" Easy LeetCode Algorithms | Solution 1

class Solution:

    def two_sum(self, nums:list[int], target:int) -> list[int]:

        for i in range(len(nums)):
            value = target - nums[i]
            
            for j in range(len(nums)):
                if value == nums[j]:
                    return [i,j]
        
algorithms : Solution = Solution()
print(algorithms.two_sum([11,15,2,7],9))