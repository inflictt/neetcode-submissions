class Solution:
    def pivotIndex(self, arr: List[int]) -> int:
        n = len(arr)
        
        prefixSum = 0
        prefixArr  = []
        
        suffixSum = 0 
        suffixArr =  [0]*n
        
        for i in range(n):
            prefixSum+=arr[i]
            prefixArr.append(prefixSum)

        for i in range(n-1,-1,-1):
            suffixSum+=arr[i]
            suffixArr[i] = (suffixSum)
            
        for i in range(n):
            if suffixArr[i]==prefixArr[i]:
                return i
        return -1
        