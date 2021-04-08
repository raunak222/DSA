# countConstruct


# recursion  Time _Complexity--> O(n^m *m)  Space -->O(m^2)  m--target_length  , n--> wordbank length
def countConstruct(target,wordbank):
    if target=='':
        return 1
    count=0    
    for word in wordbank:
        if target.find(word)==0:
            suffix=target[len(word):]
            numWays =countConstruct(suffix,wordbank)
            count+=numWays
    return count
  
print(countConstruct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(countConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countConstruct('purple',['p','ur','ple','purp','le','pu','urple']))


# Memo    # Time _Complexity--> O(n* m^2)  Space -->O(m^2)  m--target_length  , n--> wordbank length

def countConstruct_m(target,wordbank,memo):
    if target in memo:
        return memo[target]
    if target=='':
        return 1
    count=0    
    for word in wordbank:
        if target.find(word)==0:
            suffix=target[len(word):]
            numWays =countConstruct_m(suffix,wordbank,memo)
            count+=numWays
    memo[target]=count        
    return count
  
print(countConstruct_m('skateboard',['bo','rd','ate','t','ska','sk','boar'],{}))
print(countConstruct_m('abcdef',['ab','abc','cd','def','abcd'],{}))
print(countConstruct_m('purple',['p','ur','ple','purp','le','pu','urple'],{}))
print(countConstruct_m('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee'],{})) 

# Tabulation    Time--> O(m^2 *n)  Space --> O(m)

def countConstruct_t(target,wordbank):
    dp=[0]*(len(target)+1)
    dp[0]=1
    for i in range(len(target)):
        if dp[i]:
            for word in wordbank:
                if word==target[i:i+len(word)]:
                    dp[i+len(word)]+=dp[i]
    return dp[-1]

print(countConstruct_t('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(countConstruct_t('abcdef',['ab','abc','cd','def','abcd']))
print(countConstruct_t('purple',['p','ur','ple','purp','le','pu','urple']))
print(countConstruct_t('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee']))     


