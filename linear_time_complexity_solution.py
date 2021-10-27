"""
Array di esempio:
    
index      0     1     2     3    4     5     6     7     8   9
Input: [ -334, -452, -367, -284, -95, -122, -444, -456, -152, 25 ]

O(n) Approach - Linear Complexity

"""

class Solution:
    def maxContiguousSubarraySum(self, nums):
        '''
        :type nums: list of int
        :rtype: int
        '''

        max_so_far = nums[0]
        max_ending_here = nums[0]
            
        # Check di tutti gli altri elementi nell'array, dall'indice 1 in poi
        for i in range(1, len(nums)):
            """
    
            Si può procedere in due modi:
    
            maxEndingHere + nums[i] --> sommiamo il valore dell'elemento all'indice i, al valore somma del subarray contiguo ottenuto fino all'indice i - 1
    
            nums[i] --> ricominciamo dall'ultimo elemento, ossia quello all'indice i, e il nuovo subarray assume questo valore
            
            Per esempio, utilizzando l'array definito inizialmente:

            index      0     1     2     3    4     5     6     7     8   9
            Input: [ -334, -452, -367, -284, -95, -122, -444, -456, -152, 25 ]

            1) Partendo all'indice 0, abbiamo -334
            2) Spostandoci all'indice 1, abbiamo ora due scelte: facciamo iniziare il nuovo subarray contiguo partendo dal valore di
               questo ultimo elemento (-452), o estendiamo il subarray precedente (indice 0) sommando ad esso l'elemento all'indice 1?
               -334 + (-452) = -786 --> diamo al nuovo subarray il valore -452 perché -452 > -786, e collochiamo -452 presso l'indice 1;
            3) Seguendo il ragionamento precedente, continuiamo per tutti gli indici successivi:
               Valore indice 2 = -367
               -452 + (- 367) = -819 --> diamo al nuovo subarray il valore -452, perché -452 > -819, e collochiamo -452 presso l'indice 2;
            ecc...

            """
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            
            # Il valore 'maxSoFar' è stato superato da 'maxEndingHere'?
            max_so_far = max(max_ending_here, max_so_far)

        return max_so_far

# Unit Test

s = Solution()

array = [ -334, -452, -367, -284, -95, -122, -444, -456, -152, 25 ]

print(s.maxContiguousSubarraySum(array))

## Output = 25