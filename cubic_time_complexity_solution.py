"""
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
        max_sum = -10000
        
        for left in range(0, n):
            for right in range(left, n):
                # Primo check
                window_sum = 0

                # Aggiungere tutti gli elementi
                for k in range(left, right + 1):
                    window_sum += nums[k]

                # La somma più alta ottenuta fino a questo punto è stata superata?
                max_sum = max(max_sum, window_sum)

        return max_sum

# Unit Test

s = Solution()

array = [ -334, -452, -367, -284, -95, -122, -444, -456, -152, 25 ]

print(s.maxContiguousSubarraySum(array))

## Output = 25