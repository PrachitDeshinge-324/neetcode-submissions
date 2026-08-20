class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1 
        iszero = False 
        zero_count = 0
        for i in nums:
            if i !=0:
                product*=i
            else:
                iszero = True
                zero_count+=1
        ans = []
        if zero_count > 1:
            ans = [0]*len(nums)
            return ans
        else :
            for i in nums:
                if i != 0 and iszero==False:
                    ans.append(int(product/i))
                elif i != 0 and iszero == True:
                    ans.append(0)
                else:
                    ans.append(product)
        return ans