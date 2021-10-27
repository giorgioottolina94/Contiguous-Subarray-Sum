"""
Array di esempio:
    
index      0     1     2     3    4     5     6     7     8   9
Input: [ -334, -452, -367, -284, -95, -122, -444, -456, -152, 25 ]

O(n^2) Approach - Quadratic Time

"""

class Solution:
    def maxContiguousSubarraySum(self, nums):
        '''
        :type nums: list of int
        :rtype: int
        '''
        n = len(nums)
        # Valore minimo arbitrario
        max_sum = -1000000000

        # L'elemento più a sinistra sarà il punto di partenza del subarray contiguo
        for left in range(0, n):
            running_sum = 0
            # L'elemento a destra sarà l'indice finale del subarray
            for right in range(left, n):

                # Si aggiunge l'elemento corrente al valore ottenuto al punto precedente per ottenere la somma finale del subarray
                running_sum += nums[right]
                
                # La somma più alta ottenuta fino a questo punto è stata superata?
                max_sum = max(max_sum, running_sum)

        return max_sum

# Unit Test

s = Solution()

array = [ -334, -452, -367, -284, -95, -122, -444, -456, -152, 25 ]

print(s.maxContiguousSubarraySum(array))

## Output = 25