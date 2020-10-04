def findOppositeNumber(n, m): 
  
    if (m > (n // 2)) : 
        return (m - (n // 2)) 
  
    return (m + (n // 2)) 
  
# Driver code 
n = 10
m = 6
print(findOppositeNumber(n, m)) 