# allConstruct  

# Recusion   Time Complexity =O(n^m)  , Space=O(m)  m--target_length  , n--> wordbank length

def allConstruct(target,wordbank):
    if  target=='':
        return [[]]
    res=[]    
    for word in wordbank:
        if target.find(word)==0:
            suffix=target[len(word):]    
            suffixWays=allConstruct(suffix,wordbank)
            targetWays=[ [word]+ i for i in  suffixWays]
            if targetWays:
                res+=targetWays
    
    return res
print(allConstruct('purple',['purp','p','ur','le','urple']))    
print(allConstruct('skateboard',['bo','rd','ate','t','ska','sk','board','te']))

# Memo    Time Complexity =O(n^m)  , Space=O(m)  m--target_length  , n--> wordbank length   !!can't do better!! its always exponantial 

def allConstruct_m(target,wordbank,memo):
    if target in memo:
        return memo[target]
    if  target=='':
        return [[]]
    res=[]    
    for word in wordbank:
        if target.find(word)==0:
            suffix=target[len(word):]    
            suffixWays=allConstruct_m(suffix,wordbank,memo)
            targetWays=[ [word]+ i for i in  suffixWays]
            if targetWays:
                res+=targetWays
    memo[target]=res
    return res
print(allConstruct_m('purple',['purp','p','ur','le','urple'],{}))    
print(allConstruct_m('skateboard',['bo','rd','ate','t','ska','sk','board','te'],{}))
print(allConstruct_m('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee'],{})) 


# Tabulation    Time --> O(n^m)    Space-->O(n^m)

def allConstruct_t(target,wordbank):
    dp=[ [] for _ in range(len(target)+1) ]
    dp[0]=[[]]
    for i in range(len(target)):
        for word in wordbank:
            if word==target[i:i+len(word)]:
                newComb=[[word] for j in dp[i]]
                dp[i+len(word)]+=newComb
                       
    return dp[-1]

print(allConstruct_t('purple',['purp','p','ur','le','urple']))    
print(allConstruct_t('skateboard',['bo','rd','ate','t','ska','sk','board','te']))
print(allConstruct_t('eeeeeeeeeeef',['e','ee','eee','eeee','eeeee'])) 


