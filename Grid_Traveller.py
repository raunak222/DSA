# Grid TRaveler

# recursive
def Grid_Travel_r(m,n):
    if m==0 or n==0:
        return 0
    if m==1 and n==1:
        return 1
    return Grid_Travel_r(m-1,n)+Grid_Travel_r(m,n-1)
print(Grid_Travel_r(3,3))         

# memorization
 
def Grid_Travel_m(m,n):
    d={'1,1':1}
    def helper(m,n):
        if m==0 or n==0:
            return 0
        key=str(m)+','+str(n)
        if key not in d:
            d[key]=helper(m-1,n)+helper(m,n-1)
        return d[key]
    return helper(m,n)         
print(Grid_Travel_m(3,3))

# Tabulation

def Grid_Travel_t(m,n):
    grid=[[0 for _ in range(n+1)] for _ in range(m+1)]
    grid[1][1]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i==j==1:
                pass
            else:
                grid[i][j]=grid[i-1][j]+grid[i][j-1]
    return grid[m][n] 

print(Grid_Travel_t(3,3))          
