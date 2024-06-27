"""
Optimized Solution

Array di esempio:

index      0     1     2     3    4     5     6     7     8   9
Input: [ -334, -452, -367, -284, -95, -122, -444, -456, -152, 25 ]

O(n^3) Approach - Cubic Time

"""

class Solution:
    def maxContiguousSubarraySum(self, nums):
        '''
        :type nums: list of int
        :rtype: int
        '''
        n = len(nums)
        # Valore minimo arbitrario
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, n):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum

# Unit Test

s = Solution()

array = [ -334, -452, -367, -284, -95, -122, -444, -456, -152, 25 ]

print(s.maxContiguousSubarraySum(array))

## Output = 25
