class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        Stoe open for n minutes 
        customers of length n
        customers[i] = # custoemrs that enter at the start of the ith minute and all those 
        customers leave at the end minute

        grumpy[i] == 1 if grumpy
        grumpuy[i] == 0 not grumpy

        if grumpy[i] == 1 then customers are NOT satisfied
        if grumpy[i] == 0 then customers are satisfied 

        secrete technique for not being grump for  minute consectutive minutes but only once 

        """
        left = 0
        curr = 0
       
        for right in range(len(customers)):
            if grumpy[right] == 0:
                curr += customers[right]
            
        
        # now do the sliding window on the minutes 
        magic_ans = 0
        magic_curr = 0
        for right in range(len(customers)):
            if grumpy[right] == 1:
                magic_curr += customers[right]
                
            while right-left+1 > minutes and left <= right:
                if grumpy[left] == 1:
                    magic_curr -= customers[left]
                left += 1
            magic_ans = max(magic_ans, magic_curr)
        print(magic_ans)
        return magic_ans + curr
        





