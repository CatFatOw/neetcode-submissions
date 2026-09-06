class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        arr: integer array
        return the max length of a subarray of arr

        TWO OPTIONS:
        
        if k is odd then arr[k] > arr[k+1]
        else arr[k] < arr[k+1]


        ir k is even then arr[k] > arr[k+1]
        else arr[k] < arr[k+1]

        APPORACH:

        two DP apporach

        we use a DP apporach for case 1 and another dp apporach another 1. iterating through all possibile positions we can then gtet it 

        """

        memo1 = {}
        memo2 = {}

        def dp1(i, prev):
            # if prev = 0 then it was >  if prev = 1 then it was < 
            if i == len(arr)-1:
                return 1
        
            if (i, prev) in memo1:
                return memo1[(i,prev)]
            
            best = 1
    
            # case 1: arr[k] > arr[k+1]
            if arr[i] > arr[i+1] and prev == 1:
                best  += dp1(i+1, 0)
            
            elif arr[i] < arr[i+1] and prev==0:
                best +=  dp1(i+1, 1)
            memo1[(i, prev)] = best 
            return best 

        def dp2(i, prev):
            if i == len(arr)-1:
                return 1
        
            if (i, prev) in memo2:
                return memo2[(i, prev)]
            
            best = 1
            
            if arr[i] > arr[i+1] and prev==0:
                best  += dp2(i+1, 1)
            
            elif arr[i] < arr[i+1] and prev==1:
                best +=  dp2(i+1,0)
            memo2[(i, prev)] = best 
            return best 

        ans = 1
        for i in range(len(arr)):
            ans = max(ans, max(dp1(i,0), dp2(i,0)))
        return ans
        

            

            

