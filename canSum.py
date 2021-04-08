# canSum

# recursive  Time _Complexity--> O(n^m)  
def canSum(targetSum,arr):
    if targetSum==0:
        return True
    if targetSum<0:
        return False    
    for num in arr:
        rem=targetSum-num
        if (canSum(rem,arr)==True):
            return True    
    return False

targetSum=30
arr=[7,14]
print(canSum(targetSum,arr))    

# memorization  Time _Complexity--> O(n*m)  
def canSum_m(targetSum,arr,memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum==0:
        return True
    if targetSum<0:
        return False    
    for num in arr:
        rem=targetSum-num
        if (canSum_m(rem,arr,memo)==True):
            memo[targetSum]=True
            return True   
    memo[targetSum]=False         
    return False

targetSum=30
arr=[7,14]
memo={}
print(canSum_m(targetSum,arr,memo))        

# Tabulation   Time _Complexity--> O(n*m)  Space--> O(m)
def canSum_t(targetSum,arr):
    dp=[False]*(targetSum+1)
    dp[0]=True
    for i in range(targetSum):
        if dp[i]:
            for num in arr:
                if i+num<=targetSum:
                    dp[i+num]=True
    return dp[-1]

targetSum=30
arr=[7,14]                
print(canSum_t(targetSum,arr))
