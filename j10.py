def countPairsWithDiffK(arr, n, k): 
    count = 0
for i in range(0, n): 
for j in range(i+1, n) : 
              
            if arr[i] - arr[j] == k or arr[j] - arr[i] == k: 
                count += 1
                return count 
  

arr = [1, 5, 3, 4, 2] 
  
n = len(arr) 
k = 3
print ("Count of pairs with given diff is ", 
                countPairsWithDiffK(arr, n, k)) 
