# BestSum 

#recursion   Time _Complexity--> O(n^m *m)    m-->targetSum   n-->len(arr)

def bestSum(targetSum,arr):
    shortestCombination=None
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    for num in arr:
        rem=targetSum-num
        remComb= bestSum(rem,arr)
        if remComb!=None:
            comb=remComb+[num]
            if shortestCombination==None or len(comb)<len(shortestCombination):
                shortestCombination=comb
    
    return shortestCombination
targetSum=10
arr=[1,2,5]    
print(bestSum(targetSum,arr))    

# memorization   Time _Complexity--> O(n* m^2)  

def bestSum_m(targetSum,arr,memo):
    shortestCombination=None
    if targetSum in memo:
        return memo[targetSum]
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    for num in arr:
        rem=targetSum-num
        remComb=bestSum_m(rem,arr,memo)
        if remComb!=None:
            comb=remComb+[num]
            if shortestCombination==None or len(comb)<len(shortestCombination):
                shortestCombination=comb 
                       
    memo[targetSum]=shortestCombination
    return shortestCombination
targetSum=10
arr=[2,5]  
memo={}  
print(bestSum_m(targetSum,arr,memo)) 

# Tabulation   Time --> O(m^2 *n)  Space-->O(m^2)

def bestSum_t(targetSum,arr):
    dp=[None]*(targetSum+1)
    dp[0]=[]
    for i in range(targetSum):
        if dp[i]!=None:
            for num in arr:
                if i+num<=targetSum:
                    comb=dp[i]+[num]
                    if dp[i+num]==None or  len(comb)<len(dp[i+num]):
                        dp[i+num]=comb
    return dp[-1]

targetSum=10
arr=[2,5]                
print(bestSum_t(targetSum,arr))
