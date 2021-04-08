# canConstruct

# recursion   Time _Complexity--> O(n^m *m)  Space -->O(m^2)  m--target_length  , n--> wordbank length
def canConstruct(target,wordbank):
    if target=='':
        return True
    for word in wordbank:
        if target.find(word)==0:
            suffix=target[len(word):]
            if  canConstruct(suffix,wordbank)==True:
                return True

    return False 
  
print(canConstruct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(canConstruct('abcdef',['ab','abc','cd','def','abcd']))

# Memo  # Time _Complexity--> O(n* m^2)  Space -->O(m^2)  m--target_length  , n--> wordbank length

def canConstruct_m(target,wordbank,memo):
    if  target in memo:
        return memo[target]
    if target=='':
        return True 
    for word in wordbank:
        if target.find(word)==0:
            suffix=target[len(word):] 
            if canConstruct_m(suffix,wordbank,memo)==True:
                memo[target]=True
                return True      
    memo[target]=False            
    return False
print(canConstruct_m('skateboard',['bo','rd','ate','t','ska','sk','boar'],{}))
print(canConstruct_m('abcdef',['ab','abc','cd','def','abcd'],{}))    
print(canConstruct_m('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee'],{})) 


# Tabulation   Time --> O(m^2 *n)   Space--> O(m)
def canConstruct_t(target,wordbank):
    dp=[False]*(len(target)+1)
    m=len(target)
    dp[0]=True
    for i in range(m):
        if dp[i]:
            for word in wordbank:
                if word==target[i:i+len(word)]:
                    dp[i+len(word)]=True
    return dp[-1]
print(canConstruct_t('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(canConstruct_t('abcdef',['ab','abc','cd','def','abcd']))    
print(canConstruct_t('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee'])) 
                    


