def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ret = []
    unit = []
    self.recur(ret,candidates,unit,target,0)
    return ret


def recur(self,ret,arr,unit,target,total):
    if total > target:
        return
    if total == target:
        ret.append(unit)
        return
    else:
        for i in range(0,len(arr)):
            unit.append(arr[i])
            #NOTE:we have to use unit[:] because if we
            #does not do this, list is mutable so that unit will be changed in place and
            #thus will chage the unit being pushed on ret.
            self.recur(ret,arr[i:],unit[:],target,total+arr[i])
            unit.pop()


#NOTE: Optimized version
def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ret = []
    unit = []
    self.recur(ret,candidates,unit,target,0,)
    return ret


def recur(self,ret,arr,unit,target,total):
    if total > target:
        return
    if total == target:
        ret.append(unit[:])
        return
    else:
        for i in range(0,len(arr)):
            unit.append(arr[i])
            self.recur(ret,arr[i:],unit,target,total+arr[i])
            unit.pop()

#NOTE: Best way
def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ret = []
    unit = []
    self.dfs(candidates,ret,unit,target,0,)
    return ret

def dfs(self,arr,ret,unit,target,s):
    if target < 0:
        return
    if target == 0:
        ret.append(unit)
        return
    for i in range(s,len(arr)):
        self.dfs(arr,ret,unit+[arr[i]],target-arr[i],i)
