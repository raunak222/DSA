# Fibonacci

# recursion 
def fibo_r(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo_r(n-1)+fibo_r(n-2)
print(fibo_r(7))        

# memorization
def fibo(n):
    d={0:0,1:1}
    def helper(n):
        if n not in  d:
            d[n]= helper(n-1)+helper(n-2)
        return d[n]
    return helper(n)    
print(fibo(7))     

#Tabulation

def fibo_t(n):
    table=[0]*(n+1)
    table[1]=1
    for i in range(2,n+1):
        table[i]=table[i-1]+table[i-2]
    return table[n]
print(fibo_t(7))        

# No extra Space
def fibo_2(n):
    if n==0:
        return 0
    if n==1:
        return 1    
    a,b=0,1
    for _ in range(2,n+1):
        temp=a+b
        a=b
        b=temp
    return b
print(fibo_2(7))    
    

