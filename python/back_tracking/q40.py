def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ret = []
    unit = []
    candidates.sort()
    self.dfs(candidates,ret,unit,target,0,)
    return ret

def dfs(self,arr,ret,unit,target,s):
    if target < 0:
        return
    if target == 0:
        ret.append(unit)
        return
    i = s
    while i < len(arr):
        self.dfs(arr,ret,unit+[arr[i]],target-arr[i],i+1)
        i += 1
        while i < len(arr) and arr[i] == arr[i-1]:
            i += 1
