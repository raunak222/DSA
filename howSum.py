# How Sum

# Recursion   # Time _Complexity--> O(n^m  *m)    m-->targetsum   n=len(arr)
def howSum(targetSum,arr):
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    for num in arr:
        rem=targetSum-num
        comb=howSum(rem,arr)
        if comb!=None:
            return comb+[num]
    return None    

targetSum=10
arr=[2,5]
print(howSum(targetSum,arr))


# Memorization   Time _Complexity--> O(n* m^2)  
def howSum_m(targetSum,arr,memo):
    if  targetSum==0:
        return []
    if targetSum<0:
        return None
    if targetSum in memo:
        return memo[targetSum]
    for num in arr:
        rem=targetSum-num
        comb=howSum_m(rem,arr,memo)  
        if comb!=None:
            memo[targetSum]=comb+[num]
            return memo[targetSum]
    memo[targetSum]=None    
    return None    
targetSum=10
arr=[2,5]    
memo={}
print(howSum_m(targetSum,arr,memo))    

# Tabulation   Time -->O(m^2 *n) Space--> O(m^2)
                
def howSum_t(targetSum,arr):
    dp=[None]*(targetSum+1)
    dp[0]=[]
    for i in range(targetSum):
        if dp[i]!=None:
            for num in arr:
                if i+num<=targetSum:
                    dp[i+num]=dp[i]+[num]
    return dp[-1]

targetSum=10
arr=[2,5]                
print(howSum_t(targetSum,arr))
