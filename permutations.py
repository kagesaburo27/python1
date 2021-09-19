arr = input().split()
def permutation(arr):  
   if len(arr) == 0:  
       return []  
   if len(arr) == 1:  
       return [arr]  
   l = []  
   for i in range(len(arr)):  
       m = arr[i]  
       remain = arr[:i] + arr[i+1:]  
       for p in permutation(remain):  
            l.append([m] + p)  
   return l 
print([''.join(p) for p in permutation(arr)])